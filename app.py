import streamlit as st
from google import genai
from memory import load_memory, save_memory
import json

# ==========================
# Load Memory
# ==========================

memory = load_memory()

# ==========================
# Gemini Configuration
# ==========================

API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

# ==========================
# Streamlit UI
# ==========================

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Study Assistant")
st.write("Ask study-related questions, generate quizzes, and track your learning.")

# ==========================
# Sidebar
# ==========================

with st.sidebar:

    page = st.radio(
    "Navigation",
    [
        "💬 Chat Assistant",
        "📝 Quiz Generator",
        "📅 Study Planner"
    ]
)
    st.markdown("---")

   

    st.header("🕒 Previous Chats")

    for i, chat in enumerate(memory["chat_history"][-10:]):

        if st.button(
            chat["user"][:30],
            key=f"chat_{i}"
        ):
            st.session_state.selected_chat = chat

# ==========================
# Session State
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "study_plan" not in st.session_state:
    st.session_state.study_plan = ""

# ==========================
# Display Chat History
# ==========================



if "selected_chat" in st.session_state:

    st.subheader("Previous Conversation")

    st.markdown(
        f"**You:** {st.session_state.selected_chat['user']}"
    )

    st.markdown(
        f"**AI:** {st.session_state.selected_chat['assistant']}"
    )

# ==========================
# Chat Input
# ==========================

prompt = st.chat_input(
    "Ask a question..."
)

if prompt:

    # User message

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Gemini response

    with st.spinner("Thinking..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        answer = response.text

    # Assistant message

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Save memory

    memory["chat_history"].append(
        {
            "user": prompt,
            "assistant": answer
        }
    )

    if prompt not in memory["topics"]:
        memory["topics"].append(prompt)

    save_memory(memory)

# ==========================
# Quiz Generator
# ==========================

if page == "📝 Quiz Generator":

    st.header("📝 Quiz Generator")

    quiz_topic = st.text_input(
        "Enter a topic"
    )

    quiz_level = st.selectbox(
    "Select Level",
    [
        "Class 10",
        "Class 12",
        "Diploma",
        "Bachelors",
        "Masters",
        "Competitive Exams",
        "Government Exams",
        "SAT"
    ]
    )

    quiz_difficulty = st.selectbox(
    "Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
    )

    quiz_type = st.selectbox(
    "Question Type",
    [
        "Mixed",
        "Conceptual",
        "Numerical",
        "Application Based"
    ]
    )

    generate_quiz = st.button(
        "Generate Quiz"
    )

    # ==========================
    # Quiz Session Variables
    # ==========================

    if "quiz_questions" not in st.session_state:
        st.session_state.quiz_questions = []

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "show_result" not in st.session_state:
        st.session_state.show_result = False

    if "last_result" not in st.session_state:
        st.session_state.last_result = ""

    if "wrong_questions" not in st.session_state:
        st.session_state.wrong_questions = []

    # ==========================
    # Generate Quiz
    # ==========================

    if generate_quiz and quiz_topic:

        with st.spinner("Generating quiz..."):

          quiz_prompt = f"""
Generate exactly 5 MCQs.

Topic:
{quiz_topic}

Academic Level:
{quiz_level}

Difficulty:
{quiz_difficulty}

Question Type:
{quiz_type}

Requirements:

- Questions must match the selected academic level.
- Questions must match the selected difficulty.
- Questions must match the selected question type.
- Include conceptual understanding.
- Include application-based questions when appropriate.
- Avoid repeated questions.
- Each question should have 4 options.
- Only one option must be correct.
- Explanation should be 2-3 lines and educational.

Return ONLY valid JSON.

Format:

[
    {{
        "question": "Question text",
        "options": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "answer": 0,
        "explanation": "Short explanation"
    }}
]

Return exactly 5 questions.
answer must be the correct option index (0,1,2,3).
No markdown.
No code fences.
No extra text.
"""

        try:

                quiz_response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=quiz_prompt,
                    config={
                        "response_mime_type": "application/json"
                    }
                )

                questions = json.loads(
                    quiz_response.text
                )

                st.session_state.quiz_questions = questions
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.session_state.show_result = False

                st.success("Quiz generated!")

        except Exception as e:

                st.error(
                    f"Quiz generation failed: {e}"
                )

# ==========================
# Display Quiz
# ==========================

