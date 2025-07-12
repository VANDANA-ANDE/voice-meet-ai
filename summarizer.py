import requests
import streamlit as st

API_TOKEN = st.secrets["HUGGINGFACE_API_TOKEN"]
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def generate_summary(transcript):  # underscore for unused param
    if not transcript.strip():
        return "Transcript is empty. Please transcribe audio first."

    payload = {
        "inputs": f"summarize: {transcript}",
        "parameters": {"max_length": 150, "do_sample": False},
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        

        if isinstance(result, list) and "summary_text" in result[0]:
            return result[0]["summary_text"]
        
        else:
            return "Unexpected response format from Hugging Face API."

    except Exception as e:
        return f"Hugging Face API error: {e}"
