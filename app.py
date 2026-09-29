import os
import json
import streamlit as st
from dotenv import load_dotenv
from google import genai


# ==========================================
# CONFIGURATION
# ==========================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
HISTORY_FILE = "history.json"
MODEL_NAME = "gemini-3.6-flash"


# ==========================================
# CHECK API KEY
# ==========================================

if not API_KEY:
    st.error("Gemini API key not found. Check your .env file.")
    st.stop()


client = genai.Client(api_key=API_KEY)


# ==========================================
# HISTORY FUNCTIONS
# ==========================================

def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_history(history):
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(
                history,
                file,
                ensure_ascii=False,
                indent=2
            )
    except Exception:
        pass


# ==========================================
# STREAMLIT PAGE
# ==========================================

st.set_page_config(
    page_title="Solvora",
    page_icon="💡",
    layout="centered"
)
st.markdown(
    """
    <style>
    .welcome-card {
    padding: 22px;
    margin: 20px 0;
    border-radius: 16px;
    background: #f7f9fc;
    border: 1px solid #e1e7f0;
}

.welcome-card h3 {
    margin-top: 0;
    font-size: 24px;
}

.welcome-card p {
    font-size: 16px;
    color: #5f6368;
    line-height: 1.6;
}

    .solvora-logo {
        font-size: 45px;
    }

    .solvora-header h1 {
        margin: 0;
        font-size: 38px;
    }

    .solvora-header p {
        margin: 4px 0 0 0;
        font-size: 16px;
        color: #5f6368;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# SESSION STATE
# ==========================================

if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "quick_question" not in st.session_state:
    st.session_state.quick_question = None

if "history" not in st.session_state:
    st.session_state.history = load_history()


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown(
        """
        <div class="solvora-header">
            <div class="solvora-logo">💡</div>
            <div>
                <h1>Solvora</h1>
                <p>Your intelligent problem-solving assistant</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Language
    st.subheader("🌐 Language")

    language = st.selectbox(
        "Choose your language",
        [
            "English",
            "ಕನ್ನಡ (Kannada)"
        ]
    )

    st.divider()

    # Category
    st.subheader("📂 Choose a category")

    category = st.selectbox(
        "Problem type",
        [
            "🌐 General Problem",
            "🎓 Education",
            "💼 Career",
            "💻 Programming",
            "📝 Productivity",
            "💡 Other"
        ]
    )

    st.divider()

    # Clear current conversation
    if st.button("🗑️ Clear Conversation"):

        st.session_state.conversation = []
        st.session_state.quick_question = None

        st.rerun()

    st.divider()

    # History
    st.subheader("🕘 History")

    if st.session_state.history:

        for i, item in enumerate(
            reversed(st.session_state.history),
            1
        ):

            question = item.get(
                "question",
                "Previous question"
            )

            st.write(
                f"**{i}.** {question}"
            )

    else:

        st.caption(
            "No previous questions yet."
        )

    st.divider()
    with st.expander("about solvora"):
        st.write(
            "Solvora is an AI-powered problem-solving assistant "
            "that helps you find practical solutions to your problems. "
            "It can provide guidance on a variety of topics, including "
            "education, career, programming, productivity, and more."
        )
        st.write(
            "it can help with education, career planning,"
            " programming, productivity, and general questions."
        )
        with st.expander("safety & responsible AI"):
            st.write(
                "solvora provide general information and guidance."
                        "AI responses may sometimes be incorrect."
            )
            st.write(
        "For medical, legal, financial, or other high-risk "
        "situations, consult a qualified professional."
    )

    st.write(
        "Do not share passwords, API keys, or other sensitive "
        "personal information with Solvora."
    )

    st.divider()
    st.caption("Solvora")
    st.caption("AI Problem-Solving Assistant")


# ==========================================
# MAIN TITLE
# ==========================================

st.markdown(
    """
    <div class="solvora-header">
        <div class="solvora-logo">💡</div>
        <div>
            <h1>Solvora</h1>
            <p>Your intelligent problem-solving assistant</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
# ==============================
# QUICK SUGGESTIONS
# ==============================

st.markdown("### 💡 Quick Suggestions")
st.caption("Choose a topic to get started with Solvora")

col1, col2 = st.columns(2)

if language == "English":

    with col1:

        if st.button("🎓 Study Plan", use_container_width=True):
            st.session_state.quick_question = (
                "Create a simple and effective study plan "
                "for a BTech CSE student."
            )

        if st.button("💻 Learn Python", use_container_width=True):
            st.session_state.quick_question = (
                "Teach me Python from beginner level "
                "step by step with simple examples."
            )

        if st.button("🧑‍💻 Programming Help", use_container_width=True):
            st.session_state.quick_question = (
                "Help me understand a programming problem "
                "with a simple step-by-step explanation."
            )

    with col2:

        if st.button("💼 Career Help", use_container_width=True):
            st.session_state.quick_question = (
                "Help me create a step-by-step career "
                "preparation plan for an IT job."
            )

        if st.button("📝 Productivity", use_container_width=True):
            st.session_state.quick_question = (
                "Create a simple daily productivity plan "
                "for studying and learning skills."
            )

        if st.button("🌐 General Problem", use_container_width=True):
            st.session_state.quick_question = (
                "I have a problem and need a practical "
                "solution. Help me step by step."
            )

else:

    with col1:

        if st.button("🎓 ಅಧ್ಯಯನ ಯೋಜನೆ", use_container_width=True):
            st.session_state.quick_question = (
                "BTech CSE ವಿದ್ಯಾರ್ಥಿಗಾಗಿ ಸರಳವಾದ ಅಧ್ಯಯನ "
                "ಯೋಜನೆಯನ್ನು ರಚಿಸಿ."
            )

        if st.button("💻 Python ಕಲಿಯಿರಿ", use_container_width=True):
            st.session_state.quick_question = (
                "Python ಅನ್ನು beginner level ನಿಂದ "
                "ಸರಳ ಉದಾಹರಣೆಗಳೊಂದಿಗೆ ಹಂತ ಹಂತವಾಗಿ ಕಲಿಸಿ."
            )

        if st.button("🧑‍💻 Programming ಸಹಾಯ", use_container_width=True):
            st.session_state.quick_question = (
                "ನನಗೆ programming problem ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು "
                "ಹಂತ ಹಂತವಾಗಿ ಸಹಾಯ ಮಾಡಿ."
            )

    with col2:

        if st.button("💼 Career ಸಹಾಯ", use_container_width=True):
            st.session_state.quick_question = (
                "IT job ಗಾಗಿ ಹಂತ ಹಂತವಾಗಿ career "
                "preparation plan ನೀಡಿ."
            )

        if st.button("📝 Productivity", use_container_width=True):
            st.session_state.quick_question = (
                "ಓದು ಮತ್ತು skills ಕಲಿಯಲು ಸರಳವಾದ "
                "daily productivity plan ನೀಡಿ."
            )

        if st.button("🌐 ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆ", use_container_width=True):
            st.session_state.quick_question = (
                "ನನಗೆ ಒಂದು ಸಮಸ್ಯೆ ಇದೆ. ಅದಕ್ಕೆ practical "
                "solution ಅನ್ನು ಹಂತ ಹಂತವಾಗಿ ನೀಡಿ."
            )







# ==========================================
# WELCOME MESSAGE
# ==========================================
if len(st.session_state.conversation) == 0:

    if language == "English":

        st.markdown(
            """
            <div class="welcome-card">
                <h3>👋 Welcome to Solvora</h3>
                <p>
                    Tell me your problem and I'll help you
                    find a practical solution.
                </p>
                <p>
                    💡 Ask about studies, careers, programming,
                    productivity, or everyday problems.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="welcome-card">
                <h3>👋 Solvora ಗೆ ಸ್ವಾಗತ</h3>
                <p>
                    ನಿಮ್ಮ ಸಮಸ್ಯೆಯನ್ನು ಹೇಳಿ. ಪ್ರಾಯೋಗಿಕ ಪರಿಹಾರ
                    ಕಂಡುಕೊಳ್ಳಲು ನಾನು ಸಹಾಯ ಮಾಡುತ್ತೇನೆ.
                </p>
                <p>
                    💡 Studies, careers, programming, productivity
                    ಅಥವಾ ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳ ಬಗ್ಗೆ ಕೇಳಬಹುದು.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================
# DISPLAY CONVERSATION
# ==========================================

for message in st.session_state.conversation:

    if message["role"] == "user":

        with st.chat_message("user", avatar="👤"):
            st.markdown(message["content"])

    else:

        with st.chat_message("assistant", avatar="💡"):
            st.markdown(message["content"])

# ==========================================
# USER INPUT
# ==========================================

if language == "English":

    input_placeholder = (
        "Describe your problem..."
    )

else:

    input_placeholder = (
        "ನಿಮ್ಮ ಸಮಸ್ಯೆಯನ್ನು ಇಲ್ಲಿ ಬರೆಯಿರಿ..."
    )
# ==============================
# PHOTO QUESTION
# ==============================
st.markdown("### 📷 Ask Solvora about a photo")

uploaded_image = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"],
    help="Upload a question, document, diagram, or other image."
)

if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="Uploaded image",
        use_container_width=True
    )

    photo_question = st.text_input(
        "❓ What would you like to know about this photo?",
        placeholder="Example: Explain this question step by step."
    )

    if st.button("🔍 Analyze Photo", use_container_width=True):

        if not photo_question.strip():
            st.warning("Please enter a question about the photo.")

        else:
            try:
                # Read the uploaded image
                image_bytes = uploaded_image.getvalue()

                # Send image + question to Gemini
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=[
                        photo_question,
                        genai.types.Part.from_bytes(
                            data=image_bytes,
                            mime_type=uploaded_image.type
                        )
                    ]
                )

                st.markdown("### 💡 Solvora's Answer")
                st.markdown(response.text)
                # AI SPEAKER
                speaker_text = response.text.replace("`", "").replace("*", "")

                st.markdown(
                    f"""
                    <button
                        onclick="speakSolvora()"
                        style="
                            padding:10px 18px;
                            border-radius:10px;
                            border:1px solid #d1d5db;
                            background:#f7f9fc;
                            cursor:pointer;
                            font-size:16px;
                        ">
                        🔊 Read Answer Aloud
                    </button>

                    <script>
                    function speakSolvora() {{
                        const text = {speaker_text!r};
                        window.speechSynthesis.cancel();
                        const speech = new SpeechSynthesisUtterance(text);
                        speech.rate = 0.9;
                        speech.pitch = 1;
                        window.speechSynthesis.speak(speech);
                    }}
                    </script>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(
                    "Solvora is temporarily unable to analyze "
                    "this photo. Please try again later."
                )

 

user_input = st.chat_input(
    input_placeholder
)


# ==========================================
# QUICK QUESTION
# ==========================================

if st.session_state.quick_question:

    user_input = (
        st.session_state.quick_question
    )

    st.session_state.quick_question = None


# ==========================================
# PROCESS USER QUESTION
# ==========================================

if user_input:

    # ------------------------------
    # SHOW USER QUESTION
    # ------------------------------

    with st.chat_message("user"):

        st.write(user_input)


    # ------------------------------
    # SAVE USER MESSAGE
    # ------------------------------

    st.session_state.conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    # ------------------------------
    # BUILD CONVERSATION
    # ------------------------------

    conversation_text = ""

    for message in st.session_state.conversation:

        conversation_text += (
            message["role"]
            + ": "
            + message["content"]
            + "\n"
        )


    # ==========================================
    # LANGUAGE INSTRUCTION
    # ==========================================

    if language == "English":

        language_instruction = """
Answer completely in English.
Use simple and clear English.
"""

    else:

        language_instruction = """
Answer completely in Kannada (ಕನ್ನಡ).
Use simple, natural Kannada.
Technical terms such as Python, GitHub,
SQL and API can remain in English when useful.
"""


    # ==========================================
    # SOLVORA PROMPT
    # ==========================================

    prompt = f"""
You are Solvora, an intelligent problem-solving assistant.

Selected category:
{category}

Required language:
{language_instruction}

Safety rules:
- Do not provide dangerous or harmful instructions.
- For medical problems, provide general information and recommend consulting a qualified healthcare professional.
- For legal or financial problems, provide general information and recommend consulting a qualified professional when appropriate.
- If the user may be in immediate danger, encourage them to contact local emergency services or a trusted person.
- Be honest about uncertainty and do not pretend to be a professional.

Conversation:
{conversation_text}

Help the user solve their problem.

Give:
1. A clear explanation.
2. Practical steps.
3. Simple language.
4. Examples when useful.

Remember the previous conversation.
"""


    # ==========================================
    # GEMINI REQUEST
    # ==========================================

    with st.chat_message("assistant"):

        if language == "English":

            spinner_text = (
                "Solvora is thinking..."
            )

        else:

            spinner_text = (
                "Solvora ಯೋಚಿಸುತ್ತಿದೆ..."
            )


        with st.spinner(spinner_text):

            response = None
            last_error = None

            try:

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

            except Exception as e:

                last_error = e


        # ==========================================
        # SUCCESS
        # ==========================================

        if response:

            answer = response.text

            st.write(answer)


            # ------------------------------
            # SAVE CONVERSATION
            # ------------------------------

            st.session_state.conversation.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )


            # ------------------------------
            # SAVE HISTORY
            # ------------------------------

            st.session_state.history.append(
                {
                    "question": user_input,
                    "answer": answer,
                    "category": category
                }
            )


            save_history(
                st.session_state.history
            )


            # ==========================================
            # USEFUL RESOURCES
            # ==========================================

            st.divider()

            if language == "English":

                st.subheader(
                    "🔗 Useful Resources"
                )

            else:

                st.subheader(
                    "🔗 ಉಪಯುಕ್ತ ಸಂಪನ್ಮೂಲಗಳು"
                )


            if "Programming" in category:

                st.markdown(
                    "🐍 **Python:** https://docs.python.org/3/"
                )

                st.markdown(
                    "💻 **GitHub:** https://github.com/"
                )

                st.markdown(
                    "🧩 **LeetCode:** https://leetcode.com/"
                )


            elif "Education" in category:

                st.markdown(
                    "📚 **Khan Academy:** https://www.khanacademy.org/"
                )

                st.markdown(
                    "🎓 **MIT OpenCourseWare:** https://ocw.mit.edu/"
                )


            elif "Career" in category:

                st.markdown(
                    "💼 **LinkedIn:** https://www.linkedin.com/"
                )

                st.markdown(
                    "💻 **GitHub:** https://github.com/"
                )

                st.markdown(
                    "🧑‍💻 **LeetCode:** https://leetcode.com/"
                )


            elif "Productivity" in category:

                st.markdown(
                    "📝 **Notion:** https://www.notion.so/"
                )


            else:

                st.markdown(
                    "🔎 **Google:** https://www.google.com/"
                )


        # ==========================================
        # ERROR HANDLING
        # ==========================================

        else:

            error_text = str(last_error).lower()


            # ------------------------------
            # QUOTA / RATE LIMIT
            # ------------------------------

            if (
                "429" in error_text
                or "quota" in error_text
                or "resource exhausted" in error_text
            ):

                if language == "English":

                    st.warning(
                        "⚠️ Solvora has temporarily reached "
                        "the Gemini API usage limit. "
                        "Please try again later."
                    )

                else:

                    st.warning(
                        "⚠️ Solvora Gemini API ಬಳಕೆಯ ಮಿತಿಯನ್ನು "
                        "ತಾತ್ಕಾಲಿಕವಾಗಿ ತಲುಪಿದೆ. "
                        "ಸ್ವಲ್ಪ ಸಮಯದ ನಂತರ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ."
                    )


            # ------------------------------
            # TEMPORARY SERVER ERROR
            # ------------------------------

            elif (
                "503" in error_text
                or "unavailable" in error_text
                or "temporarily" in error_text
            ):

                if language == "English":

                    st.warning(
                        "⚠️ Solvora is temporarily unable "
                        "to connect to Gemini. "
                        "Please wait a little and try again."
                    )

                else:

                    st.warning(
                        "⚠️ Solvora ಈಗ Gemini ಗೆ ಸಂಪರ್ಕಿಸಲು "
                        "ತಾತ್ಕಾಲಿಕವಾಗಿ ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ. "
                        "ಸ್ವಲ್ಪ ಸಮಯದ ನಂತರ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ."
                    )


            # ------------------------------
            # OTHER ERROR
            # ------------------------------

            else:

                if language == "English":

                    st.warning(
                        "⚠️ Solvora couldn't process "
                        "your request right now. "
                        "Please try again later."
                    )

                else:

                    st.warning(
                        "⚠️ Solvora ಈಗ ನಿಮ್ಮ ವಿನಂತಿಯನ್ನು "
                        "ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. "
                        "ಸ್ವಲ್ಪ ಸಮಯದ ನಂತರ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ."
                    )