import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="RITESH KUMAR SAH AI | LearnCodeOnline",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme and animations
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Root variables */
    :root {
        --primary-color: #6366f1;
        --secondary-color: #8b5cf6;
        --accent-color: #f59e0b;
        --bg-dark: #0f172a;
        --bg-card: #1e293b;
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --border-color: #334155;
    }
    
    /* Main background */
    .stApp {
        background: gradient(to bottom right, var(--bg-dark), var(--bg-card));  
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit header and footer */
    header[data-testid="stHeader"] {
        display: none;
    }
    
    .stApp > footer {
        display: none;
    }
    
    /* Custom header */
    .main-header {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.3);
        animation: slideDown 0.8s ease-out;
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        margin: 0.5rem 0 0 0;
        font-weight: 300;
    }
    
    /* Chat container */
    .chat-container {
        background: var(--bg-card);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        animation: fadeInUp 0.6s ease-out;
        min-height: 400px;
        max-height: 600px;
        overflow-y: auto;
    }
    
    /* Message styles */
    .user-message {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 5px 20px;
        margin: 1rem 0;
        max-width: 80%;
        margin-left: auto;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        animation: slideInRight 0.5s ease-out;
        font-weight: 500;
        word-wrap: break-word;
    }
    
    .Ritesh-message {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        color: var(--text-primary);
        padding: 1.5rem;
        border-radius: 20px 20px 20px 5px;
        margin: 1rem 0;
        max-width: 85%;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        animation: slideInLeft 0.5s ease-out;
        line-height: 1.6;
        word-wrap: break-word;
    }
    
    .Ritesh-message::before {
        content: "👨‍💻 Ritesh Bhai";
        display: block;
        font-weight: 600;
        color: var(--accent-color);
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: var(--bg-card) !important;
        color: var(--text-primary) !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(99, 102, 241, 0.4) !important;
    }
    
    /* Stats cards */
    .stats-card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .stats-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    }
    
    .stats-number {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary-color);
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    /* Quote section */
    .quote-section {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
        border-left: 4px solid var(--primary-color);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 2rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    .quote-text {
        color: var(--text-primary);
        font-size: 1.1rem;
        font-style: italic;
        line-height: 1.6;
    }
    
    .quote-author {
        color: var(--text-secondary);
        margin-top: 0.5rem;
        font-weight: 500;
    }
    
    /* Welcome message */
    .welcome-message {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: var(--text-secondary);
        margin: 2rem 0;
        animation: fadeIn 1.2s ease-out;
    }
    
    .welcome-message h3 {
        color: var(--primary-color);
        margin-bottom: 1rem;
    }
    
    /* Animations */
    @keyframes slideDown {
        from { transform: translateY(-30px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes fadeInUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-dark);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary-color);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--secondary-color);
    }
</style>
""", unsafe_allow_html=True)

# Initialize OpenAI client
@st.cache_resource
def init_openai_client():
    try:
        return OpenAI()
    except Exception as e:
        st.error(f"Failed to initialize OpenAI client: {str(e)}")
        st.error("Please make sure your OPENAI_API_KEY is set in your .env file")
        return None

client = init_openai_client()

# System prompt
from personas.persona_templates import PERSONA_TEMPLATES
SYSTEM_PROMPT = PERSONA_TEMPLATES.get("Ritesh Kumar Sah", "default persona")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "message_count" not in st.session_state:
    st.session_state.message_count = 0

if "processing" not in st.session_state:
    st.session_state.processing = False

# Header
st.markdown("""
<div class="main-header">
    <h1>RITESH KUMAR SAH</h1>
    <p>Your coding mentor & career guide - LearnCodeOnline ke saath</p>
</div>
""", unsafe_allow_html=True)

# Stats section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="stats-card">
        <div class="stats-number">{st.session_state.message_count}</div>
        <div class="stats-label">Messages Exchanged</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">43</div>
        <div class="stats-label">Countries Traveled</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">2M+</div>
        <div class="stats-label">Students Impacted</div>
    </div>
    """, unsafe_allow_html=True)

