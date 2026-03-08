# 🤖 Code Assistant Agent

AI-powered assistant that **analyzes, fixes, and explains code** using the **Google Gemini API**.
The project provides a simple **Streamlit web interface** where users can paste code and receive error detection, fixes, and explanations.

---

## 🚀 Features

* **Syntax Error Detection** – Identifies syntax errors in code.
* **Automatic Fix Suggestions** – Suggests corrected versions of code.
* **Code Explanation** – Explains what the code does in simple terms.
* **Gemini AI Integration** – Uses Google Gemini models for intelligent analysis.
* **Streamlit UI** – Interactive interface for testing the assistant.

---

## 📂 Project Structure

```
code-assistant-agent/
│
├── agent.py          # Main AI agent logic
├── tools.py          # Code analysis tools
├── validator.py      # Syntax validation module
├── app.py            # Streamlit user interface
├── requirements.txt  # Project dependencies
├── .env              # API key configuration (not pushed to GitHub)
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/code-assistant-agent.git
cd code-assistant-agent
```

Install required dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Gemini API Setup

1. Generate an API key from **Google AI Studio**.
2. Create a `.env` file in the project directory.
3. Add your API key:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

Start the Streamlit interface:

```
streamlit run app.py
```

After running the command, the app will open in your browser.

---

## 🧪 Example

Input code:

```python
print("Hello
```

The agent will:

1. Detect the syntax error.
2. Suggest a corrected version of the code.
3. Provide an explanation of the issue.

---

## 🛠 Technologies Used

* Python
* Streamlit
* Google Gemini API
* python-dotenv

---

## 📌 Future Improvements

* Support for multiple programming languages
* Code optimization suggestions
* GitHub integration for automated code review
* Memory-based conversation with the assistant

---

## 📜 License

This project is licensed under the **MIT License**.
