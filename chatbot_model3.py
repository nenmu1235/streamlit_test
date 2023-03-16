#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:24:37 2023

@author: haeyuel
"""

from translator import *
from davinci_chatbot import generate_text


import streamlit as st


try:
    text = st.text_input("대화를 입력하세요: ")
    en_text = ko_to_en(text)
    response = generate_text(en_text)
    ko_text = en_to_ko(response)
    st.write("당신: ",text)
    st.write("Chatbot: ", ko_text)
except:
    pass
