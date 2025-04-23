# 🩺 Medical Report Summarizer

[![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-ff4b4b?style=flat-square&logo=streamlit&logoColor=white)]()
[![Live App](https://img.shields.io/badge/Try%20It-Live%20Demo-00c853?style=flat-square)](https://heath-app.onrender.com/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

A simple and powerful healthcare tool that allows users to upload a **medical report image** and get an instant, AI-generated summary in **plain English**.

---

## 🧠 What It Does

This app uses the **Moonshot AI multimodal model** via [OpenRouter](https://openrouter.ai) to:
- 🔍 Analyze medical report images (JPG/PNG)
- 🧾 Understand the document content
- 🗣️ Respond in clean, simple language
- 🧑‍⚕️ Act as a virtual healthcare assistant for quick assessments

---

## 🚀 Live Demo

👉 [Click here to try it out!](https://heath-app.onrender.com/)

---

## 🛠️ Tech Stack

| Layer       | Tech                               |
|-------------|------------------------------------|
| **Frontend**| [Streamlit](https://streamlit.io)  |
| **Backend** | Python                             |
| **AI Model**| `moonshotai/kimi-vl-a3b-thinking:free` via OpenRouter |
| **Image**   | PIL, Base64 Encoding               |
| **Auth**    | `.env` for securing API keys       |

---

## 📸 Screenshots

> Upload a medical report and receive a concise health summary.

![example](screenshots/back1.PNG)

---

## ⚙️ Setup Instructions

### 🔐 Prerequisites
- Python 3.8+
- [OpenRouter API key](https://img2.PNG)

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/medical-report-summarizer.git
cd medical-report-summarizer

# Install dependencies
pip install -r requirements.txt

# Add your OpenRouter API key
touch .env
echo "api_key=your_api_key_here" >> .env
