# highlight_segments.py
from transformers import pipeline

emotion = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

def score_segments(segments, min_clip_duration=60, max_results=6):
    scored = []
    for s in segments:
        result = emotion(s["text"])[0]
        # Considere mais rótulos se a emoção não for o único critério
        if result["label"] in ["joy", "surprise", "anger", "love", "sadness", "fear"]: # Expandido para mais emoções
            scored.append({
                "start": s["start"],
                "end": s["end"],
                "text": s["text"],
                "score": result["score"]
            })
    
    # Ordena os segmentos pela pontuação para começar com os mais relevantes
    scored.sort(key=lambda x: x["score"], reverse=True)

    final_highlights = []
    used_indices = set() # Para evitar usar o mesmo segmento várias vezes

    for i, s in enumerate(scored):
        if i in used_indices: # Se este segmento já foi usado como parte de um clipe, pule
            continue

        current_start = s["start"]
        current_end = s["end"]
        current_text = s["text"]
        
        # Encontra o índice original do segmento para verificar adjacência
        original_segment_index = -1
        for j, original_s in enumerate(segments):
            if original_s["start"] == s["start"] and original_s["end"] == s["end"]:
                original_segment_index = j
                break

        # Tenta estender o clipe para frente
        # Itera sobre os segmentos originais para manter a ordem temporal
        for k in range(original_segment_index + 1, len(segments)):
            next_s = segments[k]
            # Considera o próximo segmento se a lacuna não for muito grande (ex: 5 segundos)
            if next_s["start"] - current_end < 5: 
                current_end = next_s["end"]
                current_text += " " + next_s["text"]
                # Marca o índice do segmento original como usado
                for idx, sc in enumerate(scored):
                    if sc["start"] == next_s["start"] and sc["end"] == next_s["end"]:
                        used_indices.add(idx) # Marca o segmento original como usado

            if (current_end - current_start) >= min_clip_duration:
                break # Atingiu a duração mínima, pare de estender

        # Tenta estender o clipe para trás
        for k in range(original_segment_index - 1, -1, -1):
            prev_s = segments[k]
            if current_start - prev_s["end"] < 5: # Se a lacuna não for muito grande
                current_start = prev_s["start"]
                current_text = prev_s["text"] + " " + current_text
                # Marca o índice do segmento original como usado
                for idx, sc in enumerate(scored):
                    if sc["start"] == prev_s["start"] and sc["end"] == prev_s["end"]:
                        used_indices.add(idx) # Marca o segmento original como usado

            if (current_end - current_start) >= min_clip_duration:
                break # Atingiu a duração mínima, pare de estender
        
        # Adiciona o highlight final se ele for longo o suficiente e ainda não foi adicionado
        # (usamos um truque para evitar duplicatas: um set de tuplas (start, end)
        # para highlights já adicionados para evitar clips sobrepostos na lista final)
        if (current_end - current_start) >= min_clip_duration:
            new_highlight = {
                "start": current_start,
                "end": current_end,
                "text": current_text,
                "score": s["score"] # Mantém a pontuação do segmento inicial para ordenação
            }
            # Verifica se já existe um highlight com o mesmo start/end para evitar duplicação
            if not any(h['start'] == new_highlight['start'] and h['end'] == new_highlight['end'] for h in final_highlights):
                final_highlights.append(new_highlight)

        # Se já tivermos `max_results` clipes longos o suficiente, pare.
        if len(final_highlights) >= max_results:
            break

    # Ordena os highlights finais novamente pela pontuação (do segmento inicial)
    final_highlights.sort(key=lambda x: x["score"], reverse=True)
    return final_highlights[:max_results] # Retorna apenas os top N, que já devem ser longos