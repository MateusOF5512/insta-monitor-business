# BIBLIOTECAS USADAS

import streamlit as st
from PIL import Image

im = Image.open("instagram.png")
st.set_page_config(page_title="Instagram Monitor", page_icon=im, layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

from layout.pages_brasil2 import *
from layout.teste_pages3 import *


# APLICAÇÃO
topo()

st.markdown("# Insta Monitor User 1")
st.sidebar.markdown("# Insta Monitor:")


