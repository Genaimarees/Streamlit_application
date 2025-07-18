import streamlit as st

st.set_page_config(page_title="Word Reverser", layout="centered")
st.title("🔁 Word Reverser App")

# Text input from user
sentence = st.text_input("Enter a sentence to reverse each word:")

# When user clicks the Enter button
if st.button("Enter"):
    if not sentence.strip():
        st.warning("Please enter a non-empty sentence.")
    else:
        # Split sentence into words and reverse each word
        reversed_words = [word[::-1] for word in sentence.split()]
        result = " ".join(reversed_words)
        
        # Display result
        st.subheader("🔄 Reversed Words:")
        st.success(result)
