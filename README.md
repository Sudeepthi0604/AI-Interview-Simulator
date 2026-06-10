🤖 AI Interview Simulator

AI Interview Simulator is an intelligent web application that conducts mock interviews and provides real-time feedback using Generative AI. It helps users practice interviews, improve communication skills, and prepare for technical roles effectively.

✨ Overview

This project simulates real interview environments by generating role-based questions and evaluating user responses. It acts like a virtual HR interviewer that guides users to improve their performance.

🚀 Key Features
🎯 Role-based AI interview generation
🧠 Dynamic question flow (based on previous answers)
💬 Natural conversation-style interview experience
📊 AI-powered answer evaluation
📈 Performance score & feedback report
📄 Resume-based question customization
⚡ Fast and interactive UI

🛠️ Tech Stack
Python
Streamlit / Flask
Google Generative AI (Gemini) / OpenAI API
FAISS (for resume-based retrieval)
SQLite (database)
HTML/CSS (UI enhancements)

📁 Project Structure
ai-interview-simulator/
│
├── app.py                  # Main application
├── interview_engine.py     # AI question generator
├── evaluator.py            # Answer evaluation logic
├── utils.py                # Helper functions
├── requirements.txt        # Dependencies
├── .env                    # API keys
│
├── database/
│   └── users.db
│
├── templates/              # UI templates (if Flask)
└── README.md

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/Sudeepthi0604/ai-interview-simulator.git
cd ai-interview-simulator
2. Create virtual environment
python -m venv ai_interview
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Add API Key

Create a secret.toml file:

GOOGLE_API_KEY=your_api_key_here
5. Run the application
streamlit run app.py

🧠 Working Flow
User selects job role & experience level
AI generates personalized interview questions
User answers in chat-like interface
AI evaluates responses using NLP
Final report is generated with suggestions
📊 Sample Output
Technical Skills: ⭐⭐⭐⭐⭐
Communication: ⭐⭐⭐⭐
Problem Solving: ⭐⭐⭐⭐⭐
Overall Score: 88/100


Feedback:

Improve explanation structure
Add more real-world examples
Practice concise answers
🔮 Future Enhancements
🎤 Voice-based interview mode
🎥 Video interview analysis
🌍 Multi-language support
📊 Advanced analytics dashboard
🧑‍💼 HR-style adaptive questioning system

👨‍💻 Author:
Sudeepthi Barla
