import streamlit as st
from utils import read_pdf, read_txt
from flashcard_generator import generate_flashcards

# Page config
st.set_page_config(
    page_title="AI Flashcard Generator",
    layout="centered",
    page_icon="🤖"
)

# Custom CSS: Background, Fonts, Sidebar Label Color
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #222222;
    }

    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1470&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    [data-testid="stAppViewContainer"] > .main {
        background-color: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(8px);
        border-radius: 14px;
        padding: 2rem;
        margin: 2rem auto;
    }

    /* Sidebar Text Color */
    section[data-testid="stSidebar"] .stTextInput label,
    section[data-testid="stSidebar"] .stRadio label,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] h5,
    section[data-testid="stSidebar"] h6,
    section[data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }

    h1, h2, h3 {
        color: #111 !important;
        font-weight: 600;
        text-align: center;
    }

    .stTextInput > label, .stTextArea > label, .stFileUploader > label {
        font-weight: 500;
        color: #333;
    }

    code {
        color: #000;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Inputs (sidebar background is default; labels are white)
with st.sidebar:
    st.header("🔧 Input Settings")
    input_type = st.radio("Choose Input Type", ["Paste Text", "Upload File"])
    subject = st.text_input("Optional Subject", placeholder="e.g., Biology, History")

# Main Title
st.markdown("<h1>🤖 AI Flashcard Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444;'>Convert educational content into clean, effective Q&A flashcards using GPT</p>", unsafe_allow_html=True)
st.write("")

# Content Input Area
text = ""
if input_type == "Paste Text":
    text = st.text_area("✍️ Paste your content below", height=300, placeholder="Paste textbook content, notes, etc.")
else:
    uploaded_file = st.file_uploader("📂 Upload a .txt or .pdf file", type=["txt", "pdf"])
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            text = read_pdf(uploaded_file)
        else:
            text = read_txt(uploaded_file)

# Generate Flashcards Button
if st.button("🚀 Generate Flashcards"):
    if not text.strip():
        st.warning("⚠️ Please provide some content to generate flashcards.")
    else:
        with st.spinner("🧠 Thinking... Generating your flashcards..."):
            output = generate_flashcards(text, subject)
        st.success("✅ Flashcards Generated!")

        st.markdown("### 🧾 Flashcards:")
        st.code(output, language="markdown")

        st.download_button(
            label="📥 Download Flashcards",
            data=output,
            file_name="flashcards.txt",
            mime="text/plain"
        )

# Footer
st.markdown(
    """
    <hr style='margin-top: 2em;'>
    <p style='text-align: center; color: #999;'>Made with ❤️ using OpenAI & Streamlit</p>
    <p style='text-align: center; color: #999;'>Made by Pravesh Kumar</p>
    """,
    unsafe_allow_html=True
)
