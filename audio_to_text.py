"""
MIT License

Copyright (c) 2025 CosimoRUCCI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software...
"""


import speech_recognition as sr
from pydub import AudioSegment
import os

def split_audio(audio, chunk_length_ms=300000):  # 5 minuti (300000 ms)
    """Divide l'audio in chunk più piccoli."""
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunks.append(audio[i:i + chunk_length_ms])
    return chunks

def m4a_to_text(m4a_file, output_txt_file="output.txt", chunk_length_ms=300000):
    # Verifica che il file esista
    if not os.path.exists(m4a_file):
        raise FileNotFoundError(f"File {m4a_file} non trovato!")
    
    # Converti M4A in WAV
    wav_file = "temp_converted.wav"
    try:
        audio = AudioSegment.from_file(m4a_file, format="m4a")
        audio = audio.set_frame_rate(16000)  # Imposta la frequenza a 16 kHz
        audio.export(wav_file, format="wav")
    except Exception as e:
        return f"Errore durante la conversione del file: {str(e)}"
    
    # Trascrivi l'audio
    recognizer = sr.Recognizer()
    full_text = ""
    
    try:
        # Carica l'audio e dividilo in chunk
        audio = AudioSegment.from_wav(wav_file)
        chunks = split_audio(audio, chunk_length_ms)
        
        # Elabora ogni chunk separatamente
        for i, chunk in enumerate(chunks):
            chunk_file = f"chunk_{i}.wav"
            chunk.export(chunk_file, format="wav")
            
            with sr.AudioFile(chunk_file) as source:
                audio_data = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio_data, language="it-IT")
                    full_text += text + "\n"
                except sr.UnknownValueError:
                    print(f"Chunk {i}: Google Speech Recognition non ha capito l'audio")
                except sr.RequestError as e:
                    print(f"Chunk {i}: Errore dal servizio API - {e}")
            
            # Rimuovi il file chunk dopo l'elaborazione
            if os.path.exists(chunk_file):
                os.remove(chunk_file)
        
        # Salva il testo completo in un file TXT
        with open(output_txt_file, "w", encoding="utf-8") as txt_file:
            txt_file.write(full_text)
        
        return full_text
    
    except Exception as e:
        return f"Errore durante la trascrizione: {str(e)}"
    finally:
        # Rimuovi il file temporaneo WAV
        if os.path.exists(wav_file):
            os.remove(wav_file)

# Esempio di utilizzo
try:
    # Specifica il file M4A e il file TXT di output
    m4a_file = r"C:\percorso\del\tuo\file.m4a"
    output_txt_file = "testo_estratti.txt"
    
    # Esegui la conversione e salva il testo
    testo = m4a_to_text(m4a_file, output_txt_file)
    print("Testo estratto:\n", testo)
    print(f"Il testo è stato salvato in: {output_txt_file}")
except Exception as e:
    print("Errore:", str(e))