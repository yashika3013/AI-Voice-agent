# app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

def generate_response_local(user_input, conversation_history):
    text = user_input.lower().strip()

    # 1. Construction-related responses
    if "tower a" in text:
        return "Tower A almost ready hai, finishing touch chal raha hai. Possession January 2026 tak expected hai."
    if "tower b" in text:
        return "Tower B interiors chal rahe hain – flooring aur paint full speed pe hai."
    if "clubhouse" in text:
        return "Clubhouse ka design finalize ho gaya hai, opening next month plan hai!"
    if "road" in text or "roads" in text:
        return "Internal roads 70 percent done hain, markings aur lights abhi lag rahe hain."
    if "landscaping" in text or "garden" in text:
        return "Landscaping planning stage me hai – green zones ka layout finalize ho raha hai."
    if "construction" in text or "update" in text:
        return "Aaj ka site update: Tower A almost done, Tower B interiors chal rahe hain, clubhouse opening soon!"

    # 2. Friendly chat
    if "chai" in text or "coffee" in text:
        return "Haha! Chai bina toh Riverwood incomplete lagta hai ☕ Aapne chai pee li?"
    if "hello" in text or "hi" in text or "namaste" in text:
        return "Namaste ji! Kaise ho aap? Aaj ka din kaisa jaa raha hai?"
    if "thank" in text:
        return "Arre koi baat nahi! Riverwood ke saath ho toh sab easy hai 😎"
    if "visit" in text or "site" in text or "possession" in text:
        return "Aap kab aa rahe ho site pe? Weekend visit kaafi chill hota hai!"

    # 3. Simple memory-based continuation
    if conversation_history:
        last_user = next((msg["content"].lower() for msg in reversed(conversation_history) if msg["role"] == "user"), "")
        if "tower" in last_user:
            return "Sab towers schedule pe hain — aapka investment safe side pe hai 💯"
        if "chai" in last_user:
            return "Waise aap chai lover ho ya coffee gang? Mujhe lagta hai chai gang ho 😌"

    # 4. Default fallback
    return "Sab kuch smooth chal raha hai Riverwood me 🏗️ Aap kis tower ka update chahte ho — A, B, ya clubhouse?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get("message", "").strip()
        history = data.get("history", [])

        if not user_input:
            return jsonify({"error": "Empty message"}), 400

        ai_response = generate_response_local(user_input, history)
        return jsonify({
            "response": ai_response,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        print("Error:", e)
        return jsonify({
            "response": "Thoda technical glitch aa gaya 😅 fir se boliye?",
            "timestamp": datetime.now().isoformat()
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)