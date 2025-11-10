# 🏗️ Riverwood AI Voice Agent

### 🌍 [**Live Demo → Click Here**](https://ai-voice-agent-v020.onrender.com/)
> _“Namaste ji! Main Riverwood AI Assistant hoon — chai pee li?”_ ☕  
> A friendly Hinglish voice assistant built for the **Riverwood Internship Challenge**, designed to build relationships, not just real estate.

---

## 🎯 Overview

The **Riverwood AI Voice Agent** is an intelligent, human-like assistant built using **Flask** and the **Web Speech API**.  
It allows users to have **two-way real-time voice conversations** in **Hinglish (Hindi + English)** — simulating customer updates, friendly interactions, and site progress information for Riverwood Estates.

---

## 🧠 Features

✅ **🎤 Real-time Voice Input** – Speak naturally; the AI listens via browser mic.  
✅ **🗣️ Voice Output** – The AI speaks back in an Indian English tone (using `speechSynthesis`).  
✅ **💬 Hinglish Conversations** – Warm, natural, and locally relatable personality.  
✅ **🏗️ Construction Updates** – Gives realistic Riverwood progress details (Tower A, Tower B, clubhouse, etc.)  
✅ **🧠 Memory** – Remembers previous turns during a session for contextual replies.  
✅ **⚙️ Lightweight & Free** – Runs entirely on free browser APIs + Flask backend.

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask (Python) |
| **APIs Used** | Web Speech API (SpeechRecognition + SpeechSynthesis) |
| **Hosting** | Render (Free Tier) |

---

## ⚙️ How It Works

1️⃣ User clicks **Speak** or types a message  
2️⃣ Browser records the voice → converts to text  
3️⃣ Flask backend processes the message  
4️⃣ A local Hinglish response is generated (no external API needed)  
5️⃣ The browser speaks the AI’s reply back naturally  

---

## 🚀 Live Demo

🎧 **Try it out here:**  
👉 [https://ai-voice-agent-v020.onrender.com/](https://ai-voice-agent-v020.onrender.com/)

🗣️ **Example questions you can ask:**
- “Tower A update batao”  
- “Aur Tower B ka kya chal raha hai?”  
- “Chai pee li?”  
- “Thanks Riverwood!”

---

## 🖥️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yashika3013/AI-Voice-agent.git
cd AI-Voice-agent

# 2. Install dependencies
pip install flask flask-cors

# 3. Run the app
python app.py

# 4. Open in browser
http://localhost:5000

