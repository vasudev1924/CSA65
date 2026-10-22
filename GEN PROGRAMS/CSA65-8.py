from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

prompt = input("Enter prompt: ")

response = client.chat_completion(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=100
)

print(response.choices[0].message.content)
