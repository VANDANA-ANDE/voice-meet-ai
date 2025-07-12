import streamlit as st
from transcriber import transcribe_audio
from summarizer import generate_summary
from pdf_export import export_to_pdf

st.set_page_config(page_title="AI Voice Notes Transcriber", page_icon="🎙️", layout="wide")
st.title("🎙️ AI Voice Notes Transcriber")
st.write("Upload your audio file below:")

# Upload audio
audio_file = st.file_uploader(
    "Choose an audio file", 
    type=["wav", "mp3", "m4a", "aac", "ogg"], 
    key="audio_upload"
)

# Load secrets
speech_key = st.secrets["SPEECH_KEY"]
service_region = st.secrets["SPEECH_REGION"]

# Initialize session state variables if not present
if "transcript" not in st.session_state:
    st.session_state.transcript = ""
if "summary" not in st.session_state:
    st.session_state.summary = ""

# Audio uploaded
if audio_file:
    st.audio(audio_file)
    st.success("Audio uploaded successfully!")

    if st.button("Transcribe Audio", key="transcribe_btn"):
        with st.spinner("Transcribing..."):
            st.session_state.transcript = transcribe_audio(audio_file, speech_key, service_region)
            st.session_state.summary = ""  # Clear old summary if any

# Show transcript if available
if st.session_state.transcript:
    st.subheader("📝 Transcript")
    st.write(st.session_state.transcript)

    # Generate summary only if not already generated
    if not st.session_state.summary:
        if st.button("Generate Summary", key="summary_btn"):
            with st.spinner("Summarizing..."):
                st.session_state.summary = generate_summary(st.session_state.transcript)

# Show summary if available
if st.session_state.summary:
    st.subheader("📄 Meeting Summary")
    st.write(st.session_state.summary)

    # PDF export
    st.markdown("---")
    st.subheader("⬇️ Download Report")
    pdf_file = export_to_pdf(st.session_state.transcript, st.session_state.summary)
    st.download_button(
        label="📄 Download PDF",
        data=pdf_file,
        file_name="meeting_summary.pdf",
        mime="application/pdf"
    )
