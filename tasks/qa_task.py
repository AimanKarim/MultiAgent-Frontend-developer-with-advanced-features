from crewai import Task

qa_task = Task(
    description="Review the generated HTML, CSS, and image consistency",
    expected_output="QA feedback and validation"
)
