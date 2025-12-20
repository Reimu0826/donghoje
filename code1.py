import streamlit as st
import random
import uuid  # key 재생성을 위한 uuid

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

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

st.title("학교 퀴즈")

#문제 표시
for i, no in enumerate(st.session_state["quiz"]):
    question = no[0]
    st.write(f"{i+1}. {question}")

    # key에 uuid를 붙여서 항상 새로운 컴포넌트로 인식
    st.radio(
        "보기 선택",
        st.session_state["choices"][i],
        key=f"answer_{i}_{uuid.uuid4()}",
        index=None,  # 처음 체크 없음
        disabled=st.session_state["submitted"]
    )

#정답 제출
if st.button("정답 제출") and not st.session_state["submitted"]:
    score = 0
    for i, no in enumerate(st.session_state["quiz"]):
        answer_key = [k for k in st.session_state.keys() if k.startswith(f"answer_{i}_")]
        if answer_key:
            if st.session_state[answer_key[0]] == no[2]:
                score += 1
    st.session_state["score"] = score
    st.session_state["submitted"] = True

#결과 출력
if st.session_state["submitted"]:
    st.success(f"점수: {st.session_state['score']} / {len(st.session_state['quiz'])}")

#초기화 (정답 제출 후에만 표시)
if st.session_state["submitted"]:
    if st.button("초기화 (다시 시작)"):
        st.session_state.clear()
        st.rerun()
