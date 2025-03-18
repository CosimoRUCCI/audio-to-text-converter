### **README.md**

```markdown
# Audio to Text Converter

Un semplice script Python per convertire file audio (formato M4A) in testo, utilizzando Google Speech Recognition. Lo script gestisce anche file audio lunghi, dividendoli in chunk più piccoli.

## Funzionalità
- Converte file M4A in testo.
- Gestisce file audio lunghi (>10 minuti) dividendoli in chunk.
- Salva il testo estratto in un file TXT.

## Requisiti
Per far funzionare lo script, è necessario installare le seguenti librerie e strumenti:

### 1. Librerie Python
Installa le librerie richieste eseguendo:
```bash
pip install SpeechRecognition pydub
```

### 2. FFmpeg
FFmpeg è necessario per la conversione dei file audio. Segui questi passaggi per installarlo:

#### **Windows**:
1. Scarica FFmpeg da [https://www.gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds).
2. Estrai la cartella ZIP (es. in `C:\ffmpeg`).
3. Aggiungi `C:\ffmpeg\bin` al **PATH di sistema**:
   - Apri **Impostazioni di sistema avanzate** → **Variabili d'ambiente**.
   - Trova `Path` in **Variabili di sistema** e clicca su **Modifica**.
   - Aggiungi una nuova voce con il percorso `C:\ffmpeg\bin`.

#### **macOS/Linux**:
Installa FFmpeg tramite terminale:
```bash
# macOS (con Homebrew)
brew install ffmpeg

# Linux (Debian/Ubuntu)
sudo apt install ffmpeg
```

### 3. Python
Assicurati di avere Python 3.x installato. Puoi scaricarlo da [https://www.python.org/downloads/](https://www.python.org/downloads/).

---

## Come usare lo script

### 1. Clona il repository
```bash
git clone https://github.com/tuo-username/audio-to-text.git
cd audio-to-text
```

### 2. Esegui lo script
Modifica il percorso del file M4A nel file `audio_to_text.py`:
```python
m4a_file = r"C:\percorso\del\tuo\file.m4a"
```

Esegui lo script:
```bash
python audio_to_text.py
```

### 3. Risultato
Il testo estratto verrà salvato in un file chiamato `testo_estratti.txt` nella stessa cartella dello script.

---

## Personalizzazione
- **Lunghezza dei chunk**: Puoi modificare la lunghezza dei chunk cambiando il parametro `chunk_length_ms` (in millisecondi) nella funzione `m4a_to_text`.
  ```python
  testo = m4a_to_text(m4a_file, output_txt_file, chunk_length_ms=300000)  # 5 minuti
  ```

- **Lingua**: Cambia il parametro `language` in `recognize_google` per supportare altre lingue.

---

## Limitazioni
- **Limite di Google Speech Recognition**: Google impone un limite di circa 50 richieste gratuite al giorno.
- **Qualità dell'audio**: Più lungo è l'audio, maggiore è la probabilità di errori di riconoscimento. Assicurati che l'audio sia chiaro e senza rumori.

---

## Licenza
Questo progetto è rilasciato sotto la licenza MIT. Consulta il file [LICENSE](LICENSE) per ulteriori dettagli.

---

## Contributi
Se vuoi contribuire al progetto, apri una issue o invia una pull request. Ogni contributo è benvenuto!

---

## Contatti
Per domande o suggerimenti, contattami su GitHub o via email: [rucci.cosimo@gmail.com](mailto:rucci.cosimo@gmail.com).
```

---

### **Struttura del repository**
Ecco come organizzare il repository su GitHub:
```
audio-to-text/
├── audio_to_text.py       # Script principale
├── README.md              # Documentazione
├── requirements.txt       # File delle dipendenze
└── LICENSE                # Licenza (opzionale)
```

---

### **File `requirements.txt`**
- dipendenze:
```plaintext
SpeechRecognition==3.10.0
pydub==0.25.1
```

---
