import whisper

def transcribe_audio(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    print("📝 Transcrição concluída.")
    return result["segments"]
