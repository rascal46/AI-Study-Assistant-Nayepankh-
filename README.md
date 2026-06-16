# 📚 AI Study Assistant

## Live Demo

🔗 https://ai-studyassist.streamlit.app/

---

## Overview

AI Study Assistant is an intelligent learning companion built using Streamlit and Google's Gemini API.

It helps students learn more efficiently through AI-powered explanations, interactive quizzes, personalized study plans, and performance analysis.

---

## Features

### 💬 AI Chat Assistant

Ask study-related questions and receive detailed AI-generated explanations.

**Examples:**

- Explain Z Transform
- What is Fourier Series?
- Explain Maxwell's Equations
- Explain Shakespeare's Macbeth

**Features:**

- Natural language interaction
- Detailed explanations
- Topic tracking
- Previous conversation access

---

### 🕒 Previous Chats

The assistant stores previous conversations and allows users to revisit them from the sidebar.

**Benefits:**

- Review previous learning sessions
- Quickly revisit explanations
- Maintain learning continuity

---

### 📝 Quiz Generator

Generate AI-created quizzes on any topic.

#### Academic Levels

- Class 10
- Class 12
- Diploma
- Bachelors
- Masters
- Competitive Exams
- Government Exams
- SAT

#### Difficulty Levels

- Easy
- Medium
- Hard

#### Question Types

- Mixed
- Conceptual
- Numerical
- Application Based

#### Quiz Workflow

1. Generate a quiz from a topic.
2. Questions appear one at a time.
3. Submit your answer.
4. Receive immediate feedback.
5. View explanation.
6. Proceed to the next question.
7. Receive final score.

---

### 📈 Quiz Performance Analysis

After completing a quiz, users can generate an AI-powered performance report.

The assistant analyzes:

- Weak concepts
- Knowledge gaps
- Revision priorities
- Recommended next topics
- Personalized revision strategy

This creates a mini adaptive-learning experience.

---

### 📅 Study Planner

Generate personalized study schedules based on your syllabus.

#### Inputs

- Subject Name
- Syllabus Topics
- Exam Date
- Study Hours Per Day

#### Output

The AI creates:

- Day-by-day schedule
- Topic breakdown
- Revision plan
- Realistic workload distribution

This helps students prepare systematically before examinations.

---

### 🧠 Learning Memory

The application currently stores:

- Studied topics
- Chat history
- Previous conversations

Storage is handled using local JSON files.

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
git clone https://github.com/rascal46/AI-Study-Assistant-Nayepankh-.git
cd AI-Study-Assistant-Nayepankh-
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

This project is deployed using Streamlit Community Cloud.

**Live Application:**

https://ai-studyassist.streamlit.app/

**Required Secret:**

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

---

## Future Roadmap

Planned improvements:

- Persistent database storage (SQLite/PostgreSQL)
- User authentication
- Progress dashboard
- Flashcard generator
- PDF notes generator
- Adaptive learning paths
- Quiz history tracking
- Study streak system
- Personalized topic recommendations
- Learning analytics dashboard

---

## Current Limitations

- Memory is stored using local JSON files.
- No user authentication.
- Data is not shared across devices.
- Limited long-term persistence on cloud deployments.

Future versions may integrate SQLite, PostgreSQL, or Firebase.

---

## Author

**Tirtharaj Bhattacharya**

B.Tech Electronics & Communication Engineering Student

Built with Python, Streamlit, and Google Gemini API.