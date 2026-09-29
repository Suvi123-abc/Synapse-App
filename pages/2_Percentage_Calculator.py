import streamlit as st

# =========================
# MARKS INPUT PAGE
# =========================
st.title("📝 Enter Marks")
st.write("Record your marks for both terms here.")

# Subject list
subjects = ["Maths", "Science", "SST", "Hindi", "English", "3rd Language"]

# Initialize session state if needed
if "term1_marks" not in st.session_state:
    st.session_state.term1_marks = [0, 0, 0, 0, 0, 0]

if "term2_marks" not in st.session_state:
    st.session_state.term2_marks = [0, 0, 0, 0, 0, 0]

# Input marks in two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Term 1 Marks")
    for i, subject in enumerate(subjects):
        st.session_state.term1_marks[i] = st.number_input(
            f"{subject}",
            min_value=0,
            max_value=100,
            value=st.session_state.term1_marks[i],
            key=f"term1_{i}"
        )

with col2:
    st.subheader("Term 2 Marks")
    for i, subject in enumerate(subjects):
        st.session_state.term2_marks[i] = st.number_input(
            f"{subject}",
            min_value=0,
            max_value=100,
            value=st.session_state.term2_marks[i],
            key=f"term2_{i}"
        )

# Display summary
st.divider()
st.subheader("📊 Summary")

term1_avg = sum(st.session_state.term1_marks) / len(subjects) if any(st.session_state.term1_marks) else 0
term2_avg = sum(st.session_state.term2_marks) / len(subjects) if any(st.session_state.term2_marks) else 0

col1, col2 = st.columns(2)
with col1:
    st.metric("Term 1 Average", f"{term1_avg:.2f}%")

with col2:
    st.metric("Term 2 Average", f"{term2_avg:.2f}%")

st.success("✅ Marks saved automatically!")

# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.markdown("## 📚 SYNAPSE")
st.sidebar.markdown("Smart Student Dashboard")

