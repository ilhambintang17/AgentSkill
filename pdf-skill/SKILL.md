---
name: pdf
description: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.
license: Proprietary. LICENSE.txt has complete terms
---

# PDF Processing Guide

## Overview

This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see REFERENCE.md. If you need to fill out a PDF form, read FORMS.md and follow its instructions.

## Prerequisites

Install required libraries before use. These may not be pre-installed:

```bash
# Try standard pip first; if PEP 668 blocks it, use --break-system-packages
pip install pypdf pdfplumber 2>/dev/null || pip install --break-system-packages pypdf pdfplumber
```

**Fallback for text extraction** if Python libraries are unavailable:
```bash
# pdftotext is often pre-installed via poppler-utils
pdftotext -layout input.pdf output.txt
```


## Quick Start

**CRITICAL FOR LLM AGENTS (Executing Python):** To use the Python snippets in this guide, you MUST write them to a temporary file (e.g., `scratch/process_pdf.py`) using your file writing tools, and then execute the file using the terminal tool. Do not try to execute code blocks directly.

```python
from pypdf import PdfReader, PdfWriter

# Read a PDF
reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

# Extract text
text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Python Libraries

### pypdf - Basic Operations

#### Merge PDFs
```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

#### Split PDF
```python
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output:
        writer.write(output)
```

#### Extract Metadata
```python
reader = PdfReader("document.pdf")
meta = reader.metadata
print(f"Title: {meta.title}")
print(f"Author: {meta.author}")
print(f"Subject: {meta.subject}")
print(f"Creator: {meta.creator}")
```

#### Rotate Pages
```python
reader = PdfReader("input.pdf")
writer = PdfWriter()

page = reader.pages[0]
page.rotate(90)  # Rotate 90 degrees clockwise
writer.add_page(page)

with open("rotated.pdf", "wb") as output:
    writer.write(output)
```

### pdfplumber - Text and Table Extraction

#### Extract Text with Layout
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

#### Extract Tables
```python
with pdfplumber.open("document.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            print(f"Table {j+1} on page {i+1}:")
            for row in table:
                print(row)
```

#### Advanced Table Extraction
```python
import pandas as pd

with pdfplumber.open("document.pdf") as pdf:
    all_tables = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table:  # Check if table is not empty
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)

# Combine all tables
if all_tables:
    combined_df = pd.concat(all_tables, ignore_index=True)
    combined_df.to_excel("extracted_tables.xlsx", index=False)
```

### reportlab - Create PDFs

#### Basic PDF Creation
```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf", pagesize=letter)
width, height = letter

# Add text
c.drawString(100, height - 100, "Hello World!")
c.drawString(100, height - 120, "This is a PDF created with reportlab")

# Add a line
c.line(100, height - 140, 400, height - 140)

# Save
c.save()
```

#### Create PDF with Multiple Pages
```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Add content
title = Paragraph("Report Title", styles['Title'])
story.append(title)
story.append(Spacer(1, 12))

body = Paragraph("This is the body of the report. " * 20, styles['Normal'])
story.append(body)
story.append(PageBreak())

# Page 2
story.append(Paragraph("Page 2", styles['Heading1']))
story.append(Paragraph("Content for page 2", styles['Normal']))

# Build PDF
doc.build(story)
```

#### Subscripts and Superscripts

**IMPORTANT**: Never use Unicode subscript/superscript characters (₀₁₂₃₄₅₆₇₈₉, ⁰¹²³⁴⁵⁶⁷⁸⁹) in ReportLab PDFs. The built-in fonts do not include these glyphs, causing them to render as solid black boxes.

Instead, use ReportLab's XML markup tags in Paragraph objects:
```python
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

# Subscripts: use <sub> tag
chemical = Paragraph("H<sub>2</sub>O", styles['Normal'])

# Superscripts: use <super> tag
squared = Paragraph("x<super>2</super> + y<super>2</super>", styles['Normal'])
```

For canvas-drawn text (not Paragraph objects), manually adjust font the size and position rather than using Unicode subscripts/superscripts.

#### Advanced Layout, Syntax Highlighting & Preventing Overlaps
When generating complex reports (e.g., side-by-side code comparisons, cheat sheets):
1. **Avoid HTML-to-PDF tools** (like headless Chrome) for complex code highlighting, as background colors and JavaScript execution (like Highlight.js) can fail or render inconsistently.
2. **Use Native ReportLab Tables** for side-by-side layouts. Calculate column widths dynamically (e.g., `landscape(A4)[0] / 2`).
3. **Prevent Overlaps:** Always use `PageBreak()` or `KeepTogether()` from `reportlab.platypus` to prevent tables and explanations from overlapping or breaking awkwardly across pages.
4. **Native Syntax Highlighting:** ReportLab's `Paragraph` supports basic HTML (`<font color="#HEX">`, `<b>`, `<i>`). You can write a simple tokenizer using Python's `re.split(r'(\W+)', text)` to manually highlight keywords, types, and comments without needing external CSS.
5. **CRITICAL: Font Size and Line Height (Leading):** When changing `fontSize` in `ParagraphStyle`, you MUST explicitly set the `leading` (line height) to be roughly `fontSize * 1.2` or higher (e.g., if `fontSize=22`, set `leading=28`). If you increase font size without setting `leading`, wrapped text lines will violently overlap into themselves and into adjacent paragraphs!
6. **STRICT PAGE CONSTRAINTS:** If the user demands fitting everything into exactly N pages (e.g. "fit everything into 2 pages"):
   - Radically reduce `fontSize` (e.g. down to 7 or 8 for code) and `leading` (to 8 or 9).
   - Slash margins (`rightMargin=15`, `leftMargin=15`, `topMargin=10`, `bottomMargin=10`).
   - Remove `Spacer` objects entirely or reduce their height to 1 or 2 points.
   - Slash table cell paddings (`TOPPADDING`, `BOTTOMPADDING`, `LEFTPADDING`, `RIGHTPADDING`) to 1 or 2.
   - Reduce paragraph `spaceBefore` and `spaceAfter` to 0 or 1.
   - It is significantly harder than it looks to fit dynamic code into a small space, so compress more aggressively than you think is necessary on the first attempt to avoid spilling over into an extra page.

