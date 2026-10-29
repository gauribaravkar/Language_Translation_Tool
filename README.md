
# 🌐 Lingua — Language Translation Tool

> **"Your words. Their language. One connected world."**

Lingua is a Python-based language translation web application that helps users translate text between multiple languages. It also allows users to listen to translated text, download translations, and access recent translation history through a simple and interactive interface.

## ✨ Features

- 🌍 **Multilingual Translation:** Translate text between supported languages.
- 🔄 **Swap Languages:** Quickly switch the source and target languages.
- 🔊 **Text-to-Speech:** Listen to translated text using generated audio.
- 🎧 **Audio Player:** Play generated speech directly in the application.
- ⬇️ **Download Translation:** Save translated text as a `.txt` file.
- 🎵 **Download Audio:** Download generated speech as an MP3 file.
- 🕘 **Recent History:** View up to 10 recent translations during the current session.
- 📋 **Copy-Friendly Output:** Copy translated text from the displayed result.
- ✨ **Sample Text:** Try the application with sample text.
- 🗑️ **Clear Text:** Clear the input and translation output.
- 🎨 **Modern Interface:** Purple gradient branding, responsive layout, and a light theme.
- ⚠️ **Error Handling:** Display helpful messages for connection and translation errors.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| MyMemory Translation API | Text translation |
| Requests | API communication |
| gTTS | Text-to-speech generation |
| HTML and CSS | Interface styling |

## 🌐 Supported Languages

Lingua currently provides the following language options:

- English
- Hindi
- Marathi
- Spanish
- French
- German
- Italian
- Portuguese
- Japanese

Translation and speech availability may vary by language and external service.

## 📁 Project Structure

```text
CodeAlpha_Language_Translation_Tool/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Install Python

Install a compatible version of Python 3 and verify the installation:

```bash
python --version
```

### 2. Clone the repository

After uploading the project to GitHub, clone it using:

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_Language_Translation_Tool.git
```

Open the project folder:

```bash
cd CodeAlpha_Language_Translation_Tool
```

Replace `YOUR_USERNAME` with your GitHub username.

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If you use Windows Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

Create a `requirements.txt` file containing:

```text
streamlit
requests
gTTS
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 🚀 How to Use Lingua

1. Open the application in your browser.
2. Select the source language.
3. Select the target language.
4. Enter text or click **Try sample**.
5. Click **Translate now**.
6. Read and copy the translated result.
7. Click **Listen to translation** to generate speech.
8. Play the audio or download the MP3.
9. Download the translated text or revisit recent translations.

## 🔄 Application Workflow

```text
User enters text
       |
       v
Select source and target languages
       |
       v
Click Translate
       |
       v
MyMemory Translation API
       |
       v
Display translated text
       |
       +------> Download translated text
       |
       +------> Generate speech using gTTS
                         |
                         v
                  Play or download MP3
```

## 🧪 Testing

Test the application with different languages and text inputs.

| Test case | Expected result |
|---|---|
| Translate English to Hindi | Display Hindi translation |
| Translate English to Marathi | Display Marathi translation |
| Enter empty text | Show a validation message |
| Select the same source and target language | Display the original text |
| Swap source and target languages | Switch the language selections |
| Generate speech | Display an audio player if successful |
| Download translated text | Download a `.txt` file |
| Disconnect the internet | Show an appropriate error message |
| Switch between languages | Use the selected language pair |

## ⚠️ Limitations

- An internet connection is required for the translation API and online speech generation.
- External API availability, usage limits, and translation quality may vary.
- Speech generation depends on the language support provided by gTTS.
- Translation history is stored in the current Streamlit session and is not permanently saved.
- The application currently supports text translation rather than document or image translation.

## 🔮 Future Improvements

- Automatic language detection
- More language options
- Favorite translations
- Persistent translation history
- Improved mobile interface
- Voice input and speech recognition
- Document translation
- Translation history export

## 🎯 Project Objective

The objective of Lingua is to build a simple and interactive language translation tool that combines translation, speech generation, and convenient output options in one application.

This project demonstrates practical use of Python, API integration, web application development, and text-to-speech technology.

## 👩‍💻 Internship Project

**Organization:** CodeAlpha  
**Project:** Language Translation Tool  
**Category:** Artificial Intelligence / Python Development



Made with ❤️ using Python and Streamlit.

**Lingua — Your words. Their language. One connected world.**
