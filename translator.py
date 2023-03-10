#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:22:33 2023

@author: haeyuel
"""
import googletrans
def translate(text, lan):
    translator = googletrans.Translator()
    response = translator.translate(text, dest = lan).text
    return response
def ko_to_en(text):
    ja_text = translate(text, "ja")
    en_text = translate(ja_text, "en")
    return en_text
def en_to_ko(text):
    ja_text = translate(text, "ja")
    ko_text = translate(ja_text, "ko")
    return ko_text
