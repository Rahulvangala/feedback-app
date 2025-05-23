# 📝 Feedback Form Automation Project

This project demonstrates how to build a simple feedback form using **HTML**, **Flask (Python)**, and automate feedback submission using **UiPath RPA** integrated with Python scripts.

---

## 🚀 Project Features

- 🔧 **HTML Frontend**: A simple form to collect user feedback.
- 🐍 **Python Flask Backend**: Receives form data and stores it using an in-memory SQLite database.
- 🤖 **UiPath Automation**: Automatically submits and validates feedback using Python Scope activities.

---

## 🗂 Files Included

| File | Description |
|------|-------------|
| `Feedback.html` | The web form that collects feedback from the user |
| `App.py` | Python Flask server that handles form submissions and stores them in memory |
| `FeedbackAutomation.py` | Python script to test feedback submission |
| `FeedbackFormAutomation/Main.xaml` | UiPath workflow that automates feedback submission |
| `FeedbackFormAutomation/project.json` | UiPath project configuration file |

---

## 💻 How to Run This Project

### 1. Start the Flask App
Open your terminal and run:
```bash
python App.py
This will start the Flask server at: http://localhost:5001

2. Open the Form
Open Feedback.html in a browser and fill out the form to test it manually.

3. Run the Python Automation Script
Run this command in terminal or from your Python IDE:
python FeedbackAutomation.py

4. Run UiPath Automation (Optional)
Open UiPath Studio

Open the Main.xaml file

Make sure Python is installed and the Python path is correctly configured in the Python Scope activity

Click Run to execute the automation