**Example: Side-by-Side Code with Syntax Highlighting**
```python
import re
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def highlight_code(text):
    # 1. Escape HTML first!
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # 2. Tokenize
    tokens = re.split(r'(\W+)', text)
    out = []
    keywords = {'def', 'import', 'from', 'return', 'if', 'else', 'for', 'while'}
    in_comment = False
    
    for t in tokens:
        if '\\n' in t: in_comment = False
        if '#' in t: in_comment = True
        
        escaped_t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        if in_comment or '#' in t:
            out.append(f'<font color="#008000"><i>{escaped_t}</i></font>')
        elif t in keywords:
            out.append(f'<font color="#0000FF"><b>{escaped_t}</b></font>')
        else:
            out.append(escaped_t)
            
    res = ''.join(out).replace('\\n', '<br/>').replace('    ', '&nbsp;&nbsp;&nbsp;&nbsp;')
    return res

doc = SimpleDocTemplate("output.pdf", pagesize=landscape(A4))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Code', fontName='Courier', fontSize=10, leading=13))

story = []

# Create highlighted paragraphs
code1 = highlight_code("def hello():\\n    # Print hello\\n    return 'hello'")
code2 = highlight_code("def world():\\n    # Print world\\n    return 'world'")

p1 = Paragraph(code1, styles['Code'])
p2 = Paragraph(code2, styles['Code'])

# Side-by-side Table
table = Table([[p1, p2]], colWidths=[400, 400])
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#1e2227")),
    ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('GRID', (0,0), (-1,-1), 1, colors.grey)
]))

story.append(table)
story.append(PageBreak()) # Prevents overlapping with subsequent content

doc.build(story)
```

## Command-Line Tools

### pdftotext (poppler-utils)

**CRITICAL FOR LLM AGENTS (Context Window Limit):** Extracting text from a large PDF will create a massive `output.txt` file. NEVER read the entire file using `view_file` as it will exceed your context limit. Instead, either:
1. Extract only specific pages using `-f` (first) and `-l` (last) flags.
2. ALWAYS use `grep_search` on the resulting `output.txt` to find specific information.

```bash
# Extract text
pdftotext input.pdf output.txt

# Extract text preserving layout
pdftotext -layout input.pdf output.txt

# Extract specific pages
pdftotext -f 1 -l 5 input.pdf output.txt  # Pages 1-5
```

### qpdf
```bash
# Merge PDFs
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf

# Split pages
qpdf input.pdf --pages . 1-5 -- pages1-5.pdf
qpdf input.pdf --pages . 6-10 -- pages6-10.pdf

# Rotate pages
qpdf input.pdf output.pdf --rotate=+90:1  # Rotate page 1 by 90 degrees

# Remove password
qpdf --password=mypassword --decrypt encrypted.pdf decrypted.pdf
```

### pdftk (if available)
```bash
# Merge
pdftk file1.pdf file2.pdf cat output merged.pdf

# Split
pdftk input.pdf burst

# Rotate
pdftk input.pdf rotate 1east output rotated.pdf
```

## Common Tasks

### Extract Text from Scanned PDFs
```python
# Requires: pip install pytesseract pdf2image
import pytesseract
from pdf2image import convert_from_path

# Convert PDF to images
images = convert_from_path('scanned.pdf')

# OCR each page
text = ""
for i, image in enumerate(images):
    text += f"Page {i+1}:\n"
    text += pytesseract.image_to_string(image)
    text += "\n\n"

print(text)
```

### Add Watermark
```python
from pypdf import PdfReader, PdfWriter

# Create watermark (or load existing)
watermark = PdfReader("watermark.pdf").pages[0]

# Apply to all pages
reader = PdfReader("document.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)

with open("watermarked.pdf", "wb") as output:
    writer.write(output)
```

### Extract Images
```bash
# Using pdfimages (poppler-utils)
pdfimages -j input.pdf output_prefix

# This extracts all images as output_prefix-000.jpg, output_prefix-001.jpg, etc.
```

### Password Protection
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# Add password
writer.encrypt("userpassword", "ownerpassword")

with open("encrypted.pdf", "wb") as output:
    writer.write(output)
```

## Quick Reference

| Task | Best Tool | Command/Code |
|------|-----------|--------------|
| Merge PDFs | pypdf | `writer.add_page(page)` |
| Split PDFs | pypdf | One page per file |
| Extract text | pdfplumber | `page.extract_text()` |
| Extract tables | pdfplumber | `page.extract_tables()` |
| Create PDFs | reportlab | Canvas or Platypus |
| Command line merge | qpdf | `qpdf --empty --pages ...` |
| OCR scanned PDFs | pytesseract | Convert to image first |
| Fill PDF forms | pdf-lib or pypdf (see FORMS.md) | See FORMS.md |

## Next Steps

- For advanced pypdfium2 usage, see REFERENCE.md
- For JavaScript libraries (pdf-lib), see REFERENCE.md
- For generating PDFs from HTML containing LaTeX/MathJax, see **HTML_TO_PDF.md**
- If you need to fill out a PDF form, follow the instructions in FORMS.md
- For troubleshooting guides, see REFERENCE.md
