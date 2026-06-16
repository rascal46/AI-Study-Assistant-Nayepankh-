# 📚 AI Study Assistant

An AI-powered study companion built using Streamlit and Google's Gemini API.

The application helps students learn more effectively through:

- 💬 AI Chat Assistant
- 📝 Quiz Generator
- 📅 Study Planner
- 🧠 Learning Memory

---

## Features

### 💬 AI Chat Assistant

Ask study-related questions and receive AI-generated explanations using Gemini.

Examples:

- Explain Z Transform
- What is Fourier Series?
- Explain Shakespeare's Macbeth

The assistant remembers previously studied topics and displays them in the sidebar.

---

### 📝 Quiz Generator

Generate topic-based quizzes instantly.

Features:

- Topic Selection
- Academic Level Selection
  - Class 10
  - Class 12
  - Diploma
  - Bachelors
  - Masters
  - Competitive Exams
  - Government Exams
  - SAT
  
- Difficulty Selection
  - Easy
  - Medium
  - Hard

Quiz Workflow:

1. AI generates 5 MCQs.
2. Questions are shown one at a time.
3. User submits an answer.
4. Correct answer and explanation are displayed.
5. Final score is shown after all questions are completed.

---

### 📅 Study Planner

Generate personalized study schedules.

Inputs:

- Subject Name
- Syllabus Topics
- Exam Date
- Study Hours Per Day

The AI creates a realistic day-by-day preparation plan including revision sessions.

---

### 🧠 Learning Memory

The application stores:

- Previously studied topics
- Chat history

Current implementation uses a local JSON file.

---

## Technology Stack

- Python
- Streamlit
- Google Gemini API
- JSON Storage

---

## Project Structure

```text
AI-Study-Assistant/
│
├── app.py
├── memory.py
├── memory.json
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Study-Assistant.git
cd AI-Study-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Deployment

The application can be deployed using:

- Streamlit Community Cloud

Environment Secret:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

---

## Future Improvements

- Persistent Database Storage (SQLite/PostgreSQL)
- User Authentication
- Progress Dashboard
- Quiz Analytics
- PDF Study Notes Generation
- Flashcard Generator
- Learning Recommendations

---

## Limitations

Current memory uses a local JSON file.

For production deployment, a database solution such as SQLite, PostgreSQL, or Firebase would be recommended for persistent storage.

---

## Author

## Author

**Tirtharaj Bhattacharya**

B.Tech Student

Built using Python, Streamlit, and Google Gemini API.
