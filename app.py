import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

SITE = Path(__file__).parent

st.set_page_config(
    page_title="Central CPD Saúde | Sistemas e Serviços",
    page_icon=str(SITE / "favicon.png"),
    layout="wide",
    initial_sidebar_state="collapsed",
)


def data_uri(path: Path, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


@st.cache_data
def build_page() -> str:
    html = (SITE / "index.html").read_text(encoding="utf-8")
    css = (SITE / "style.css").read_text(encoding="utf-8")
    js = (SITE / "theme.js").read_text(encoding="utf-8")

    html = html.replace('<link rel="stylesheet" href="style.css">', f"<style>{css}</style>")
    html = html.replace('<script src="theme.js"></script>', f"<script>{js}</script>")
    html = html.replace('href="favicon.svg"', f'href="{data_uri(SITE / "favicon.svg", "image/svg+xml")}"')
    html = html.replace('src="assets/cpd-mark.svg"', f'src="{data_uri(SITE / "cpd-mark.svg", "image/svg+xml")}"')
    for name in ("tecnologia-saude.png", "tecnologia-saude-acesa.png"):
        html = html.replace(f'src="assets/{name}"', f'src="{data_uri(SITE / name, "image/png")}"')
    return html


# Esconde a interface do Streamlit e faz o site ocupar a janela inteira
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }
      html, body, .stApp { background: #f4faff; overflow: hidden; }
      .block-container, [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
      iframe {
        position: fixed !important; inset: 0 !important;
        width: 100vw !important; height: 100vh !important; height: 100dvh !important;
        border: 0 !important; z-index: 999999;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(build_page(), height=800, scrolling=True)
