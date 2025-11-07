# app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configure Gemini - FREE TIER
genai.configure(api_key='AIzaSyCfB16i5PkO0tI39slO7Hi4XiMrsjlRgIs')  # Get from: https://aistudio.google.com/

class RiverwoodAgent:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.system_prompt = """
        You are Riverwood AI Assistant - a friendly, warm voice agent for Riverwood Estate in Kharkhauda.
        
        PERSONALITY:
        - Warm and friendly like a family member
        - Use casual Hindi-English mix (Hinglish)
        - Remember previous conversations
        - Ask about chai, family, site visits
        - Provide construction updates naturally
        - Keep responses conversational and under 3 sentences
        - Be genuinely curious about customer's day
        
        CONSTRUCTION UPDATES (Use these realistically):
        - Foundation work: 95% complete
        - Structural work: Starting next week  
        - Landscaping: Planning phase
        - Clubhouse: Design finalized
        - Roads: 70% complete
        
        EXAMPLE PHRASES:
        "Namaste Sir! Aaj to bahut accha weather hai, chai pee li?"
        "Kal to aap site visit par aane wale the, kaisa laga Riverwood ka experience?"
        "Aapke plot number H-25 ka foundation work complete ho gaya hai!"
        "Monsoon season mein construction thoda slow hai, but planning solid chal rahi hai."
        
        Always respond in Hinglish. Be brief and warm.
        """
    
    def generate_response(self, user_input, conversation_history):
        try:
            # Prepare conversation context
            full_prompt = self.system_prompt + "\n\nConversation History:\n"
            
            for msg in conversation_history[-4:]:  # Last 4 exchanges
                full_prompt += f"{msg['role']}: {msg['content']}\n"
            
            full_prompt += f"\nUser: {user_input}\nAssistant:"
            
            # Generate response
            response = self.model.generate_content(full_prompt)
            
            return response.text.strip()
            
        except Exception as e:
            return "Arre Sir, thodi technical difficulty aa rahi hai. Dobara try karein?"

# Initialize agent
agent = RiverwoodAgent()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get('message', '')
        conversation_history = data.get('history', [])
        
        if not user_input:
            return jsonify({'error': 'Empty message'}), 400
        
        # Generate AI response
        ai_response = agent.generate_response(user_input, conversation_history)
        
        return jsonify({
            'response': ai_response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)