from os.path import join, exists
from typing import Optional


class FrontendLoader:
  def __init__(self, html_path: str, script_base: str, style_base: str):
    self.script_base = script_base
    self.style_base = style_base

    if not exists(html_path):
      raise FileNotFoundError(f"HTML file '{html_path}' could not be found. Try review your configuration.")

    with open(html_path, encoding='utf-8') as f:
      self.html_content = f.read()

  def get_html(self) -> str:
    return self.html_content

  def get_script(self, path: str) -> Optional[str]:
    file = join(self.script_base, path)

    if not exists(file):
      return None

    with open(file, encoding='utf-8') as f:
      return f.read()

  def get_style(self, path: str) -> Optional[str]:
    file = join(self.style_base, path)

    if not exists(file):
      return None

    with open(file, encoding='utf-8') as f:
      return f.read()
