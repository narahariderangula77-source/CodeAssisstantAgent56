import streamlit as st
from agent import CodeAssistantAgent

agent = CodeAssistantAgent()

st.set_page_config(
    page_title="🤖 AI Code Assistant",
    layout="wide",
    page_icon="⚡"
)

# Custom CSS for AI background + shadow effects
st.markdown("""
    <style>
        body {
            background-image: url("https://images.unsplash.com/photo-1504384308090-c894fdcc538d"); /* AI/tech themed */
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }
        .main {
            background-color: rgba(255, 255, 255, 0.92);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        }
        h1 {
            color: #2c3e50;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }
        .stTextInput > div > div > input,
        .stTextArea textarea {
            border: 2px solid #3498db;
            border-radius: 10px;
            font-size: 15px;
            box-shadow: inset 0 2px 6px rgba(0,0,0,0.1);
        }
        .stButton button {
            background: linear-gradient(90deg, #3498db, #2ecc71);
            color: white;
            border-radius: 10px;
            font-weight: bold;
            padding: 0.6em 1.5em;
            transition: 0.3s;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        .stButton button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #2ecc71, #3498db);
            box-shadow: 0 6px 16px rgba(0,0,0,0.3);
        }
        .response-box {
            background-color: #f0f8ff;
            border-left: 5px solid #3498db;
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1rem;
            box-shadow: 0 6px 18px rgba(0,0,0,0.15);
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("⚡ AI Code Assistant")
st.markdown("#### Your intelligent coding companion 🚀")

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📝 Developer Prompt")
    user_prompt = st.text_input(
        "Instruction",
        placeholder="Example: Fix the syntax error"
    )

    st.markdown("### ⚙️ Actions")
    analyze_button = st.button("🔍 Analyze Code")

with col2:
    st.markdown("### 💻 Paste Your Python Code")
    code = st.text_area(
        "Code Editor",
        height=300,
        placeholder="Write or paste your Python code here..."
    )

# Response section
if analyze_button:
    if code.strip() == "":
        st.warning("⚠️ Please provide code.")
    else:
        with st.spinner("🔎 Analyzing your code..."):
            response = agent.process(user_prompt, code)

        st.success("✅ Analysis Complete!")
        st.markdown("### 📢 Assistant Response")
        st.markdown(f"<div class='response-box'><pre>{response}</pre></div>", unsafe_allow_html=True)
