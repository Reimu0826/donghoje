import streamlit as st
import random

# 질문지 세트 데이터 구성이 중요, 심플하게 반복문으로 구현 가능
quiz = [
    ["교목은?", ["느티나무", "소나무"]],
    ["상징 동물은?", ["동호", "토끼"]],
    ['교화는?', ['동백꽃', '무궁화']],
    ['빈 칸에 들어갈 산은?', ['백두산', '금정산']],
    ['우리 학교에 있는 석상은?', ['image01.png', 'image02.png']]
]

random.shuffle(quiz)

for no in quiz:
    st.write(no[0])
    answer = st.text_input(no[0])
    # 정답이면
