import streamlit as st

st.set_page_config(page_title="Name Formatter", layout="centered")

st.title("🧾 Full Name Formatter")

# Input from user
full_name = st.text_input("Enter your full name:")

if full_name:
    name_parts = full_name.strip().split()
    
    if len(name_parts) < 2:
        st.warning("Please enter at least a first and last name.")
    else:
        first = name_parts[0]
        last = name_parts[-1]
        middle = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""

        st.subheader("🧩 Formatted Results:")
        st.write(f"**First Last:** {first} {last}")
        st.write(f"**Last, First:** {last}, {first}")
        st.write(f"**First Middle Last:** {first} {middle} {last}".strip())
        st.write(f"**Initials:** {''.join([name[0].upper() for name in name_parts])}")
        st.write(f"**Last First Initial:** {last} {first[0].upper()}.")
        st.write(f"**Short Form:** {first} {last[0].upper()}.")
