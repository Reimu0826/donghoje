import streamlit as st
import random

quiz = [
    ["교목은?", ["느티나무", "소나무"], "느티나무"],
    ["상징 동물은?", ["동호", "토끼"], "동호"],
    ['교화는?', ['동백꽃', '무궁화'], "동백꽃"],
    ['빈 칸에 들어갈 산은?', ['백두산', '금정산'], "백두산"],
    ['우리 학교에 있는 석상은?', ['image01.png', 'image02.png'], "image01.png"]
]

# 섞기
if "shuffled" not in st.session_state:
    random.shuffle(quiz)
    st.session_state.shuffled = True

for no in quiz:
    question = no[0]
    choices = no[1]
    correct = no[2]

    st.write(question)

    answer = st.radio("보기 선택", choices, key=question)

    if st.button("정답 제출", key=question + "_btn"):
        if answer == correct:
            st.success("정답입니다!")
        else:
            st.error("오답입니다.")
