# agents/qa_agent.py
import os
from bs4 import BeautifulSoup

def qa_agent(html_path, css_path, mockup_path):
    issues = []

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    if "<link" not in html or "style.css" not in html:
        issues.append("HTML does not link CSS file")

    if len(css.strip()) < 50:
        issues.append("CSS file appears empty or too small")

    if "<section" not in html:
        issues.append("No semantic sections detected")

    if issues:
        return "[QA Issues Found]:\n- " + "\n- ".join(issues)

    return None
