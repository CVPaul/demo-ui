#!/usr/bin/env python
#-*- coding:utf-8 -*-


from enum import auto
import os
from turtle import width
import pandas as pd
import streamlit as st

import common.utils as utils
import common.constant as const
import plotly.graph_objects as go


st.set_page_config(page_title=const.TITLE, layout='wide')

INTRO = '''
该APP将覆盖覆盖从架构角度simlation所需要的全部流程，下面将简要介绍，详细功能还请点击对应页面（Page），我们尽可能做到自解释（无需文档，点开就知道怎么用）
- 首页: 首页是对当前Sim&Trader所支持情况的概述，方便一目了然的了解现在所处的状况，对开发人员而言重点关注的是diff情况，当diff大于5bp（暂定）的时候会启动追查流程（详见：数据下的Debug（数据投影）部分
- 数据: 数据部分涵盖了生产，存储，权限，传输和数据地图
- 模拟: 模拟部分将对sim程序的版本，API进行控制和简化，对用户屏蔽架构所有细节
- Sim2Real: 这部分例行复盘每日的跟踪diff情况
'''


def main():
    st.title("Overview")
    with st.expander('概要信息', expanded=True):
        st.markdown(INTRO)
    # projection_type = st.selectbox(
    #     "投影方式",[
    #         "equirectangular", "mercator", "orthographic",
    #         "natural earth", "robinson", "miller", "hammer"])
    # lon = st.slider('lon', 0, 360, 0)
    # lat = st.slider('lat', 0, 360, 0)
    # rol = st.slider('rol', 0, 360)
    projection_type = "natural earth"
    lon, lat, rol = (180, 0, 0)
    # Load world data
    world_data = go.Figure(go.Choropleth(
        locations=["CHN", "HKG", "KOR", "JPN", "IND", "USA"],  # Placeholder locations, you can replace with your own data
        z=[1, 2, 3, 4, 5, 6],  # Placeholder values, you can replace with your own data
        colorscale="Viridis",
        autocolorscale=False,
        marker_line_color='white',
        marker_line_width=0.5,
        showscale=False,  # Remove colorbar
    ))

    world_data.update_layout(
        # title_text='World Map with Different Colored Countries',
        geo=dict(
            showframe=True,
            showcountries=True,
            showcoastlines=True,
            projection=dict(
                type=projection_type,  # Change projection to orthographic
                rotation=dict(lon=lon, lat=-lat, roll=rol)
            ),
            bgcolor="#1E1E1E",
            # center=dict(lon=180),  # Set center to Pacific Ocean
        ),
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        height=800, autosize=True
    )

    # 定义动画帧
    frames = []
    num_frames = 36  # 定义36个帧，每10度一个帧
    for i in range(num_frames):
        lon = i * 10
        frame = go.Frame(
            data=[dict(type='choropleth',
                    locations=['USA', 'CAN', 'MEX'],
                    locationmode='ISO-3',
                    z=[1,2,3],  # 随机生成一些数据
                    colorscale='Viridis',
                    colorbar=dict(title='Some data'))],
            name=f'frame_{i}'
        )
        frame.layout = go.Layout(
            title='Earth Rotation Animation',
            geo=dict(
                projection=dict(
                    type='orthographic',
                    rotation=dict(lon=lon, lat=0, roll=0)),
            ),
        )
        frames.append(frame)

    world_data.frames = frames
    # Show the plot in Streamlit
    st.plotly_chart(world_data, use_container_width=True)
    
    # Create some sample data
    data = {
        'From': ['orion', 'orion', 'orion', 'orion'],
        'Source': [
            '/scratch/ailab_test/ailab_dw/trader/jptrader',
            '/scratch/ailab_test/ailab_dw/hfsignal/jpstk',
            '/scratch/ailab_test/ailab_dw/signal/jp',
            '/scratch/ailab_test/ailab_dw/signal/jp1m',
        ],
        'To': ['centaurus'] * 4,
        'Dest': [
            '/vault/ailab_test/ailab_data/jp/equity/trader/',
            '/vault/ailab_test/ailab_data/jp/equity/signal/hf',
            '/vault/ailab_test/ailab_data/jp/equity/signal/daily',
            '/vault/ailab_test/ailab_data/jp/equity/signal/1m',
        ],
        'SymbolLink': ['Same As Source'] * 4,
        'UpdateTime': ['2024-04-10'] * 4,
        "Size@Cost": ['4.1GB@4m', '50GB@1.5h', '5.0G@10m', '254MB@1m'],
        "AfterProcess": ['ln -s', 'tar -xvf|ln -s', 'ln -s', 'ln -s'],
        "Status&Progress": ["Done(100%)"] * 4
    }
    df = pd.DataFrame(data)

    # Display the table
    st.table(df)

    # Create columns with specified proportions
    col1, col2, col3, col4, col5 , col6 = st.columns([1, 3, 1, 3, 2, 1])

    # Place elements in each column
    with col1:
        selectbox1 = st.selectbox(
            "From", options=["orion"])

    with col2:
        text_input1 = st.text_input("Source")

    with col3:
        selectbox2 = st.selectbox(
            "To", options=["centaurus"])

    with col4:
        text_input2 = st.text_input("Dest")

    with col5:
        mselect = st.multiselect(
            "AfterProcess", options=['ln -s', 'tar -xvf']
        )

    with col6:
        st.write(" ")
        st.write(" ")
        submit_button = st.button("Create")


if __name__ == "__main__":
    main()
