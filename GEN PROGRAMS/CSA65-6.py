from openai import OpenAI

client = OpenAI()

prompt = input("Enter prompt: ")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)
