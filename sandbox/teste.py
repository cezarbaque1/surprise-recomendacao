import streamlit as st
from st_click_detector import click_detector

if "n_clicks" not in st.session_state:
    st.session_state["n_clicks"] = "0"

with st.sidebar:
    choice = st.radio("Radio", [1, 2, 3])

id = str(int(st.session_state["n_clicks"]) + 1)

content = f"<a href='#' id='1'><img src='https://img.freepik.com/vetores-gratis/praia-com-cena-de-paisagem-marinha-de-coquetel-de-coco_603843-2345.jpg'></a>"
clicked = click_detector(content, key="1")
st.write(id)
content = f"<a href='#' id='2'><img src='https://img.freepik.com/vetores-gratis/praia-com-cena-de-paisagem-marinha-de-coquetel-de-coco_603843-2345.jpg'></a>"
clicked = click_detector(content, key="2")

if clicked != "" and clicked != st.session_state["n_clicks"]:
    st.session_state["n_clicks"] = clicked
    choice = clicked
    st.subheader("Saving Report..")
else:
    st.subheader(f"Choice: #{choice}")