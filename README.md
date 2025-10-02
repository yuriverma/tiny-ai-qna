# Tiny AI QnA

A tiny AI powered app built as part of my internship assignment.  
The app answers any question from the command line or via a simple Streamlit UI using Groq’s free LLM API.

## Features
1. Command line QnA using qna.py  
2. Interactive chat like UI built with Streamlit using app.py  
3. Multiple model support with model flag in CLI and dropdown in UI  
4. Adjustable creativity with temp flag in CLI and slider in UI  
5. Clear error handling if API key is missing  
6. Documented build log with pivots and failed attempts  

## Setup and Run

1. Clone the repository  
git clone https://github.com/yuriverma/tiny-ai-qna.git
cd tiny-ai-qna


2. Create environment  
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Add your Groq API key to .env  
GROQ_API_KEY=gsk_your_real_key_here

4. Run CLI  
python qna.py "Explain transformers like I am 12"

5. Run Streamlit UI 
streamlit run app.py


## Build Log
The detailed build log is documented in [BUILD_LOG.md](BUILD_LOG.md).  
It contains every error, what I tried, what failed, what I Googled and how I adapted.

## Learnings
## Free APIs often deprecate models so always check official docs  
## Never push real environment keys I mistakenly pushed it once and learned to rotate keys immediately  
## Streamlit is perfect for quick UI without HTML or JavaScript  
## Documenting even failures shows the process matters as much as the result  

## Next Steps
## Save QnA history to a markdown file with timestamps  
## Add token usage and latency stats  
## Deploy on Render with a Flask backend and simple web frontend  
## Try smaller Hugging Face models for an offline fallback  

## Screenshots
Add screenshots of CLI and Streamlit UI here

## Live Demo
Add Hugging Face Space link here once deployed
