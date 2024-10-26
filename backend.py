#!/usr/bin/python3 
#shebang . interpreter directive

#pip install pyyaml

import yaml
from pathlib import Path

  
OpenAPI_KEY = "Secret"
 


def get_settings():
    full_file_path = Path(__file__).parent.joinpath('settings.yaml')
    with open(full_file_path) as settings:
        settings_data = yaml.load(settings, Loader=yaml.Loader)
    return settings_data

try:
    settingsDict=get_settings()
    OPENIDKEY_KEY=settingsDict["OpenAPI_KEY"]
    print("open id  key" +OPENIDKEY_KEY)


except Exception as error:
    print("An exception occurred",error)
from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)
CORS(app)

# Set up OpenAI API key
openai.api_key = "your-api-key-goes-here"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    data = request.json
    sample_text = data.get('text', '')
    expertise = data.get('expertise', '')
    education_level = data.get('education_level', '')

    prompt = f"""
        Rewrite the following text, adjusting the complexity and terminology based on the user's expertise ({expertise}) and education level ({education_level}):\n\n{sample_text}\n\nText:
    """
    # Use OpenAI API to analyze the text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=8192,
            n=1,
            temperature=0.5,
        )

        # Extract the generated summary
        summary = response.choices[0].message['content'].strip()
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
