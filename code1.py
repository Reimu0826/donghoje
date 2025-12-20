#ChatGPT사용

import streamlit as st
import random
import uuid

quiz = [
    ["교목은?", ["느티나무", "소나무"], "느티나무"],
    ["상징 동물은?", ["동호", "토끼"], "동호"],
    ["교화는?", ["동백꽃", "무궁화"], "동백꽃"],
    ["빈 칸에 들어갈 산은?", ["백두산", "금정산"], "백두산"],
    ["우리 학교에 있는 석상은?", ["image01.png", "image02.png"], "image01.png"]
]

# 문제와 보기 초기화
if "quiz" not in st.session_state:
    random.shuffle(quiz)
    st.session_state["quiz"] = quiz

if "choices" not in st.session_state:
    st.session_state["choices"] = {}
    for i, q in enumerate(st.session_state["quiz"]):
        shuffled = q[1][:]
        random.shuffle(shuffled)
        st.session_state["choices"][i] = shuffled

# 문제별 라디오 key 초기화
if "radio_keys" not in st.session_state:
    st.session_state["radio_keys"] = [f"answer_{i}_{uuid.uuid4()}" for i in range(len(quiz))]

# 제출 상태 초기화
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

st.title("학교 퀴즈")

# 문제와 보기 표시
for i, no in enumerate(st.session_state["quiz"]):
    st.write(f"{i+1}. {no[0]}")
    st.radio(
        "보기 선택",
        st.session_state["choices"][i],
        key=st.session_state["radio_keys"][i],
        index=None,
        disabled=st.session_state["submitted"]
    )

# 정답 제출
if st.button("정답 제출") and not st.session_state["submitted"]:
    score = 0
    for i, no in enumerate(st.session_state["quiz"]):
        answer_key = st.session_state["radio_keys"][i]
        if st.session_state.get(answer_key) == no[2]:
            score += 1
    st.session_state["score"] = score
    st.session_state["submitted"] = True

# 점수 출력
if st.session_state["submitted"]:
    st.success(f"점수: {st.session_state['score']} / {len(st.session_state['quiz'])}")

# 초기화 (제출 후만 가능)
if st.session_state["submitted"]:
    if st.button("초기화 (다시 시작)"):
        st.session_state.clear()
        st.rerun()
