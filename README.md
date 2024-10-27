# Simplifier

Simplifier is a web application that simplifies domain-specific text based on an individual's expertise and education level. It uses web scraping and AI-powered text analysis to provide simplified versions and summaries of complex content.

## Features

- Web scraping to extract text from URLs
- Text simplification based on user's expertise and education level
- Bullet-point summary generation
- RESTful API for easy integration
- User-friendly React-based web interface

## Tech Stack

- Backend: Python, Flask
- Frontend: React, JavaScript, HTML, CSS
- AI: OpenAI GPT-4

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11 or higher
- pip (Python package manager)
- Node.js and npm (for React frontend)
- An OpenAI API key
- A modern web browser

## Project Structure

The project is organized into two main directories:

```
simplifier/
├── backend/
│   ├── backend.py
│   ├── requirements.txt
│   └── settings.yaml
└── frontend/
    ├── public/
    ├── src/
    ├── package.json
    └── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simplifier.git
   cd simplifier
   ```

2. Set up the backend:
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   Create a `settings.yaml` file in the `backend` directory and add your API key:
   ```yaml
   OpenAPI_KEY: 'your_api_key_here'
   ```

4. Set up the frontend:
   ```
   cd ../frontend
   npm install
   ```

## Usage

1. Start the backend server:
   ```
   cd backend
   source venv/bin/activate  # If not already activated
   python backend.py
   ```

2. In a new terminal, start the frontend development server:
   ```
   cd frontend
   npm start
   ```

3. Open your web browser and navigate to `http://localhost:3000`

4. Use the web interface to:
   - Enter a URL or paste text directly
   - Select your expertise level and education level
   - Click "Simplify" to get a simplified version and summary of the content

## API Reference

The backend provides a RESTful API for integration with other services.

### POST /analyze_url

Simplifies and summarizes text from a given URL.

Request body:
- `url` (string, required): The URL to scrape and analyze
- `expertise` (string, required): User's expertise level (e.g., "beginner", "intermediate", "expert")
- `education_level` (string, required): User's education level (e.g., "high school", "undergraduate", "graduate")

Response:
- `text` (string): Simplified version of the original text
- `summary` (string): Bullet-point summary of key points

### POST /analyze_text

Simplifies and summarizes provided text.

Request body:
- `text` (string, required): The text to analyze
- `expertise` (string, required): User's expertise level
- `education_level` (string, required): User's education level

Response:
- `text` (string): Simplified version of the original text
- `summary` (string): Bullet-point summary of key points

## Frontend Structure

The React-based frontend is located in the `frontend` directory. Key files and directories include:

- `src/`: Contains the React components and main application logic
- `public/`: Contains the public assets and `index.html`
- `package.json`: Defines the project dependencies and scripts

The interface allows users to input either a URL or direct text, select their expertise and education levels, and receive simplified text and a summary.

## Contributing

Contributions to the Simplifier project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/simplifier](https://github.com/yourusername/simplifier)
