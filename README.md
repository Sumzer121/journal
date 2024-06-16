# Journal App

## Project Overview
This project is designed to allow users to input their daily journal entries. The LLAMA AI Model analyzes these entries to provide constructive and helpful feedback, aimed at improving the user's mental state.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Sumzer121/journal.git
   cd journal
   ```

2. Install dependencies using Pipenv:
   ```
   pipenv install
   ```

## Setup
1. Create a `.env` file in the root directory of your project with the following content:
   ```
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ```

2. Apply database migrations:
   ```
   python manage.py migrate
   ```

## Usage
1. Run the development server:
   ```
   python manage.py runserver
   ```

2. Access the application at `http://127.0.0.1:8000/` in your web browser.

## Dependencies
- Django: Framework for building web applications in Python.
- TextBlob: Library for processing textual data.
- OpenAI: API for AI models.
- Transformers: Library for Natural Language Processing (NLP) tasks.
- TensorFlow: Framework for machine learning.
- Torch: Machine learning library.
- Accelerate: PyTorch extension library.
- wget: Command-line utility for downloading files.
- OLLAMA: AI Model for analyzing text and providing feedback.
