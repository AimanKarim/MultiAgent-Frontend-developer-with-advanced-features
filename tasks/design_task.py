from crewai import Task

design_task = Task(
    description="""
Create a UI design specification AND an image generation prompt.

You must output:
1. IMAGE_PROMPT: a single paragraph prompt for image generation
2. DESIGN_SPEC: detailed layout instructions (sections, spacing, colors, fonts)

Format exactly:

IMAGE_PROMPT:
<text>

DESIGN_SPEC:
<text>
""",
    expected_output="Image prompt + design specification"
)
