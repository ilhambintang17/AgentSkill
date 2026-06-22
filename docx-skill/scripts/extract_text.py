#!/usr/bin/env python3
import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def extract_text(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as docx:
            if 'word/document.xml' not in docx.namelist():
                return f"Error: {docx_path} is not a valid DOCX file."
            
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            ns = {
                'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
                'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
                'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
                'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
            }
            
            body = tree.find('.//w:body', ns)
            if body is None:
                return "Error: Could not find document body."

            def extract_paragraph(p_elem):
                para_text = []
                for child in p_elem.iter():
                    if child.tag == f"{{{ns['w']}}}t" and child.text:
                        para_text.append(child.text)
                    elif child.tag == f"{{{ns['w']}}}drawing":
                        docPr = child.find('.//wp:docPr', ns)
                        name = "IMAGE"
                        if docPr is not None and docPr.attrib.get('name'):
                            name = f"IMAGE: {docPr.attrib.get('name')}"
                        para_text.append(f" [{name}] ")
                return ''.join(para_text)

            output = []
            
            for elem in body:
                if elem.tag == f"{{{ns['w']}}}p":
                    text = extract_paragraph(elem)
                    if text.strip() or "[IMAGE" in text:
                        output.append(text)
                elif elem.tag == f"{{{ns['w']}}}tbl":
                    output.append("\n[TABLE START]")
                    for row in elem.findall('.//w:tr', ns):
                        row_data = []
                        for cell in row.findall('.//w:tc', ns):
                            cell_text = []
                            for p in cell.findall('.//w:p', ns):
                                cell_text.append(extract_paragraph(p).strip())
                            row_data.append(" ".join(cell_text))
                        output.append(" | ".join(row_data))
                    output.append("[TABLE END]\n")

            return '\n'.join(output)
    except Exception as e:
        return f"Error extracting text from {docx_path}: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_text.py <path_to_docx>")
        sys.exit(1)
    
    docx_path = sys.argv[1]
    if not os.path.exists(docx_path):
        print(f"File not found: {docx_path}")
        sys.exit(1)
        
    print(extract_text(docx_path))
