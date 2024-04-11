#!/usr/bin/env python
#-*- coding:utf-8 -*-


import streamlit as st

from common import utils
from sidebar import style


def main():
    utils.logo('image/zero.png')
    st.sidebar.divider()
    style.data()


if __name__ == "__main__":
    main()