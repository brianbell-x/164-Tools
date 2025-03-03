import streamlit as st

def display_banner():
    """Display a warning message in a Streamlit app.

    Warns users not to input classified information.
    """
    st.warning("DO NOT INPUT ANY CLASSIFIED INFORMATION")
