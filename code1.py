#ChatGPT사용

import streamlit as st
import random
import uuid

quiz = [
    ["우리 학교 교목은?", ["느티나무", "소나무"], "느티나무"],
    ["우리 학교 상징 동물은?", ["동호", "토끼"], "동호"],
    ["우리 학교의 교화는?", ["동백꽃", "무궁화"], "동백꽃"],
    ["우리 학교 교가 속 (   )에 들어갈 산은? \n 동해에 솟는 해가 지혜를 열고 (   ) 힘찬 정기 혈맥을 이어 \n 온누리 우려나갈 동호의 별들 진리의 등불 밝혀 큰 뜻 이루세", ["백두산", "금정산"], "백두산"],
    ["오늘 점심 메뉴가 아닌 것은?",["어묵말이","떡갈비","치밥"],"떡갈"],
    ["우리 학교 정문은 어느 쪽?", ["1-1.png", "1-2.png"], "1-1.png"],
    ["우리 학교에 있는 공용실이 아닌 것은?", ["2-1.png", "2-2.png","2-3.png"], "2-2.png"],
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

st.title("애교심 감별소")  # 앱 제목

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
