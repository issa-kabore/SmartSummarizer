# 🧠 Multilingual Text Summarizer with Transformers

This project is a web-based application that summarizes English or French text using LLMs. It supports direct input, `.txt`, and `.pdf` files with automatic language detection.

The project uses **Large Language Models (LLMs)** such as **BART** or **T5**, deployed via a simple, interactive **Gradio** interface.


## 📌 Objectives

- Automate the **synthesis of long texts** (e-mails, reports, news...)
- Apply **automatic summarization techniques with LLMs**.
- Propose a **simple and responsive user interface**.
- Demonstrate a **real-life case of NLP model industrialization**.


## 🧠 Technical stack

- [Transformers](https://huggingface.co/docs/transformers/index) - Pre-trained models (BART, T5...)
- [Streamlit](https://streamlit.io) - Web interface
- [Gradio](https://www.gradio.app/) - Web interface
- [Python](https://www.python.org) - Processing & pipeline
- (Bonus) Docker, FastAPI, GitHub Actions - MLOps


## ✨ Features
- Automatic language detection (English or French)
- Summarization using state-of-the-art models
- Gradio-based web interface
- Supports text, .txt and .pdf inputs

## 🚀 Run the App

```bash
git clone https://github.com/issa-kabore/SmartSummarizer.git
cd SmartSummarizer
pip install -r requirements.txt
python app_gradio.py
```


## 🚀 Demo
👉 [Link to deployed app](https://...)
📸 See screenshots below


## 📂 Project structure 
```bash
SmartSummarizer/
│
├── app_gradio.py                # Gradio main script (user interface)
├── summarizer/
│   ├── __init__.py             
│   ├── models.py                # Loading models and pipelines
│   ├── utils.py                # Import functions .txt/.pdf and Language detection
│   └── summarize.py             # Main summary function
│
├── assets/                      # (Optional) static files: images, logos, etc.
│
├── requirements.txt             # Dependencies to install
├── README.md                    # Project presentation
└── .gitignore                   # Files to be ignored by Git

```
