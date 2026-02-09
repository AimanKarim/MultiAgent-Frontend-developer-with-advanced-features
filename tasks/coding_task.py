from crewai import Task

coding_task = Task(
    description="""
Generate HTML and CSS that EXACTLY match the design spec.

Output format:

HTML:
<full html>

CSS:
<full css>
""",
    expected_output="HTML and CSS source code"
)
