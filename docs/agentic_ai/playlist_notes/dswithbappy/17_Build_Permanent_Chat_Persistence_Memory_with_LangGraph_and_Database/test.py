import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

print("API Key:", os.getenv("GOOGLE_API_KEY"))  # Debug

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="My name is Uday. I am a software engineer. I love to code in Python and JavaScript. I also enjoy working with AI and machine learning models. I am currently exploring the capabilities of the Gemini LLM.",
)

print(response.text)