"""Refresh inline CSS after editing assets/fonts.css or assets/styles.css."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parent.parent
for name in ('index.html', '404.html'):
    path = ROOT / name
    text = path.read_text(encoding='utf-8')
    fonts = (ROOT / 'assets/fonts.css').read_text().replace("url('fonts/", "url('/assets/fonts/")
    css = fonts
    if name == 'index.html':
        css += '\n' + (ROOT / 'assets/styles.css').read_text()
    block = '<!-- BEGIN GENERATED STYLES -->\n<style>\n' + css + '\n</style>\n<!-- END GENERATED STYLES -->'
    if '<!-- BEGIN GENERATED STYLES -->' in text:
        text = re.sub(r'<!-- BEGIN GENERATED STYLES -->.*?<!-- END GENERATED STYLES -->', lambda m: block, text, flags=re.S)
    else:
        text = re.sub(r'<link[^>]*href="/?assets/fonts.css[^"\s]*"[^>]*>', lambda m: block, text)
        text = re.sub(r'<link[^>]*href="assets/styles.css"[^>]*>\n?', '', text)
    path.write_text(text, encoding='utf-8')
