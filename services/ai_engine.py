import openai
from config.config import OPENAI_API_KEY

client = openai.OpenAI(api_key="OPENAI_API_KEY")

def generate_response(prompt, persona):
    full_prompt = f"{persona}\n\n{prompt}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
