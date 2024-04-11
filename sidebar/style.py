#!/usr/bin/env python
#-*- coding:utf-8 -*-


import streamlit as st
import common.utils as utils


def data():
    # Info
    with st.sidebar.expander("数据生产", expanded=True):
        st.write("Product")
        st.write('xxx')
    with st.sidebar.expander('数据存储'):
        st.write("Product")
    with st.sidebar.expander('数据权限'):
        st.write("Product")
    with st.sidebar.expander('数据传输'):
        st.write("Product")
    with st.sidebar.expander('数据地图'):
        st.write("Product")