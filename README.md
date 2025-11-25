# Motivational Coach Chatbot  
**Your personal AI-powered motivational coach — always ready to lift you up when you need it most.**  

Live Demo (when hosted): https://huggingface.co/spaces/your-username/motivational-coach  
(You’ll have your own permanent link after following the steps below)

![Preview](https://github.com/user-attachments/assets/placeholder-image.png)  
*(Replace with your own screenshot after first run)*

## Features
- Real-time conversation with full memory  
- Short, powerful, uplifting responses (1–3 sentences)  
- Beautiful, responsive web interface powered by Gradio  
- One-click public shareable link (works for 72+ hours locally)  
- Powered by Google Gemini 1.5 Flash (fast & free tier friendly)  
- Works on Windows, macOS, and Linux  

## Preview (What It Looks Like)
![Uploading image.png…]()


```
You: I keep procrastinating and feel guilty...
Coach: Guilt is just energy looking for direction. Start with one tiny task right now — 2 minutes — and watch momentum take over. You're already winning by showing up!
```

## Requirements
- Python 3.10 or 3.11 (recommended)  
- Internet connection (for Gemini API calls)  

## Quick Start (5 Minutes)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/motivational-coach-chatbot.git
cd motivational-coach-chatbot
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install google-generativeai gradio
```

### 4. Get Your Free Gemini API Key
1. Go to → https://aistudio.google.com/app/apikey  
2. Click “Create API key”  
3. Copy the key (starts with `AIzaSy...`)

### 5. Add Your API Key
Open `app.py` and replace:
```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```
with your actual key.

### 6. Run the Chatbot
```bash
python app.py
```

Your browser will open automatically at http://localhost:7860  
You’ll also get a **public shareable link** (e.g., https://xxxx.gradio.live)

### 7. Stop the App
Press `Ctrl + C` in the terminal.

## Project Structure
```
motivational-coach-chatbot/
├── app.py              # Main chatbot code
├── README.md           # This file
├── requirements.txt    # (Optional) Auto-generated
└── screenshot.png     # (Optional) Add your own
```

## Optional: Free Permanent Hosting (Recommended)

### Host on Hugging Face Spaces (100% Free)
1. Go to → https://huggingface.co/spaces  
2. Click “Create new Space”  
3. Choose “Gradio” as SDK  
4. Connect your GitHub repo  
5. Add your API key as a Secret (name: `GEMINI_API_KEY`)  
6. Deploy → Done! Permanent public link

### Host on Streamlit, Render, Railway, etc.
Just upload the repo and set the start command: `python app.py`

## Example Prompts to Try
- “I failed my exam today”  
- “I feel stuck in life”  
- “I’m scared to quit my job”  
- “Help me stay focused”  
- “I feel overwhelmed with work”

## Security Note
Never commit your API key to GitHub!  
Use environment variables or Hugging Face Secrets in production.

## Contributing
Pull requests are welcome! Feel free to:
- Improve the UI/theme  
- Add voice input  
- Add daily quote feature  
- Support multiple languages

## License
MIT License — feel free to use, modify, and share.

---
**You deserve to feel motivated every single day.**  
This bot was made to help you get there.

Made with passion by Sadiq Ali
