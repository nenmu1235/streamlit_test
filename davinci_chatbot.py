#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:18:06 2023

@author: haeyuel
"""
import openai

model_engine = 'davinci'
openai.api_key = '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'

def generate_text(prompt):
    response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=20,
      n=1,
      stop="STOP",
      temperature=0.5,
    )
    raw_text = response.choices[0].text
    text = raw_text.strip()
    return text