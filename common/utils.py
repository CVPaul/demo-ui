#!/usr/bin/env python
#-*- coding:utf-8 -*-


from PIL import Image

import streamlit as st


@st.cache_data(ttl=300)
def load_image(path):
    return Image.open(path)


def logo(logo_path):
    st.sidebar.image(
        load_image(logo_path),
        use_column_width=True)