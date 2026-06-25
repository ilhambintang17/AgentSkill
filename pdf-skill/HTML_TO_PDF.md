# Generating PDF from HTML with MathJax / LaTeX

When generating a PDF from an HTML file that contains complex LaTeX (rendered via MathJax), you will encounter severe issues if you attempt to use basic tools like `weasyprint`, `reportlab`, or simple headless chrome `file://` execution.

Common Errors:
- Blank PDFs or 0 byte PDFs due to headless chrome crashing or timing out.
- MathJax hanging indefinitely due to `file://` protocol CORS restrictions.
- `setContent()` in Puppeteer timing out because external CDN scripts block the `load` or `domcontentloaded` events.
- Malware/hanging domains (e.g., `polyfill.io`) preventing page load.

## The Bulletproof Workflow

To guarantee a successful, fully-rendered PDF with MathJax, follow this exact workflow:

### 1. Prepare the HTML (MathJax Config)

Ensure your HTML includes a startup hook that signals when MathJax is finished rendering. Remove any `polyfill.io` scripts as they are deprecated and known to hang.

```html
<!-- Include MathJax -->
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']]
  },
  startup: {
    pageReady: () => {
      return MathJax.startup.defaultPageReady().then(() => {
        // Create a div to signal Puppeteer that MathJax is done
        const div = document.createElement('div');
        div.id = 'mathjax-done';
        document.body.appendChild(div);
      });
    }
  }
};
</script>
```

### 2. The Puppeteer Print Script (`print.js`)

Do NOT use `page.setContent()`. Instead, navigate to a local HTTP server URL.

```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ 
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  console.log("Navigating to local server...");
  // Navigate to local server to avoid file:// CORS issues
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'domcontentloaded' });
  
  console.log("Waiting for MathJax...");
  try {
    // Wait for the exact signal we created in the HTML
    await page.waitForSelector('#mathjax-done', { timeout: 30000 });
    console.log("MathJax finished!");
  } catch (e) {
    console.log("Timeout waiting for MathJax. Generating PDF anyway...");
  }
  
  // Optional small buffer
  await new Promise(r => setTimeout(r, 2000));
  
  await page.pdf({
    path: 'output.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '5mm', right: '5mm', bottom: '5mm', left: '5mm' }
  });

  await browser.close();
  console.log("PDF generated successfully.");
})();
```

### 3. The Execution Script (Bash)

To run this safely, you MUST serve the directory using Python's `http.server` to bypass Chrome's `file://` security policies.

```bash
# Start local server in the background
python3 -m http.server 8080 --directory /path/to/html/folder &
SERVER_PID=$!

# Give the server a few seconds to initialize
sleep 5

# Run the puppeteer script
node print.js

# Kill the server
kill $SERVER_PID
```

### Critical CSS Tips for PDF Generation

If your PDF produces blank pages in the middle:
- Do NOT use `height: 100vh` or fixed `height: 297mm` on container elements if they might overflow.
- Do NOT use `page-break-after: always` alongside fixed heights, as it will trigger extra blank pages.
- Let content naturally flow to the next page. If using multiple columns, simply apply `column-count: 2;` to a wrapper without restricting its height.
