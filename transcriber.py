import azure.cognitiveservices.speech as speechsdk
import tempfile
import os
from pydub import AudioSegment

def transcribe_audio(uploaded_file, speech_key, service_region):
    try:
        # Step 1: Save uploaded file to temp file
        suffix = os.path.splitext(uploaded_file.name)[1].lower()
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_audio:
            temp_audio.write(uploaded_file.read())
            temp_audio_path = temp_audio.name

        # Step 2: Convert to WAV if not already WAV
        if suffix != ".wav":
            wav_path = temp_audio_path + ".wav"
            audio = AudioSegment.from_file(temp_audio_path)
            audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
            audio.export(wav_path, format="wav")
            os.remove(temp_audio_path)  # remove original temp file
            temp_audio_path = wav_path

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
