import streamlit as st
from personas.persona_templates import personas
from services.ai_engine import generate_response

st.set_page_config(page_title="Persona AI")

st.title("🧠 Persona AI Chatbot")

# Select persona
persona_key = st.selectbox("Choose a persona", list(personas.keys()))
user_input = st.text_area("Ask something...")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        response = generate_response(user_input, personas[persona_key])
        st.markdown(f"**{persona_key.upper()} says:**\n\n{response}")
