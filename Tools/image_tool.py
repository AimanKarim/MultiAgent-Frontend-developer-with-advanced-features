from crewai.tools import tool
import os
from google import genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@tool("Generate UI Mockup")
def generate_ui_mockup(prompt: str) -> str:
    """
    Generate a UI mockup image using Gemini Imagen.

    Args:
        prompt (str): Detailed prompt describing the page design.

    Returns:
        str: Path to the saved image.
    """
    os.makedirs("outputs/designs", exist_ok=True)

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_images(
        model="imagen-4.0-generate-001",
        prompt=prompt
    )

    image_bytes = response.images[0].image_bytes
    path = "outputs/designs/mockup.png"
    with open(path, "wb") as f:
        f.write(image_bytes)

    return path
