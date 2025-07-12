import streamlit as st
from transcriber import transcribe_audio
from summarizer import generate_summary
import os

st.set_page_config(page_title="AI Voice Notes Transcriber", page_icon="🎙️", layout="wide")

st.title("🎙️ AI Voice Notes Transcriber")

st.write("Upload your audio file below:")

audio_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a", "aac", "ogg"])

# Load secrets from .streamlit/secrets.toml
speech_key = st.secrets["SPEECH_KEY"]
service_region = st.secrets["SPEECH_REGION"]

if audio_file is not None:
    st.audio(audio_file)
    st.success("Audio uploaded successfully!")

    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing..."):
            transcript = transcribe_audio(audio_file, speech_key, service_region)
            st.subheader("📝 Transcript")
            st.write(transcript)

            if transcript:
                openai_key = st.secrets["OPENAI_API_KEY"]

                if st.button("Generate Summary"):
                    with st.spinner("Summarizing..."):
                        summary = generate_summary(transcript, openai_key)
                        st.subheader("📄 Meeting Summary")
                        st.write(summary)
