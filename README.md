# 🎤 Text-to-Speech Converter (TTS-GUI)

A simple, Python-based desktop application that converts text into speech and plays the audio, complete with a graphical user interface (GUI) built using **Tkinter**. This tool leverages the **gTTS** (Google Text-toSpeech) library for audio generation and **Pygame** for seamless audio playback.

## ✨ Features

* **GUI Interface:** Easy-to-use desktop application for a smooth user experience.
* **Text Input:** Type or paste text directly into the entry field to generate speech.
* **File Input:** Load content from any **`.txt`** file, convert the entire document to speech, and display the content for review.
* **Instant Playback:** Audio is saved as a time-stamped MP3 file (`output_timestamp.mp3`) and automatically played instantly upon successful conversion.
* **Clear All:** Quickly reset both the single-line entry and the multi-line text display.

## 🛠️ Prerequisites

Before running the application, you need to have **Python 3.x** installed.

This project requires the following external libraries:

* **`gTTS`**: The core library for generating the speech audio.
* **`pygame`**: Used specifically for its `mixer` module to handle loading and playing the generated MP3 audio files.
* **`tkinter`**: Usually comes pre-installed with Python, used for the GUI.

## 🚀 Installation and Setup

Follow these steps to get the application running on your local machine:

### 1. Clone the Repository (Optional)

If you have this code in a repository, clone it:

Bash
git clone [https://github.com/YourUsername/repo-name.git](https://github.com/YourUsername/repo-name.git)
cd repo-name

2. Install Dependencies
Use pip to install the necessary libraries:
Bash
pip install gtts pygame

3. Run the Application
Execute the Python script from your terminal:
Bash
python tts_converter.py
