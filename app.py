import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GraphOSINT | Intelligence Link Analysis",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

full_screen_css = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        z-index: 99999 !important;
    }
</style>
"""
st.markdown(full_screen_css, unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_source = f.read()
        
    components.html(html_source)
    
except FileNotFoundError:
    st.error("⚠️ Fichier 'index.html' introuvable dans le répertoire.")
