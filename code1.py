import streamlit as st
import random

quiz = [
    ["교목은?", ["느티나무", "소나무"], "느티나무"],
    ["상징 동물은?", ["동호", "토끼"], "동호"],
    ["교화는?", ["동백꽃", "무궁화"], "동백꽃"],
    ["빈 칸에 들어갈 산은?", ["백두산", "금정산"], "백두산"],
    ["우리 학교에 있는 석상은?", ["image01.png", "image02.png"], "image01.png"]
]

# 최초 1회만 문제 + 보기 섞기
if "quiz" not in st.session_state:
    random.shuffle(quiz)
    st.session_state["quiz"] = quiz

    st.session_state["choices"] = {}
    for i, q in enumerate(quiz):
        shuffled = q[1][:]
        random.shuffle(shuffled)
        st.session_state["choices"][i] = shuffled

    st.session_state["submitted"] = False

st.title("학교 퀴즈")

# 문제 표시
for i, no in enumerate(st.session_state["quiz"]):
    question, _, correct = no
    st.write(f"{i+1}. {question}")

    st.radio(
        "보기 선택",
        st.session_state["choices"][i],  # ✅ 수정된 부분
        key=f"answer_{i}",
        disabled=st.session_state["submitted"]
    )

# 정답 제출
if st.button("정답 제출") and not st.session_state["submitted"]:
    score = 0
    for i, no in enumerate(st.session_state["quiz"]):
        if st.session_state.get(f"answer_{i}") == no[2]:
            score += 1

    st.session_state["score"] = score
    st.session_state["submitted"] = True

# 결과 출력
if st.session_state["submitted"]:
    st.success(f"점수: {st.session_state['score']} / {len(st.session_state['quiz'])}")

# 초기화
if st.button("초기화 (다시 시작)"):
    st.session_state.clear()
    st.experimental_rerun()
