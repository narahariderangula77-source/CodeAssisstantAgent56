import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Print available models
for m in genai.list_models():
    print(m.name)