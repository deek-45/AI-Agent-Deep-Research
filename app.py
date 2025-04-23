import streamlit as st
from main import build_graph

st.set_page_config(page_title="AI Research Assistant", layout="centered")
st.title("🔍 AI Agent-Based Research Assistant")

query = st.text_input("Enter your research question:", "")

if st.button("Run Research"):
    st.info("Running dual-agent research...", icon="💡")
    try:
        result = build_graph(query)
        st.success("Research complete! Here's your draft:")
        st.markdown(result["draft"])
    except Exception as e:
        st.error("⚠️ Failed to retrieve research results. Please check your internet connection or API key and try again.")
        st.exception(e)