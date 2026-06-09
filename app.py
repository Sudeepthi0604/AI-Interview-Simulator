# import streamlit as st
# import google.generativeai as genai

# # Configure Gemini API
# api_key = st.secrets.get("GOOGLE_API_KEY")

# if not api_key:
#     st.error("Google API Key not found!")
#     st.stop()

# genai.configure(api_key=api_key)

# model = genai.GenerativeModel("gemini-2.5-flash")

# def generate_question(role):
#     prompt = f"""
#     You are a professional interviewer.

#     Generate ONE interview question for a {role} candidate.

#     Return only the question.
#     """

#     response = model.generate_content(prompt)
#     return response.text.strip()


# def evaluate_answer(question, answer):
#     prompt = f"""
#     You are an expert interviewer.

#     Question:
#     {question}

#     Candidate Answer:
#     {answer}

#     Evaluate the answer and provide:

#     Score: /10
#     Strengths:
#     Weaknesses:
#     Suggested Improvement:
#     Ideal Answer:
#     """

#     response = model.generate_content(prompt)
#     return response.text

# # UI

# st.set_page_config(
#     page_title="AI Interview Simulator",
#     page_icon="🎤",
#     layout="wide"
# )

# st.title("🎤 AI Interview Simulator")
# st.write("Practice technical interviews using Gemini AI.")

# role = st.selectbox(
#     "Select Interview Role",
#     [
#         "Software Developer",
#         "AI/ML Engineer",
#         "Data Analyst",
#         "Python Developer",
#         "Frontend Developer",
#         "Backend Developer"
#     ]
# )

# # Session State
# if "question" not in st.session_state:
#     st.session_state.question = ""

# if "history" not in st.session_state:
#     st.session_state.history = []

# # Generate Question
# if st.button("Generate Question"):
#     st.session_state.question = generate_question(role)

# # Show Question
# if st.session_state.question:
#     st.subheader("Interview Question")
#     st.info(st.session_state.question)

#     answer = st.text_area(
#         "Enter Your Answer",
#         height=200
#     )

#     if st.button("Submit Answer"):
#         if answer.strip():

#             with st.spinner("Evaluating..."):
#                 feedback = evaluate_answer(
#                     st.session_state.question,
#                     answer
#                 )

#             st.subheader("AI Feedback")
#             st.write(feedback)

#             st.session_state.history.append({
#                 "question": st.session_state.question,
#                 "answer": answer,
#                 "feedback": feedback
#             })

#         else:
#             st.warning("Please enter an answer.")

# # Interview History
# if st.session_state.history:
#     st.subheader("Interview History")

#     for i, item in enumerate(st.session_state.history, start=1):
#         with st.expander(f"Round {i}"):

#             st.markdown("### Question")
#             st.write(item["question"])

#             st.markdown("### Your Answer")
#             st.write(item["answer"])

#             st.markdown("### Feedback")
#             st.write(item["feedback"])


import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# Configure Gemini API

api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Google API Key not found!")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# Resume Text Extraction

def extract_resume_text(pdf_file):
    text = ""

    try:
        pdf_reader = PdfReader(pdf_file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        st.error(f"Error reading PDF: {e}")

    return text

# Generate Interview Question

def generate_question(role, resume_text=""):

    prompt = f"""
    You are a professional interviewer.

    Candidate Role:
    {role}

    Candidate Resume:
    {resume_text}

    Generate ONE interview question based on:
    - Candidate skills
    - Projects
    - Technologies
    - Resume content

    If resume is empty, generate a normal interview question.

    Return only the question.
    """

    response = model.generate_content(prompt)

    return response.text.strip()

# Evaluate Answer

def evaluate_answer(question, answer):

    prompt = f"""
    You are an expert technical interviewer.

    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer and provide:

    Score: /10

    Strengths:
    - point wise

    Weaknesses:
    - point wise

    Suggested Improvements:
    - point wise

    Ideal Answer:
    """

    response = model.generate_content(prompt)

    return response.text

# Streamlit UI

st.set_page_config(
    page_title="AI Interview Simulator",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Interview Simulator")
st.write("Practice personalized interviews using Gemini AI.")


# Role Selection

role = st.selectbox(
    "Select Interview Role",
    [
        "Software Developer",
        "AI/ML Engineer",
        "Data Analyst",
        "Python Developer",
        "Frontend Developer",
        "Backend Developer"
    ]
)

# Resume Upload

uploaded_resume = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

resume_text = ""

if uploaded_resume:
    resume_text = extract_resume_text(uploaded_resume)

    st.success("Resume uploaded successfully!")

# -----------------------------
# Session State
# -----------------------------
if "question" not in st.session_state:
    st.session_state.question = ""

if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Generate Question
# -----------------------------
if st.button("Generate Question"):

    with st.spinner("Generating interview question..."):

        st.session_state.question = generate_question(
            role,
            resume_text
        )

# -----------------------------
# Display Question
# -----------------------------
if st.session_state.question:

    st.subheader("Interview Question")

    st.info(st.session_state.question)

    answer = st.text_area(
        "Enter Your Answer",
        height=200
    )

    # -------------------------
    # Submit Answer
    # -------------------------
    if st.button("Submit Answer"):

        if answer.strip():

            with st.spinner("Evaluating Answer..."):

                feedback = evaluate_answer(
                    st.session_state.question,
                    answer
                )

            st.subheader("AI Feedback")

            st.write(feedback)

            st.session_state.history.append({
                "question": st.session_state.question,
                "answer": answer,
                "feedback": feedback
            })

        else:
            st.warning("Please enter your answer.")

# -----------------------------
# Interview History
# -----------------------------
if st.session_state.history:

    st.subheader("Interview History")

    for i, item in enumerate(
        st.session_state.history,
        start=1
    ):

        with st.expander(f"Round {i}"):

            st.markdown("### Question")
            st.write(item["question"])

            st.markdown("### Your Answer")
            st.write(item["answer"])

            st.markdown("### Feedback")
            st.write(item["feedback"])