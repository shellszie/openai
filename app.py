from flask import Flask, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route('/')
def generate_text():
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Generate a medium multiple-choice question about mathematics. Provide 4 options labeled A, B, C, D. ",
               # "Format as: >>QuestionA>>optionB>>optionC>>optionD>>option",
        max_tokens=50
    )
    generated_text = response.choices[0].text.strip()
    formatted_text = format_response(generated_text)
    return render_template('home.html', response=formatted_text)
    # return generated_text

#takes text input and returns json of question and each multiple choice answer
#{
# Question: What is the minimum number of digits needed to represent the value of the product, 9 x 9 x 9?
# A: 3,
# B: 4,
# C: 27,
# D: 81
# }
def format_response(raw_input):
    print("raw = ", raw_input)
    tokens = raw_input.split("\n")
    print("tokens = ", tokens)
    return tokens


if __name__ == '__main__':
    app.run(debug=True)