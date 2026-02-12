# 🤖 AI TransSummarizer

A professional **Full-Stack AI Application** designed to streamline content consumption. This tool leverages state-of-the-art Large Language Models (LLMs) to provide two core services: **Smart Text Summarization** and **High-Accuracy English-to-Arabic Translation**.

## 🚀 Live Demo
Experience the application live here: [AI-TransSummarizer on Hugging Face](https://philopateerdev-ai-transsummarizer.hf.space)

## ✨ Key Features
* **Smart Summarization**: Uses the `facebook/bart-large-cnn` model to condense long articles into short, informative summaries.
* **Neural Translation**: Translates English content into fluent Arabic using the `Helsinki-NLP` translation engine.
* **Dual-Mode Processing**: Users can summarize and translate simultaneously in a single click.
* **Responsive Dark UI**: A modern, user-friendly interface with a sleek violet theme, optimized for both desktop and mobile.
* **Robust Backend**: Powered by FastAPI for high-speed request handling and Pydantic for data validation.

## 🛠️ Technical Stack
* **Backend**: Python 3.9, FastAPI.
* **AI Framework**: Hugging Face Transformers.
* **Frontend**: HTML5, CSS3 (Modern UI), JavaScript (Asynchronous Fetch API).
* **Infrastructure**: Dockerized environment deployed on Hugging Face Spaces.

## ⚙️ How It Works
The system follows a modular logic flow:
1. **Input**: User pastes English text and selects desired tasks.
2. **Preprocessing**: JavaScript appends hidden triggers (`summarize` / `ترجم`) based on user selection.
3. **AI Pipeline**: 
    - If "Summarize" is triggered, the `BART` model reduces the text length while preserving meaning.
    - If "Translate" is triggered, the `OPUS-MT` model converts the resulting text into Arabic.
4. **Output**: The processed result is displayed instantly without page reloads.

## 📦 Local Setup
To run this project locally:

1. **Clone the repo**:
   ```bash
   git clone [https://github.com/PhilopateerDev/AI-TransSummarizer.git](https://github.com/PhilopateerDev/AI-TransSummarizer.git)
