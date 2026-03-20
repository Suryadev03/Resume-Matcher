# 📄 Skill Matcher App using Gemini API

An AI‑powered **Skill Matcher Application** that compares a candidate’s resume with a job description and generates a **match score, ATS analysis, SWOT insights, and tailored resume suggestions** using **Google Gemini API**.

This app helps **job seekers**, **recruiters**, and **HR professionals** evaluate resume–JD fit quickly and intelligently.

WebLink : https://resume-matcher-irffqn3zxkdx9vmyzvtu5d.streamlit.app/

---

## 🚀 Features

- 📑 Upload resume (PDF) via sidebar  
- 🧾 Paste job description text  
- 🤖 AI‑assisted skill matching with Gemini  
- 📊 ATS score calculation  
- ✅ Matched & unmatched keywords  
- 🔍 SWOT analysis of resume vs JD  
- ✍️ Resume improvement suggestions  
- 📄 Auto‑generated revised resumes for better shortlisting chances  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Framework:** Streamlit  
- **AI Model:** Gemini (`gemini-2.5-flash`)  
- **PDF Parsing:** PyPDF / pdfminer.six  
- **Environment Management:** python‑dotenv  

---

## 🔑 Prerequisites

- Python **3.9+**  
- Google **Gemini API Key** stored in `.env` file as `GOOGLE_GEMINI_API`  
- Internet connection  

---
## 🖥️ How It Works

- Upload your resume (PDF) in the sidebar.
- Paste the job description in the text area.
- The app sends both to Gemini API with a structured prompt.
- Gemini generates:
- ATS score & keyword analysis
- Selection probability
- SWOT analysis
- Resume positives & gaps
- Two revised resumes tailored to the JD

---
