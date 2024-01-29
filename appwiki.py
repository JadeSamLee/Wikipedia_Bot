import streamlit as st
from langchain.utilities import WikipediaAPIWrapper

input = st.text_input('Type your prompt here')

wikipedia = WikipediaAPIWrapper()

if input:
    text = wikipedia.run(input)
    st.text(text)

