import streamlit as st
from streamlit_modern_select import streamlit_modern_select

options = ["a", "b", "c", "d", "e"]
value = streamlit_mdern_select(options, size=3)
st.write(f"You selected {value}")