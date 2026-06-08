import streamlit as st
import pathlib

st.set_page_config(page_title="Durable E2E Tests on Temporal", layout="wide")

html = pathlib.Path(__file__).parent / "flow.html"
st.components.v1.html(html.read_text(), height=2200, scrolling=True)

