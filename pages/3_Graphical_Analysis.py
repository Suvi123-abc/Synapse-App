import os
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from groq import Groq

# =========================
# GROQ API CONFIGURATION
# =========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
def ask_groq(prompt):
    """
    Send a prompt to Groq API and get a response.
    
    Args:
        prompt (str): The prompt to send to Groq
        
    Returns:
        str: The response from Groq, or an error message
    """
    try:
        if not GROQ_API_KEY:
            return "⚠️ Groq API key not configured. Please add GROQ_API_KEY to your Streamlit secrets."
        
        client = Groq(api_key=GROQ_API_KEY)
        message = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",
        )
        return message.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error generating response: {str(e)}"

# =========================
# PERFORMANCE ANALYSIS PAGE
# =========================
st.title("📈 Performance Analysis and AI Assistance")
st.write("Visualize your academic progress across subjects.")

# Subject list
subjects = ["Maths", "Science", "SST", "Hindi", "English", "3rd Language"]

# Initialize session state if needed
if "term1_marks" not in st.session_state:
    st.session_state.term1_marks = [0, 0, 0, 0, 0, 0]

if "term2_marks" not in st.session_state:
    st.session_state.term2_marks = [0, 0, 0, 0, 0, 0]

# Display comparison chart
st.subheader("Term 1 vs Term 2 Marks")

if any(st.session_state.term1_marks) or any(st.session_state.term2_marks):
    x = np.arange(len(subjects))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    bars1 = ax.bar(x - width/2, st.session_state.term1_marks, width, label="Term 1", color="#1f77b4")
    bars2 = ax.bar(x + width/2, st.session_state.term2_marks, width, label="Term 2", color="#ff7f0e")

    ax.set_xlabel("Subjects", fontsize=12)
    ax.set_ylabel("Marks", fontsize=12)
    ax.set_title("Subject-wise Performance", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(subjects, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    st.pyplot(fig)

    # Individual subject analysis
    st.divider()
    st.subheader("📊 Individual Subject Performance")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Term 1 Details:**")
        for subject, mark in zip(subjects, st.session_state.term1_marks):
            st.write(f"{subject}: {mark}/100")
    
    with col2:
        st.write("**Term 2 Details:**")
        for subject, mark in zip(subjects, st.session_state.term2_marks):
            st.write(f"{subject}: {mark}/100")
    
    with col3:
        st.write("**Improvement:**")
        for i, subject in enumerate(subjects):
            improvement = st.session_state.term2_marks[i] - st.session_state.term1_marks[i]
            color = "🟢" if improvement >= 0 else "🔴"
            st.write(f"{color} {subject}: {improvement:+d}")

    # =========================
    # SMART STUDY PLAN SECTION
    # =========================
    st.divider()
    st.subheader("🧠 Generate Smart Study Plan")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Generate Plan Based on Term 1 Marks"):
            if not st.session_state.term1_marks or all(m == 0 for m in st.session_state.term1_marks):
                st.error("Please enter valid Term 1 marks first.")
            else:
                weak_subjects = [subjects[i] for i, m in enumerate(st.session_state.term1_marks) if m < 60]
                if weak_subjects:
                    prompt = f"I need a daily study plan to improve in {', '.join(weak_subjects)}. Provide a structured, encouraging plan."
                    with st.spinner("Generating study plan..."):
                        plan = ask_groq(prompt)
                        if "Error" in plan or "⚠️" in plan:
                            st.error(plan)
                        else:
                            st.write("**Your Smart Study Plan for Term 1:**")
                            st.markdown(plan)
                else:
                    st.success("Great job! No weak subjects detected (all >= 60). Keep it up!")
    with col2:
        if st.button("Generate Plan Based on Term 2 Marks"):
            if not st.session_state.term2_marks or all(m == 0 for m in st.session_state.term2_marks):
                st.error("Please enter valid Term 2 marks first.")
            else:
                weak_subjects = [subjects[i] for i, m in enumerate(st.session_state.term2_marks) if m < 60]
                if weak_subjects:
                    prompt = f"I need a daily study plan to improve in {', '.join(weak_subjects)}. Provide a structured, encouraging plan."
                    with st.spinner("Generating study plan..."):
                        plan = ask_groq(prompt)
                        if "Error" in plan or "⚠️" in plan:
                            st.error(plan)
                        else:
                            st.write("**Your Smart Study Plan for Term 2:**")
                            st.markdown(plan)
                else:
                    st.success("Great job! No weak subjects detected (all >= 60). Keep it up!")

else:
    st.info("📝 Enter marks in the 'Marks Input' section to see your analysis.")

# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.markdown("## 📚 SYNAPSE")
st.sidebar.markdown("Smart Student Dashboard")
