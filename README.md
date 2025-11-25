# online-Motivational-chatbot-
1️⃣ Install Python 3.10+ (or 3.11 recommended)
2️⃣ Create a virtual environment
python -m venv venv
# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

Step-by-step (VS Code Terminal)
1️⃣ Make sure your virtual environment is activated

You should see:

(.venv) PS C:\Users\name\Desktop\online chatbot>


If not, activate it:

.\.venv\Scripts\activate

2️⃣ Install Gemini API library
pip install --upgrade google-generativeai


If Windows gives permission error:

python -m pip install --upgrade google-generativeai

3️⃣ Install Gradio
pip install gradio
