# tools/file_writer.py
import os

def write_code_files(html_content: str, css_content: str, output_dir="outputs/code"):
    """
    Saves HTML and CSS content to separate files and returns their paths.

    Args:
        html_content (str): Full HTML content
        css_content (str): Full CSS content
        output_dir (str): Directory to save files

    Returns:
        Tuple[str, str]: (html_path, css_path)
    """
    os.makedirs(output_dir, exist_ok=True)

    html_path = os.path.join(output_dir, "index.html")
    css_path = os.path.join(output_dir, "style.css")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)

    return html_path, css_path
