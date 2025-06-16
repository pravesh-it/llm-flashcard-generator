# 🧠 LLM Flashcard Generator
A Python-based tool that uses a Large Language Model (LLM) like OpenAI's GPT to generate study flashcards from any given text. Perfect for students, educators, or lifelong learners.

## ✨ Features
- Generate question-answer flashcards from long-form text
- Uses OpenAI's API to extract key concepts
- Supports chunked processing for large documents
- Easy-to-use command-line interface

## 🚀 Getting Started
### 1. Clone the repository
```bash
git clone https://github.com/pravesh-it/llm-flashcard-generator.git
cd llm-flashcard-generator
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the app
- streamlit run app.py
- python app.py

## 📂 Project Structure
llm-flashcard-generator/<br>
├── app.py                  # Main entry point<br>
├── flashcard_generator.py # Core logic to interact with the LLM<br>
├── utils.py                # Helper functions for chunking and formatting<br>
├── requirements.txt        # Python dependencies<br>
├── to_run_the_app.txt      # Run instructions<br>
└── README.md               # Project documentation

## 🧪 Example
### Input:
Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods...

### Output:
Q: What is the main function of photosynthesis?
A: To synthesize food using sunlight.

Q: What organisms can perform photosynthesis?
A: Green plants and some other organisms.

## 🛠️ Built With
Python 3.7+
OpenAI GPT API

## 📌 Notes
Keep your api_key.txt private.
This is a basic prototype; you can enhance it by adding support for file input, GUI, or saving flashcards to a database or CSV.

## 📄 License
This project is licensed under the MIT License.
