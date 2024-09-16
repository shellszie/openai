from flask import Flask
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

@app.route('/')
def generate_text():
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Generate a medium multiple-choice question about mathematics. Provide 4 options labeled A, B, C, " +
                "D. Clearly mark the correct answer. Format as: Question, A) option, B) option, C) option, D) option",
        max_tokens=50
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

if __name__ == '__main__':
    app.run(host='0.0.0.0')