if st.session_state.quiz_questions:

    q_index = st.session_state.current_question

    if q_index < len(st.session_state.quiz_questions):

        q = st.session_state.quiz_questions[q_index]

        st.markdown("---")

        st.subheader(
            f"Question {q_index + 1} of {len(st.session_state.quiz_questions)}"
        )

        st.write(q["question"])

        selected_answer = st.radio(
            "Choose your answer:",
            range(4),
            format_func=lambda i: q["options"][i],
            key=f"question_{q_index}"
        )

        if not st.session_state.show_result:

            if st.button("Submit Answer"):

                if selected_answer == q["answer"]:

                    st.session_state.score += 1

                    st.session_state.last_result = (
                        "✅ Correct!\n\n"
                        + q["explanation"]
                    )

                else:

                    correct_option = q["options"][q["answer"]]

                    st.session_state.wrong_questions.append(
                        {
                            "question": q["question"],
                            "correct_answer": correct_option,
                            "explanation": q["explanation"]
                        }
                    )

                    st.session_state.last_result = (
                        f"❌ Incorrect.\n\n"
                        f"Correct Answer:\n{correct_option}\n\n"
                        f"{q['explanation']}"
                    )

                st.session_state.show_result = True

                st.rerun()

        else:

            st.info(
                st.session_state.last_result
            )

            if st.button("Next Question"):

                st.session_state.current_question += 1
                st.session_state.show_result = False

                st.rerun()

    else:

        st.markdown("---")

        st.success(
            f"Quiz Complete! Score: {st.session_state.score}/{len(st.session_state.quiz_questions)}"
        )

        if st.button("📊 Analyze My Performance"):

            with st.spinner("Analyzing performance..."):

                analysis_prompt = f"""
A student completed a quiz.

Topic:
{quiz_topic}

Academic Level:
{quiz_level}

Difficulty:
{quiz_difficulty}

Score:
{st.session_state.score}/{len(st.session_state.quiz_questions)}

Incorrect Questions:
{st.session_state.wrong_questions}

Analyze:

1. Which concepts seem weak?
2. What should the student revise first?
3. Create a short 3-step revision strategy.
4. Suggest 3 related topics to study next.

Keep the response concise and educational.
"""

                analysis_response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=analysis_prompt
                )

                st.markdown("---")
                st.subheader("📈 Performance Analysis")
                st.write(analysis_response.text)

        continue_quiz = st.radio(
            "Would you like another quiz?",
            ["No", "Yes"]
        )

        if continue_quiz == "Yes":

            st.session_state.quiz_questions = []
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.show_result = False

            st.info(
                "Enter a topic and generate another quiz."
            )

# ==========================
# Study Planner
# ==========================

if page == "📅 Study Planner":

    st.header("📅 Study Planner")

    subject = st.text_input(
        "Subject Name"
    )

    syllabus = st.text_area(
    "Paste Syllabus Topics",
    height=200,
    placeholder="""
    Unit 1: Signals
    Unit 2: Systems
    Unit 3: Fourier Series
    Unit 4: Fourier Transform
    Unit 5: Z Transform
    """
    )

    exam_date = st.date_input(
        "Exam Date"
    )

    hours_per_day = st.number_input(
        "Hours Per Day",
        min_value=1,
        max_value=24,
        value=3
    )

    generate_plan = st.button(
        "Generate Study Plan"
    )

    # ==========================
    # Study Planner
    # ==========================

    if generate_plan and subject and syllabus:

        with st.spinner("Creating study plan..."):

            planner_prompt = f"""
Create a realistic study plan.

Subject:
{subject}

Syllabus Topics:
{syllabus}

Exam Date:
{exam_date}

Available Study Hours Per Day:
{hours_per_day}

Requirements:

- Divide the syllabus into manageable daily tasks.
- Prioritize important topics.
- Include revision days.
- Ensure all topics are completed before the exam.
- Present as a day-by-day schedule.
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=planner_prompt
            )

            st.session_state.study_plan = response.text

    elif generate_plan:

        st.warning(
            "Please enter both subject and syllabus topics."
        )

    # ==========================
    # Display Study Plan
    # ==========================

    if st.session_state.study_plan:

        st.markdown("---")

        st.subheader("📅 Generated Study Plan")

        st.write(
            st.session_state.study_plan
        )