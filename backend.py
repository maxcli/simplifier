#!/usr/bin/python3 
#shebang . interpreter directive

#pip install pyyaml

import yaml
from pathlib import Path
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
from openai import OpenAI


def get_settings():
    full_file_path = Path(__file__).parent.joinpath('settings.yaml')
    with open(full_file_path) as settings:
        settings_data = yaml.load(settings, Loader=yaml.Loader)
    return settings_data

try:
    settingsDict = get_settings()
    OPENAI_API_KEY = settingsDict["OpenAPI_KEY"]
    print("OpenAI API key loaded")
except Exception as error:
    print("An exception occurred", error)
    OPENAI_API_KEY = "your-api-key-goes-here"

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=OPENAI_API_KEY)


@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    data = request.json
    sample_text = data.get('sample_text', '')
    expertise = data.get('expertise', '')
    education_level = data.get('education_level', '')

    rewrite_prompt = f"""
        Rewrite the following text, adjusting the complexity and terminology based on the user's expertise ({expertise}) and education level ({education_level}).

        Text: {sample_text}
    """

    summary_prompt = f"""
        Provide a 3-bullet point short summary at most 30 wordsof the key points from the following text, adjusting the complexity and terminology based on the user's expertise ({expertise}) and education level ({education_level}).
        Sample: 
        - bullet point 1 \n
        - bullet point 2 \n
        - bullet point 3 \n
        Text: {sample_text}
    """
    
    try:
        # First API call for rewritten text
        rewrite_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": rewrite_prompt}],
            max_tokens=8192,
            n=1,
            temperature=0.5,
        )
        rewritten_text = rewrite_response.choices[0].message.content.strip()

        # Second API call for bullet point summary
        summary_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": summary_prompt}],
            max_tokens=8192,
            n=1,
            temperature=0.5,
        )
        summary = summary_response.choices[0].message.content.strip()

        return jsonify({
            'text': rewritten_text,
            'summary': summary
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
   
        


if __name__ == '__main__':
    app.run(debug=True) # default http://localhost:5000
