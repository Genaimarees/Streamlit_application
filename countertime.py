import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer", layout="centered")
st.title("⏳ Countdown Timer with Start, Stop & Reset")

# Initialize session state
if "count" not in st.session_state:
    st.session_state.count = 10
if "running" not in st.session_state:
    st.session_state.running = False

# Functions for buttons
def start():
    if st.session_state.count > 0:
        st.session_state.running = True

def stop():
    st.session_state.running = False

def reset():
    st.session_state.running = False
    st.session_state.count = 10

# Buttons: Start, Stop, Reset
col1, col2, col3 = st.columns(3)
with col1:
    st.button("▶️ Start", on_click=start)
with col2:
    st.button("⏹️ Stop", on_click=stop)
with col3:
    st.button("🔄 Reset", on_click=reset)

# Countdown Display
placeholder = st.empty()

# Countdown logic
if st.session_state.running:
    if st.session_state.count >= 0:
        placeholder.markdown(f"## ⏱️ {st.session_state.count}")
        time.sleep(1)
        st.session_state.count -= 1
        st.rerun()  # ✅ Correct method
    else:
        st.session_state.running = False
        placeholder.markdown("## ✅ Countdown Finished!")
else:
    if st.session_state.count < 10 and st.session_state.count >= 0:
        placeholder.markdown(f"## ⏹️ Countdown Paused at {st.session_state.count}")
    else:
        placeholder.markdown(f"## ⏱️ {st.session_state.count}")
