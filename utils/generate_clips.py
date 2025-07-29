from moviepy import VideoFileClip, CompositeVideoClip, ColorClip # Adicionado ColorClip e CompositeVideoClip para Opção 2
import os
from .text_animation import add_animated_captions 

def cut_highlights_vertical(video_path, highlights, output_dir="output"):
    base_clip = VideoFileClip(video_path)
    output_files = []

    os.makedirs(output_dir, exist_ok=True)

    for i, h in enumerate(highlights):
        subclip = base_clip.subclipped(h["start"], h["end"]) # Corrigido para .subclipped()
        
        target_width = 1080
        target_height = 1920

        subclip_aspect_ratio = subclip.w / subclip.h
        target_aspect_ratio = target_width / target_height 

        if subclip_aspect_ratio > target_aspect_ratio:
            # O vídeo é mais "largo" que o formato 9:16.
            # Redimensiona para que a altura do vídeo corresponda à altura alvo.
            # A largura será automaticamente calculada, sendo maior que 1080.
            resized_clip = subclip.resized(height=target_height)
            
            # Corta a largura para o tamanho alvo (1080), centralizando o conteúdo.
            # O `x_center` deve ser calculado com base na largura do `resized_clip`.
            final = resized_clip.cropped(x_center=resized_clip.w / 2, width=target_width)
        else:
            # O vídeo é mais "alto" ou da mesma proporção que o 9:16.
            # Redimensiona para que a largura do vídeo corresponda à largura alvo.
            # A altura será automaticamente calculada, sendo maior que 1920.
            resized_clip = subclip.resized(width=target_width)
            
            # Corta a altura para o tamanho alvo (1920), centralizando o conteúdo.
            # O `y_center` deve ser calculado com base na altura do `resized_clip`.
            final = resized_clip.cropped(y_center=resized_clip.h / 2, height=target_height)

        if "text" in h and h["text"]:
            final = add_animated_captions(final, h["text"])

        out_path = os.path.join(output_dir, f"tiktok_clip_{i+1}.mp4")
        
        final.write_videofile(out_path, codec="libx264", audio_codec="aac", fps=subclip.fps)
        output_files.append(out_path)

    base_clip.close()
    return output_files