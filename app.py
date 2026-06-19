import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GraphOSINT | Intelligence Link Analysis",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    iframe {
        border: none;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_source = f.read()
        
    components.html(html_source, height=900, scrolling=False)
    
except FileNotFoundError:
    st.error("⚠️ Fichier 'index.html' introuvable dans le répertoire.")