import os

def coding_agent(design_spec, mockup_path):
    """
    Generate HTML and CSS that matches the Gemini mockup design.
    design_spec: {
        'title': str,
        'sections': [str],
        'colors': [str],
        'font': str
    }
    mockup_path: path to Gemini-generated mockup image
    """
    html_sections = ""
    css_sections = ""

    for i, section in enumerate(design_spec["sections"]):
        section_type = section["type"]
        headline = section.get("headline", section_type.title())
        color = design_spec["colors"].get(section_type, "#F0F0F0")

    html_sections += f"""
<section id="{section_type}">
    <div class="container">
        <h2>{headline}</h2>
        <p>Content for {section_type} goes here...</p>
    </div>
</section>
"""

    css_sections += f"""
#{section_type} {{
    background-color: {color};
    text-align: center;
    padding: 80px 20px;
    font-family: {design_spec['font']};
}}
#{section_type} .container {{
    max-width: 1000px;
    margin: 0 auto;
}}
#{section_type} h2 {{
    font-size: 3rem;
    margin-bottom: 20px;
    color: #333;
}}
#{section_type} p {{
    font-size: 1.2rem;
    color: #555;
}}
"""


    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{design_spec['title']}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

{html_sections}

<!-- Mockup Image from Gemini -->
<div style="text-align:center; margin: 50px 0;">
    <img src="{os.path.basename(mockup_path)}" alt="Design Mockup" style="width:80%; border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
</div>

</body>
</html>
"""

    css = f"""
body {{
    margin: 0;
    padding: 0;
}}
{css_sections}
"""

    return html, css
