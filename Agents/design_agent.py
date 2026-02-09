from crewai import Agent
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # set in .env

# agents/design_agent.py
# design_agent.py

def design_agent_execute(requirements):
    title = requirements.get("page_type", "Landing Page")

    design_spec = {
        "title": title,
        "brand_vibe": requirements.get("vibe", "modern"),
        "color_preferences": requirements.get("colors", []),
        "font_preference": "Inter, sans-serif",
    }

    image_prompt = f"""
Create a high-fidelity landing page UI for:
{title}

Style:
- {design_spec["brand_vibe"]}
- Use the requested color palette if provided
- Clean, modern, professional

The layout should feel realistic and production-ready.
"""

    return {
        "image_prompt": image_prompt,
        "design_spec": design_spec
    }
