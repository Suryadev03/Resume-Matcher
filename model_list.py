# from dotenv import load_dotenv
# import os   
# import google.generativeai as genai

# load_dotenv()

# api_key = os.getenv('GOOGLE-GEMINI-API-KEY')
# if not api_key:
#     raise ValueError("API key for Google Gemini not found in environment variables.")

# genai.configure(api_key=api_key)
# print("Google Gemini API configured successfully.")
 
# for model in genai.list_models():
#     if 'generatecontent' in model.supported_generation_methods:
#         print("Available model:", model.name)

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE-GEMINI-API-KEY")
if not api_key:
    raise ValueError("GOOGLE_GEMINI_API not found")

genai.configure(api_key= api_key)

print("Available Gemini Models")

for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(f"  - {model.name}")