#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:40:54 2023

@author: haeyuel
"""

import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
        menu_title = "Welcome to SSK's Lab",
        options = ["Home", "People", "Researches", "Project", "Publication", "Contact"],
    )

if selected == 'Home':
    st.title(f"홈페이지 메인")
elif selected == 'Projects':
    st.title(f'프로젝트 화면')
elif selected == 'Contact':
    st.title(f'연락처')
elif selected == 'People':
    selected = option_menu(
        menu_title = "People",
        options = ["Faculty", "Graduate", "Alumny"],
        default_index = 0,
        orientation = 'horizontal',
    )
    if selected == "Faculty":
        st.title('enter faculty member')
    if selected == 'Graduate':
        st.title('enter graduate member')
    if selected == 'Alumny':
        st.title('enter alumny member')
