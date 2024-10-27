#!/usr/bin/python3 
#shebang . interpreter directive

#pip install pyyaml arize-phoenix-otel openinference-instrumentation-openai openai

import yaml
from pathlib import Path
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import os

# Arize Phoenix setup
from phoenix.otel import register
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from openinference.instrumentation.openai import OpenAIInstrumentor

def get_settings():
    full_file_path = Path(__file__).parent.joinpath('settings.yaml')
    with open(full_file_path) as settings:
        settings_data = yaml.load(settings, Loader=yaml.Loader)
    return settings_data

try:
    settingsDict = get_settings()
    OPENAI_API_KEY = settingsDict["OpenAPI_KEY"]
    PHOENIX_API_KEY = settingsDict["PHOENIX_CLIENT_HEADERS"].split("=")[1]
    PHOENIX_ENDPOINT = settingsDict["PHOENIX_COLLECTOR_ENDPOINT"]
    
    print("OpenAI API key and Phoenix settings loaded")
    
    # Set environment variables
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
    os.environ['PHOENIX_CLIENT_HEADERS'] = f"api_key={PHOENIX_API_KEY}"
    
except Exception as error:
    print("An exception occurred", error)
    OPENAI_API_KEY = "your-api-key-goes-here"
    PHOENIX_API_KEY = "your-phoenix-api-key-goes-here"
    PHOENIX_ENDPOINT = "https://app.phoenix.arize.com"

# Register the application with cloud Phoenix instance
tracer_provider = register(
    project_name="simplifier",
    endpoint=f"{PHOENIX_ENDPOINT}/v1/traces",
)

# Initialize the OpenAIInstrumentor
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)

app = Flask(__name__)
CORS(app)

# Instrument Flask
FlaskInstrumentor().instrument_app(app)

# Instrument requests library
RequestsInstrumentor().instrument()

client = OpenAI(api_key=OPENAI_API_KEY)


@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    data = request.json
    sample_text = data.get('sample_text', '')
    expertise = data.get('expertise', '')
    education_level = data.get('education_level', '')
    language = data.get('language', 'Spanish')

    # Debug print to ensure language is being received correctly
    print("Language:", language)  # This will display in your terminal/console

    rewrite_prompt = f"""
        Rewrite the following text in {language}. Adjust the complexity and terminology based on the user's expertise ({expertise}) and education level ({education_level}).

        Text: {sample_text}
    """

    summary_prompt = f"""
        Summarize the following text in {language} with three bullet points (each at most 30 words). Each point should be a complete sentence without any leading symbols:
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

    
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text
        text = soup.get_text()
        
        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        
        # Drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
    except requests.RequestException as e:
        print(f"Error scraping website: {e}")
        return ""


def truncate_text(text, max_chars=3000):
    return text[:max_chars]

@app.route('/analyze_url', methods=['POST'])
def analyze_url():
    data = request.json
    url = data.get('url', '')
    expertise = data.get('expertise', '')
    education_level = data.get('education_level', '')

    extracted_text = scrape_website(url)
    
    truncated_text = truncate_text(extracted_text)
    if not extracted_text:
        return jsonify({'error': 'Failed to extract text from the provided URL'}), 400

    rewrite_prompt = f"""
        Rewrite the following text, adjusting the complexity and terminology based on the user's expertise ({expertise}) and education level ({education_level}).

        Text: {truncated_text}
    """

    summary_prompt = f"""
        Provide a 3-bullet point summary of the key points from the following text, adjusting the complexity and terminology based on the user's expertise ({expertise}) and education level ({education_level}).

        Text: {truncated_text}
    """
    
    try:
        # First API call for rewritten text
        rewrite_response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": rewrite_prompt}],
            max_tokens=4096,
            n=1,
            temperature=0.5,
        )
        rewritten_text = rewrite_response.choices[0].message.content.strip()

        # Second API call for bullet point summary
        summary_response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": summary_prompt}],
            max_tokens=4096,
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
