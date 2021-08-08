import sys
from pathlib import Path

# file = Path(__file__).resolve()
# parent, root = file.parent, file.parents[1]
# sys.path.append(str(root))

# try:
#     sys.path.remove(str(parent))
# except ValueError: 
#     pass

import streamlit as st
import validators

from mnist_streamlit import mnist
import os

model_pages = {
    "MNIST": mnist,
}

intro = """
This app serves MNIST hand written digit recognition model using FastAPI and Streamlit.
"""

def draw_main_page():
    st.write(f"""
    # INSTILL AI FULL STACK ENGINEER INTERVIEW!👋
    """)

    st.write(intro)

    st.info("""
        :point_left: **To get started, choose from the left sidebar.**
    """)


# Draw sidebar
pages = list(model_pages.keys())
pages.insert(0, "Home")

st.sidebar.title(f"Machine Learning Models")
selected_demo = st.sidebar.radio("", pages)

# Draw main page
if selected_demo in model_pages:
    model_pages[selected_demo]()
else:
    draw_main_page()



