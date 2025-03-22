import requests
import streamlit as st

# Function to get response from Llama API
def get_llama_response(input_text):
    response = requests.post("http://localhost:8000/story/invoke",
                             json={'input': {'topic': input_text}})
    return response.json().get('output', "Error: Unexpected response format")

# Function to get response from Gemma API
def get_gemma_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input': {'topic': input_text}})
    return response.json().get('output', "Error: Unexpected response format")

# App title with emoji 🎭📜
st.markdown(
    "<h1 style='text-align: center; color: #6A5ACD;'>✨ LangChain Story & Poem Generator ✍️📖</h1>", 
    unsafe_allow_html=True
)

# Sidebar for theme selection
st.sidebar.title("🎨 Theme Settings")
theme = st.sidebar.radio("Choose a theme:", ["Light", "Dark"])

# Background styling
if theme == "Dark":
    st.markdown("""
        <style>
            body { background-color: #2E2E2E; color: white; }
            .stTextInput > div > div > input { background-color: #444; color: white; }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body { background-color: #F5F5F5; color: black; }
        </style>
        """, unsafe_allow_html=True)

# Create a two-column layout
col1, col2 = st.columns(2)

# Story input (Left side)
with col1:
    st.subheader("📖 Write a Story")
    input_text = st.text_input("Enter a topic for the story", key="story_input")
    if input_text:
        story = get_llama_response(input_text)
        st.markdown(f"<div style='background:#E6E6FA; padding:10px; border-radius:10px;'>{story}</div>", unsafe_allow_html=True)

# Poem input (Right side)
with col2:
    st.subheader("✍️ Write a Poem")
    input_text1 = st.text_input("Enter a topic for the poem", key="poem_input")
    if input_text1:
        poem = get_gemma_response(input_text1)
        st.markdown(f"<div style='background:#FFE4E1; padding:10px; border-radius:10px;'>{poem}</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ using LangChain & Streamlit</p>", 
    unsafe_allow_html=True
)
