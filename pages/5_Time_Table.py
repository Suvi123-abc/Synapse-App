import streamlit as st

# =========================
# TIME TABLE PAGE
# =========================
st.title("📅 Daily Time Table")
st.write("Plan your daily study schedule efficiently.")

# Initialize timetable if not present
if "timetable" not in st.session_state:
    st.session_state.timetable = []

# Input section
st.subheader("Add Time Slot")
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    time_slot = st.text_input("Time (e.g., 6:00 AM - 7:00 AM)")

with col2:
    activity = st.text_input("Activity (e.g., Mathematics Study)")

with col3:
    if st.button("Add", use_container_width=True):
        if time_slot and activity:
            st.session_state.timetable.append({
                "time": time_slot,
                "activity": activity
            })
            st.success("✅ Added to schedule!")
        else:
            st.error("❌ Please fill both fields.")

# Display timetable
st.divider()
st.subheader("📋 Your Study Schedule")

if st.session_state.timetable:
    # Display as a nice table
    st.markdown("| Time Slot | Activity |")
    st.markdown("|-----------|----------|")
    
    for idx, entry in enumerate(st.session_state.timetable):
        col1, col2, col3 = st.columns([3, 3, 1])
        
        with col1:
            st.write(f"🕒 {entry['time']}")
        
        with col2:
            st.write(f"📚 {entry['activity']}")
        
        with col3:
            if st.button("❌", key=f"delete_{idx}", use_container_width=True):
                st.session_state.timetable.pop(idx)
                st.rerun()
    
    # Download option
    st.divider()
    
    timetable_text = "DAILY STUDY TIME TABLE\n" + "="*40 + "\n\n"
    for entry in st.session_state.timetable:
        timetable_text += f"Time: {entry['time']}\nActivity: {entry['activity']}\n" + "-"*40 + "\n"
    
    st.download_button(
        "📥 Download Time Table",
        timetable_text,
        file_name="daily_timetable.txt",
        use_container_width=True
    )
    
    # Clear all
    if st.button("🗑️ Clear All Entries", use_container_width=True):
        st.session_state.timetable = []
        st.rerun()

else:
    st.info("📝 No time slots added yet. Add your first time slot above!")

# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.markdown("## 📚 SYNAPSE")
st.sidebar.markdown("Smart Student Dashboard")

