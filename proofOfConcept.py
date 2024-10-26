from openai import OpenAI
import scraper


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

# Set up OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)
def analyze_text(sample_text, expertise, education_level):
    prompt = f"""
        Rewrite the following text, adjusting the complexity and terminology, and use analogy based on the user's expertise ({expertise}) and education level ({education_level}):\n\n{sample_text}\n\nText:
    """
    # Use OpenAI API to analyze the text
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=8192,
            n=1,
            temperature=0.5,
        )

        # Extract the generated summary
        summary = response.choices[0].message.content.strip()
        return {'summary': summary}
    except Exception as e:
        return {'error': str(e)}

# Example usage
if __name__ == "__main__":
    
   # with open('sample_text/neural_science_review.txt', 'r') as file:
    #    sample_text = file.read().strip()
     
    sample_text = scraper.scrape_website('https://en.wikipedia.org/wiki/Neurosteroid')
        
    expertise = "Arts and Humanities"
    education_level = "high school"
    
    result = analyze_text(sample_text, expertise, education_level)
    if 'summary' in result:
        print("Generated Summary:")
        print(result['summary'])
    else:
        print("Error:", result['error'])
