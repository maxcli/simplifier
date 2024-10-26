# Simplifier

Simplifier is a web application that simplifies domain-specific text based on an individual's expertise and education level. It uses web scraping and AI-powered text analysis to provide simplified versions and summaries of complex content.

## Features

- Web scraping to extract text from URLs
- Text simplification based on user's expertise and education level
- Bullet-point summary generation
- RESTful API for easy integration

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- pip (Python package manager)
- An OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simplifier.git
   cd simplifier
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   Create a `.env` file in the project root and add your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Start the Flask server:
   ```
   python backend.py
   ```

2. The API will be available at `http://localhost:5000`. You can now make POST requests to the following endpoints:

   - `/analyze_url`: Simplify and summarize text from a given URL
   - `/analyze_text`: Simplify and summarize provided text

   Example request body:
   ```json
   {
     "url": "https://example.com/article",
     "expertise": "beginner",
     "education_level": "high school"
     "language": "english"
   }
   ```

## API Reference

### POST /analyze_url

Simplifies and summarizes text from a given URL.

Request body:
- `url` (string, required): The URL to scrape and analyze
- `language` (string, optional): The language of the text
- `expertise` (string, required): User's expertise level (e.g., "beginner", "intermediate", "expert")
- `education_level` (string, required): User's education level (e.g., "high school", "undergraduate", "graduate")

Response:
- `text` (string): Simplified version of the original text
- `summary` (string): Bullet-point summary of key points

### POST /analyze_text

Simplifies and summarizes provided text.

Request body:
- `text` (string, required): The text to analyze
- `language` (string, optional): The language of the text 
- `education_level` (string, required): User's education level (e.g., "high school", "undergraduate", "graduate")
- `expertise` (string, required): User's expertise level
