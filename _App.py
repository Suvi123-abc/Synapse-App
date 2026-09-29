import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="SYNAPSE",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================
# GLOBAL DARK THEME (NO BLUR)
# =========================
st.markdown("""
<style>
/* App background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #e5e7eb;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}

/* Cards */
.card {
    background: #020617;
    border-radius: 18px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border: 1px solid #1e293b;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
}

/* Titles */
.section-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.5rem;
}

/* Text */
.small-text {
    color: #cbd5f5;
}

/* Inputs */
input, textarea {
    background-color: #020617 !important;
    color: #f8fafc !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #2563eb, #1e40af);
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #1e40af, #1e3a8a);
}
</style>
""", unsafe_allow_html=True)


# =========================
# GLOBAL SESSION STATE (INITIALIZE ONCE)
# =========================
if "term1_marks" not in st.session_state:
    st.session_state.term1_marks = [0] * 6

if "term2_marks" not in st.session_state:
    st.session_state.term2_marks = [0] * 6

if "student_details" not in st.session_state:
    st.session_state.student_details = None

if "student_profile" not in st.session_state:
    st.session_state.student_profile = {}

if "timetable" not in st.session_state:
    st.session_state.timetable = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.markdown("## 📚 SYNAPSE")
st.sidebar.markdown("Smart Student Dashboard")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "💬 AI Assistant",
        "📊 Percentage Calculator",
        "📈 Graphical Analysis",
        "📄 Report Card",
        "📅 Time Table"
    ]
)


# =========================
# PAGE ROUTING
# =========================
if page == "🏠 Home":
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("home", "c:\\Users\\Suveerya Pandey\\OneDrive\\Desktop\\Python\\synapse_app\\pages\\1_Home.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

elif page == "💬 AI Assistant":
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("ai_assistant", "c:\\Users\\Suveerya Pandey\\OneDrive\\Desktop\\Python\\synapse_app\\pages\\2_AI_Assistant.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

elif page == "📊 Percentage Calculator":
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("percentage_calc", "c:\\Users\\Suveerya Pandey\\OneDrive\\Desktop\\Python\\synapse_app\\pages\\3_Percentage_Calculator.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

elif page == "📈 Graphical Analysis":
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("graphical_analysis", "c:\\Users\\Suveerya Pandey\\OneDrive\\Desktop\\Python\\synapse_app\\pages\\4_Graphical_Analysis.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

elif page == "📄 Report Card":
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("report_card", "c:\\Users\\Suveerya Pandey\\OneDrive\\Desktop\\Python\\synapse_app\\pages\\5_Report_Card.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

elif page == "📅 Time Table":
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("timetable", "c:\\Users\\Suveerya Pandey\\OneDrive\\Desktop\\Python\\synapse_app\\pages\\6_Time_Table.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
