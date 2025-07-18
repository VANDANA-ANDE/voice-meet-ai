import azure.cognitiveservices.speech as speechsdk
import tempfile
import os
import wave
import io

def get_audio_duration_wav(file_bytes):
    with wave.open(io.BytesIO(file_bytes), 'rb') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return duration

def transcribe_audio(uploaded_file, speech_key, service_region):
    try:
        # Step 1: Ensure WAV format only
        suffix = os.path.splitext(uploaded_file.name)[1].lower()
        if suffix != ".wav":
            return "Only WAV files are supported. Please upload a .wav file."

        # Step 2: Save uploaded file to temp location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            audio_bytes = uploaded_file.read()
            temp_audio.write(audio_bytes)
            temp_audio_path = temp_audio.name

        # Step 3: Configure Azure speech
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        audio_config = speechsdk.AudioConfig(filename=temp_audio_path)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        # Step 4: Recognize speech once
        result = speech_recognizer.recognize_once()

        # Step 5: Cleanup temp file
        os.remove(temp_audio_path)

        # Step 6: Check result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        else:
            return f"Speech recognition error: {result.reason}"

    except Exception as e:
        return f"Exception during transcription: {str(e)}"
