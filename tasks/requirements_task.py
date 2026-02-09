from crewai import Task

requirements_task = Task(
    description="""
Extract structured requirements from the user's description.
Return:
- page title
- sections
- color style
- tone
""",
    expected_output="Structured requirements as plain text"
)
