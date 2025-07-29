from moviepy import TextClip, CompositeVideoClip

def add_animated_captions(video_clip, text, start_time=0, words_per_chunk=3):
    # --- CONFIRME SE ESTE CAMINHO ESTÁ CORRETO E VÁLIDO ---
    FONT_PATH = "arial-bold.ttf" 
    # -------------------------------------------------------------------------------

    words = text.split()
    clips = []
    clip_duration = video_clip.duration 
    
    if not words:
        return video_clip 
        
    # Calcula a duração média de cada palavra para determinar o ritmo.
    # Usamos max(0.2, ...) para garantir que cada palavra tenha um tempo mínimo visível.
    # Isso é a base para a duração do chunk.
    base_word_duration = clip_duration / len(words)
    word_duration_unit = max(0.3, base_word_duration) 

    print(f"DEBUG: Clip duration: {clip_duration}s, Total Words: {len(words)}, Avg Word Time Unit: {word_duration_unit:.2f}s")

    # Variável para controlar o tempo de início do chunk atual
    current_chunk_start_time = start_time

    # Itera sobre as palavras, pulando 'words_per_chunk' a cada passo
    # O 'range' agora avança pelos índices de início de cada chunk.
    for i in range(0, len(words), words_per_chunk):
        # Pega o grupo de palavras (chunk)
        current_chunk_words = words[i : i + words_per_chunk]
        
        if not current_chunk_words:
            continue

        chunk_text = " ".join(current_chunk_words)
        
        # A duração deste chunk é o número de palavras nele * o tempo unitário por palavra
        current_chunk_duration = len(current_chunk_words) * word_duration_unit

        # Garante que o chunk não exceda a duração total do vídeo
        if (current_chunk_start_time + current_chunk_duration) > clip_duration:
            current_chunk_duration = clip_duration - current_chunk_start_time
            if current_chunk_duration <= 0:
                continue

        txt_clip = TextClip(
            font=FONT_PATH,
            text=chunk_text, # O texto agora é o chunk de palavras
            filename=None,
            font_size=90,
            size=(int(video_clip.w * 0.9), None), # Dê um pouco de margem na largura
            margin=(None, None),
            color='yellow', 
            bg_color=None,
            stroke_color='black',
            stroke_width=2,
            method='caption',
            text_align='center',
            horizontal_align='center',
            vertical_align='center',
            interline=4,
            transparent=True,
            duration=None # A duração real é definida com .with_duration() abaixo
        )
        
        # Define a posição e a duração do chunk
        txt_clip = txt_clip.with_start(current_chunk_start_time)
        txt_clip = txt_clip.with_duration(current_chunk_duration)
        txt_clip = txt_clip.with_position(("center", "bottom"))
        
        clips.append(txt_clip)

        # Atualiza o tempo de início para o PRÓXIMO chunk, para evitar sobreposição.
        current_chunk_start_time += current_chunk_duration

    final_composite_clip = CompositeVideoClip([video_clip, *clips], size=video_clip.size)
    final_composite_clip.duration = video_clip.duration

    return final_composite_clip