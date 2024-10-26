from openai import OpenAI
import scraper


# Set up OpenAI client
client = OpenAI(api_key=settingsDict["OpenAPI_KEY"])
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
