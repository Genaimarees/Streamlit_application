# names_app.py

import streamlit as st

# Title
st.title("Name Length Checker")

# List of 5 names
names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

# Display names with their lengths
st.subheader("Names and Their Lengths:")
for name in names:
    st.write(f"🔹 {name} - {len(name)} characters")
