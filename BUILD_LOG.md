# Build Log

This document captures my complete journey building the Tiny AI QnA app including errors, searches, and decisions.

## Step 1 Tried OpenAI API
- Installed openai package and wrote minimal CLI  
- Error received  

You have 0 dollars remaining credits

- Googled how to check OpenAI usage and found the usage dashboard  
- Confirmed my free trial expired and I had no credits left  
- Pivoted away from OpenAI because billing would block the project

## Step 2 Explored Hugging Face
- Tried Hugging Face pipelines like facebook bart large cnn and deepset roberta base squad2  
- Faced problems downloading large models on my 8GB RAM Mac  
- Errors related to context length and slow downloads  
- Googled huggingface free inference API without GPU and found inference endpoints are paid  
- Decided Hugging Face was not sustainable for a quick demo

## Step 3 Moved to Groq
- Googled free OpenAI compatible API and found Groq’s Llama models  
- First attempt gave error  

 model llama3-8b-8192 has been decommissioned

- Searched Groq llama3 deprecation and found official docs  
- Fixed by switching to llama 3.1 8b instant and llama 3.3 70b versatile  

## Step 4 Built CLI
- Added rich for colored CLI output  
- Added interactive mode and argparse flags for model and temperature  
- Googled python argparse multiple flags to learn syntax  

## Step 5 Added Streamlit UI
- Built a simple chat layout with sidebar settings  
- First deployment attempt failed with KeyError GROQ_API_KEY  
- Googled huggingface spaces streamlit secret key and solved by adding key as a secret in HF Spaces  

## Key Takeaways
- Always expect APIs to change and adapt quickly  
- Environment key management is critical never push secrets  
- Documenting problems and pivots is as important as the final working code  

