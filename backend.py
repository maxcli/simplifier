#!/usr/bin/python3 
#shebang . interpreter directive

#pip install pyyaml

import yaml
from pathlib import Path
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

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

# Set up OpenAI API key
client = OpenAI(api_key=OPENAI_API_KEY)

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
        response = client.chat.completions.create((
            model="gpt-4o",  # Changed from "gpt-4o" to "gpt-4"
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

if __name__ == '__main__':
    app.run(debug=True)
