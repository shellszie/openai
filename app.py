from doctest import debug

from flask import Flask, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route('/landing', methods=['GET'])
def landing():
    return render_template('landing.html')

@app.route('/question', methods=['GET', 'POST'])
def generate_text():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an expert educator who creates multiple-choice questions."},
        {"role": "user",
         "content": f"Generate a medium multiple-choice question about mathematics. Provide 4 options labeled A) B) C) D)"}
        ]
        # prompt="Generate a medium multiple-choice question about mathematics. Provide 4 options labeled A) B) C) D) ",
        #        "Format as: >>QuestionA>>optionB>>optionC>>optionD>>option",
        # max_tokens=50
    )
    # generated_text = response.choices[0].text.strip()
    # breakpoint()
    generated_text = response.choices[0].message.content.strip()
    formatted_text = format_response(generated_text)
    return render_template('question.html', response=formatted_text)
    # return generated_text

def format_response(raw_input):
    print("raw = ", raw_input)
    tokens = raw_input.split("\n")
    tokens_no_nil = remove_empty(tokens)
    print("tokens = ", tokens)
    return tokens_no_nil

def remove_empty(input):
    ret_arr = []
    for x in input:
        if x == "":
            continue
        else:
            ret_arr.append(x)

    return ret_arr

if __name__ == '__app__':
    app.run(debug=True)