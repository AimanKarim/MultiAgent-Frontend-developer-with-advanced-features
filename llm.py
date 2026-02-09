# llm.py
from crewai import LLM
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    model="gemini-2.5-flash",
    provider="google",
    api_key=GEMINI_API_KEY
)
