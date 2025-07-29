import yt_dlp
import os

def download_youtube_video(url):
    try:
        output_dir = "downloads"
        os.makedirs(output_dir, exist_ok=True)

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': os.path.join(output_dir, '%(title).40s.%(ext)s'),
            'merge_output_format': 'mp4',
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict).replace(".webm", ".mp4").replace(".mkv", ".mp4")
            print(f"✅ Vídeo baixado: {filename}")
            return filename
    except Exception as e:
        print("❌ Erro ao baixar com yt-dlp:", e)
        return None
