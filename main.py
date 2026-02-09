from agents.requirements_agent import requirements_agent
from agents.design_agent import design_agent_execute
from agents.qa_agent import qa_agent

from tools.image_tool import generate_ui_mockup
from tools.file_writer import write_code_files

from llm import gemini_llm


def main():
   
    user_input = input(
        "Describe your landing page (e.g., Coffee shop with cats, brown colors): "
    )

   
    requirements = requirements_agent(user_input)

  
    design_output = design_agent_execute(requirements)
    image_prompt = design_output["image_prompt"]
    design_spec = design_output["design_spec"]

   

    print("\n🎨 Generating mockup image with Gemini...")
    mockup_path = generate_ui_mockup.run(image_prompt)
    print(f"[Mockup Image Saved] -> {mockup_path}")

   
    llm_prompt = f"""
You are an expert frontend engineer.

You are given:
- A landing page mockup image at: {mockup_path}
- A design specification: {design_spec}

TASK:
1. Visually analyze the mockup image
2. Infer layout, spacing, typography, colors, and hierarchy
3. Generate FULL HTML and FULL CSS
4. Styling MUST be in CSS (no inline styles)
5. HTML must link the CSS file using <link>

STRICT OUTPUT FORMAT (DO NOT DEVIATE):

===HTML===
<complete valid HTML here>

===CSS===
<complete valid CSS here>

RULES:
- Do NOT omit CSS
- Do NOT return explanations
- Do NOT use placeholders like "Content goes here"
"""

    print("\n💻 Generating HTML/CSS with Gemini 2.5 Flash...")
    llm_output = gemini_llm.call(llm_prompt)

    if "===HTML===" not in llm_output or "===CSS===" not in llm_output:
        raise ValueError("❌ Gemini did not return both HTML and CSS")

    html_code = llm_output.split("===HTML===")[1].split("===CSS===")[0].strip()
    css_code = llm_output.split("===CSS===")[1].strip()

  
    html_path, css_path = write_code_files(html_code, css_code)

   
    print("\n🔍 Running QA Agent...")
    qa_feedback = qa_agent(html_path, css_path, mockup_path)
    print("\n✅ QA Feedback:\n", qa_feedback or "No issues found")

    print("\n🎉 Pipeline complete!")


if __name__ == "__main__":
    main()
