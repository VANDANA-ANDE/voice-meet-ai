import streamlit as st

st.set_page_config(page_title="AI Voice Notes Transcriber", page_icon="🎙️", layout="wide")

st.title("🎙️ AI Voice Notes Transcriber")

st.write("Upload your audio file below:")

audio_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a", "aac", "ogg"])

if audio_file is not None:
    st.audio(audio_file)
    st.success("Audio uploaded successfully!")
