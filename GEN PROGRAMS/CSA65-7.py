from google import genai
import os

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

prompt = input("Enter prompt: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
