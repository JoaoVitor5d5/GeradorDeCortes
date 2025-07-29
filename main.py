import sys
import os

from utils.download_video import download_youtube_video
from utils.transcribe import transcribe_audio
from utils.highlight_segments import score_segments
from utils.generate_clips import cut_highlights_vertical

def main(youtube_url):
    os.makedirs("output", exist_ok=True)
    
    print("🔽 Baixando vídeo do YouTube...")
    video_path = download_youtube_video(youtube_url)

    print("🎙️ Transcrevendo áudio...")
    segments = transcribe_audio(video_path)

    print("📊 Selecionando trechos expressivos...")
    highlights = score_segments(segments)

    print("✂️ Gerando clipes verticais com legendas animadas...")
    clips = cut_highlights_vertical(video_path, highlights)

    print("✅ Clipes gerados com sucesso!")
    for c in clips:
        print("🔗", c)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <link-do-youtube>")
    else:
        main(sys.argv[1])

