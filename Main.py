import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
import pygame
import time

pygame.mixer.init()
last_audio_file = None

def text_to_speech(text, language='en'):
    """Generates an MP3 file from text using gTTS and updates the last_audio_file variable."""
    global last_audio_file

    if not text.strip():
        messagebox.showwarning("Input Error", "Text field is empty.")
        return

    timestamp = int(time.time())
    output_file = f"output_{timestamp}.mp3"
    
    try:
        tts = gTTS(text=text, lang=language)
        tts.save(output_file)
        
        last_audio_file = output_file
        messagebox.showinfo("Success", f"Audio saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate speech:\n{e}")

def play_last_audio():
    """Plays the audio file specified by last_audio_file using pygame mixer."""
    if last_audio_file:
        try:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            
            pygame.mixer.music.load(last_audio_file)
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to play audio:\n{e}")
    else:
        messagebox.showwarning("No Audio", "No audio file available. Please convert text first.")

def text_file_to_speech():
    """Loads text from a .txt file, converts it to speech, and plays the audio."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
            
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, text)
            
            text_to_speech(text)
            play_last_audio()
            
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file or process text:\n{e}")

def clear_all_text():
    """Clears the contents of the single-line entry and multi-line text display."""
    text_entry.delete(0, tk.END)
    text_display.delete(1.0, tk.END)


root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("600x520")

# Input Label and Entry
tk.Label(root, text="Enter Text or Load File:", font=("Arial", 12)).pack(pady=5)
text_entry = tk.Entry(root, width=60, font=("Arial", 12))
text_entry.pack(pady=5, padx=10)

# Convert Button
tk.Button(
    root, 
    text="Convert Text & Play", 
    command=lambda: [text_to_speech(text_entry.get()), play_last_audio()], 
    font=("Arial", 12),
    bg="#4CAF50", fg="white"
).pack(pady=5)

tk.Button(
    root, 
    text="Convert Text File & Play", 
    command=text_file_to_speech, 
    font=("Arial", 12),
    bg="#2196F3", fg="white"
).pack(pady=5)

tk.Label(root, text="Text File/Input Content:", font=("Arial", 12)).pack(pady=5)
text_display = tk.Text(root, height=15, width=70, font=("Courier", 10), wrap=tk.WORD)
text_display.pack(pady=5, padx=10)

tk.Button(
    root, 
    text="Clear All", 
    command=clear_all_text, 
    font=("Arial", 12),
    bg="lightgray"
).pack(pady=10)

root.mainloop()
