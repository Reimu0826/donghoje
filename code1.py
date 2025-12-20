import streamlit as st
import random

quiz = [
    ["교목은?", ["느티나무", "소나무"], "느티나무"],
    ["상징 동물은?", ["동호", "토끼"], "동호"],
    ["교화는?", ["동백꽃", "무궁화"], "동백꽃"],
    ["빈 칸에 들어갈 산은?", ["백두산", "금정산"], "백두산"],
    ["우리 학교에 있는 석상은?", ["image01.png", "image02.png"], "image01.png"]
]

# 문제 섞기 (최초 1회)
if "quiz" not in st.session_state:
    random.shuffle(quiz)
    st.session_state.quiz = quiz

st.title("학교 퀴즈 (한 번에 채점)")

# 문제 표시 + 답 저장
for i, no in enumerate(st.session_state.quiz):
    question, choices, correct = no
    st.write(f"{i+1}. {question}")
    st.radio(
        "보기 선택",
        choices,
        key=f"answer_{i}"
    )

# 한 번에 채점
if st.button("정답 제출"):
    score = 0
    for i, no in enumerate(st.session_state.quiz):
        correct = no[2]
        user_answer = st.session_state.get(f"answer_{i}")
        if user_answer == correct:
            score += 1

    st.success(f"점수: {score} / {len(st.session_state.quiz)}")
