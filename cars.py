import streamlit as st
st.set_page_config(page_title="cars")
st.markdown("##Type of cars")
st.write("-KIA")
st.image("data:image/jpeg;base64,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")
st.write("-BMW")
st.image("./flowchart.jpeg")
