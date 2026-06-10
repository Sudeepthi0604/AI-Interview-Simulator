🤖 AI Interview Simulator

An AI-powered mock interview platform that simulates real interview experience, evaluates answers, and provides instant feedback using Generative AI.

🚀 Features
🎤 Real-time AI Interview Simulation
🧠 Smart question generation based on role/skills
📊 Instant feedback on answers
📝 Score evaluation (communication, accuracy, confidence)
📄 Resume-based question generation (optional)
💡 Improvement suggestions after interview
🌐 Web-based UI (Streamlit / Flask / React – depending on your build)
🏗️ Tech Stack
Python 🐍
Streamlit / Flask (Frontend)
Google Generative AI / OpenAI API 🤖
SQLite / Firebase (Database)
NLP + Prompt Engineering
FAISS (optional for resume Q&A)
📂 Project Structure
ai-interview-simulator/
│
├── app.py
├── interview_engine.py
├── feedback_generator.py
├── utils.py
├── requirements.txt
├── .env
├── assets/
│   └── ui_images
├── database/
│   └── users.db
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/ai-interview-simulator.git
cd ai-interview-simulator
2️⃣ Create virtual environment
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add API Key

Create .env file:

GOOGLE_API_KEY=your_api_key_here
5️⃣ Run the app
streamlit run app.py
🎯 How It Works
User selects role (e.g., Software Developer, Data Analyst)
AI generates interview questions
User answers questions via UI
AI evaluates responses
Final report with score + suggestions is generated
📊 Output Example
Communication Score: 8.5/10
Technical Accuracy: 9/10
Confidence Level: 8/10
Feedback: Improve explanation clarity & add real-time examples
💡 Future Improvements
🎥 Video-based interview analysis
🗣️ Voice input/output support
📈 Advanced analytics dashboard
🧑‍💼 HR-style adaptive questioning
🌍 Multi-language support
👨‍💻 Author

Sudeepthi Barla
