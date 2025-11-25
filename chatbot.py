
import random
import google.generativeai as genai
import gradio as gr
import time

# CONFIGURE GEMINI

genai.configure(api_key="API HERE")


MOTIVATION_QUOTES = [
    "You’re stronger than you think — keep going.",
    "Small steps every day lead to big results.",
    "Your future is created by what you do today.",
    "You are capable of amazing things.",
    "Believe in yourself — you are enough.",
    "Hard times create strong people.",
    "Every day is a new chance to become better.",
]

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="""
You are 'Sadiq Ali' — a warm, emotionally intelligent motivational guide.
Answer clearly and correctly, then always add a motivational push.
Keep tone friendly, supportive, confident.
Never mention AI.
"""
)

chat_session = model.start_chat(history=[])

# ---------------------------
# BOT FUNCTION WITH STREAMING
# ---------------------------
def motivate_stream(message, history):
    if not message:
        return history, ""

    # Add user message
    history.append({"role": "user", "content": message})

    # Get bot response
    response = chat_session.send_message(message)
    bot_reply = response.text

    # Add motivational quote
    quote = random.choice(MOTIVATION_QUOTES)
    final_reply = f"{bot_reply}\n\n💖 **Sadiq Ali Motivation:** {quote}"

    # Create empty assistant message for streaming
    history.append({"role": "assistant", "content": ""})

    # Stream typing effect
    streamed = ""
    for char in final_reply:
        streamed += char
        history[-1]["content"] = streamed
        time.sleep(0.008)  # smooth typing
        yield history, ""  # return updated history and clear input

# ---------------------------
# UI
# ---------------------------
with gr.Blocks(title="MotivaBot - Sadiq Ali") as app:

    # Header
    gr.Markdown("""
    <div style="text-align:center; background: linear-gradient(to right, #FFDEE9, #B5FFFC); 
                padding: 20px; border-radius: 15px; margin-bottom:10px;">
        <h1 style="color:#FF69B4;">🌟 MotivaBot — Guided by <b>Sadiq Ali</b></h1>
        <p style="font-size:16px; color:#333;">Ask anything and I will guide, uplift, and motivate you.</p>
    </div>
    """)

    # Chat display
    chatbot = gr.Chatbot(label="Sadiq Ali", height=500)

    # Input area
    with gr.Row():
        user_input = gr.Textbox(
            placeholder="Type your message...",
            scale=8,
            lines=1,
            max_lines=3
        )
        send_btn = gr.Button("Send", scale=2)


    # EVENT HANDLING

    # Send button click
    send_btn.click(
        motivate_stream,
        inputs=[user_input, chatbot],
        outputs=[chatbot, user_input],
        queue=True
    )

    # Press Enter to submit
    user_input.submit(
        motivate_stream,
        inputs=[user_input, chatbot],
        outputs=[chatbot, user_input],
        queue=True
    )

app.launch()
