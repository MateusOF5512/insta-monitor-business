# BIBLIOTECAS USADAS

import streamlit as st
from PIL import Image

im = Image.open("instagram.png")
st.set_page_config(page_title="Instagram Monitor", page_icon=im, layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/



st.markdown("# Bem vindo ao Insta Monitor Business")


