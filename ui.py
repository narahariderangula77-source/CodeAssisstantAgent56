import gradio as gr
from agent import CodeAssistantAgent

agent = CodeAssistantAgent()

def chat(user_prompt, code):

    if code.strip() == "":
        return "Please provide code."

    response = agent.process(user_prompt, code)

    return response


interface = gr.Interface(
    fn=chat,
    inputs=[
        gr.Textbox(label="Developer Prompt"),
        gr.Textbox(label="Code", lines=15)
    ],
    outputs=gr.Textbox(label="Assistant Response"),
    title="AI Code Assistant Agent"
)

def launch_ui():
    interface.launch()