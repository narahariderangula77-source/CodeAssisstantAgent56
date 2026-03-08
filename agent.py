import os
from dotenv import load_dotenv
import google.generativeai as genai

from tools import CodeTools
from validator import Validator

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use working model
model = genai.GenerativeModel("gemini-2.5-flash")


class CodeAssistantAgent:

    def __init__(self):
        self.tools = CodeTools()
        self.validator = Validator()

    # Call Gemini
    def ask_llm(self, prompt):

        try:
            response = model.generate_content(prompt)
            return response.text

        except Exception as e:
            return f"Backend Error: {str(e)}"

    # Main processing
    def process(self, user_prompt, code):

        # Step 1: Syntax validation
        syntax_ok, msg = self.validator.syntax_check(code)

        if not syntax_ok:

            fix_prompt = f"""
You are an expert Python debugging assistant.

The following code has a syntax error.

Code:
{code}

Python error:
{msg}

Explain the error and give corrected code.
"""

            return self.ask_llm(fix_prompt)

        # Step 2: Code analysis
        analysis = self.tools.analyze_code(code)

        prompt = f"""
User request:
{user_prompt}

Code:
{code}

Tool analysis:
{analysis}

Analyze the code and suggest improvements.
"""

        return self.ask_llm(prompt)