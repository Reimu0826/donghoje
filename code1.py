#ChatGPT사용

import streamlit as st
import random
import uuid  # 초기화용 key 생성

quiz = [
    ["교목은?", ["느티나무", "소나무"], "느티나무"],
    ["상징 동물은?", ["동호", "토끼"], "동호"],
    ["교화는?", ["동백꽃", "무궁화"], "동백꽃"],
    ["빈 칸에 들어갈 산은?", ["백두산", "금정산"], "백두산"],
    ["우리 학교에 있는 석상은?", ["image01.png", "image02.png"], "image01.png"]
]

#초기화: 문제 순서와 보기 순서
if "quiz" not in st.session_state:
    random.shuffle(quiz)
    st.session_state["quiz"] = quiz

if "choices" not in st.session_state:
    st.session_state["choices"] = {}
    for i, q in enumerate(st.session_state["quiz"]):
        shuffled = q[1][:]
        random.shuffle(shuffled)
        st.session_state["choices"][i] = shuffled

#초기화: 문제별 radio key
if "radio_keys" not in st.session_state:
    st.session_state["radio_keys"] = [f"answer_{i}_{uuid.uuid4()}" for i in range(len(quiz))]

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

st.title("학교 퀴즈")

#문제 표시
for i, no in enumerate(st.session_state["quiz"]):
    st.write(f"{i+