# Quote section
quotes = [
    ("Code sikhna mushkil nahi hai, bas consistent rehna padta hai.", "Ritesh Kumar sah"),
    ("Framework aate jaate rehte hain, concepts strong rakhiye.", "Ritesh Kumar sah"),
    ("Programming ek skill hai, problem solving ek art hai.", "Ritesh Kumar sah"),
    ("Kabhi kabhi break lena zaroori hota hai, burnout se bachne ke liye.", "Ritesh Kumar sah"),
    ("College mein marks ki bhag-daud mein skills bhool jaate hain.", "Ritesh Kumar sah")
]

random_quote = random.choice(quotes)
st.markdown(f"""
<div class="quote-section">
    <div class="quote-text">"{random_quote[0]}"</div>
    <div class="quote-author">— {random_quote[1]}</div>
</div>
""", unsafe_allow_html=True)



# Chat container
chat_container = st.container()

with chat_container:
    
    
    # Show welcome message if no chat history
    if not st.session_state.chat_history:
        st.markdown("""
        <div class="welcome-message">
            <h3>Hello! Main Ritesh hoon</h3>
            <p>Coding, career, ya life ke bare mein kuch bhi pooch sakte ho. Main yahan hoon help karne ke liye!</p>
            <p><strong>Try asking:</strong> "React kaise seekhun?", "Career guidance chahiye", "Coding se dar lagta hai"</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Display chat history
    for i, message in enumerate(st.session_state.chat_history):
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="Ritesh-message">{message["content"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Input section
st.markdown("---")

# Create form to handle Enter key submission
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            "",
            placeholder="Typing something...",
            label_visibility="collapsed",
            disabled=st.session_state.processing
        )
    
    with col2:
        send_button = st.form_submit_button(
            "Send 🚀", 
            use_container_width=True,
            disabled=st.session_state.processing
        )

# Handle form submission
if send_button and user_input.strip() and not st.session_state.processing:
    if client is None:
        st.error("❌ OpenAI client not initialized. Please check your API key configuration.")
    else:
        # Set processing state
        st.session_state.processing = True
        
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
        st.session_state.messages.append({"role": "user", "content": user_input.strip()})
        st.session_state.message_count += 1
        
        # Get AI response
        try:
            with st.spinner("🤔 Ritesh bhai is thinking..."):
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=st.session_state.messages,
                    temperature=0.7,
                    max_tokens=1000
                )
                
                ai_response = response.choices[0].message.content.strip()
                
                # Add AI response to chat history
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                st.session_state.message_count += 1
                
        except Exception as e:
            st.error(f"❌ Oops! Something went wrong: {str(e)}")
            st.error("💡 Please make sure your OpenAI API key is set correctly in your .env file.")
        
        finally:
            # Reset processing state
            st.session_state.processing = False
            
        # Rerun to show the new messages
        st.rerun()

# Action buttons
col1, col2 = st.columns(2)

with col1:
    if st.session_state.chat_history and st.button("🗑️ Clear Chat", help="Start a fresh conversation"):
        st.session_state.chat_history = []
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.session_state.message_count = 0
        st.rerun()

with col2:
    if st.button("💡 Example Questions", help="Get some conversation starters"):
        st.info("""
        **Try asking Ritesh bhai:**
        - "React kaise seekhun from scratch?"
        - "Career guidance chahiye, confused hoon"
        - "Coding interview ki preparation kaise karun?"
        - "Burnout ho gaya hai, kya karun?"
        - "Open source contribute karna hai"
        - "YouTube channel start karna chahta hoon"
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 1rem;">
    <p>Built with ❤️ for the coding community | LearnCodeOnline</p>
    <p style="font-size: 0.9rem;">🎯 "Seekhte rahiye, sikhate rahiye" - Ritesh Kumar sah</p>
    <p style="font-size: 0.8rem; margin-top: 1rem;">⚡ Powered by OpenAI GPT-4 | Made with Streamlit</p>
</div>
""", unsafe_allow_html=True)


# Second persona here...
# import streamlit as st
# from personas.persona_templates import personas
# from services.ai_engine import generate_response

# st.set_page_config(page_title="Persona AI")

# st.title("🧠 Persona AI Chatbot")

# # Select persona
# persona_key = st.selectbox("Choose a persona", list(personas.keys()))
# user_input = st.text_area("Ask something...")

# if st.button("Ask"):
#     with st.spinner("Thinking..."):
#         response = generate_response(user_input, personas[persona_key])
#         st.markdown(f"**{persona_key.upper()} says:**\n\n{response}")