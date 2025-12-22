#ChatGPT사용

import streamlit as st
import random
import uuid

ACCESS_CODE = "1234"
IMAGE_BASE_URL = "https://raw.githubusercontent.com/Reimu0826/donghoje/main/image/"
IMAGE_WIDTH = 400

if "authorized" not in st.session_state:
    st.session_state["authorized"] = False

st.title("애교심 감별소")

if not st.session_state["authorized"]:
    code = st.text_input("코드를 입력하세요", type="password")
    if st.button("확인"):
        if code == ACCESS_CODE:
            st.session_state["authorized"] = True
            st.rerun()
        else:
            st.error("코드가 틀렸습니다.")
    st.stop()


quiz = [
    ["우리 학교 교목은?", ["느티나무", "소나무"], "느티나무"],
    ["우리 학교 상징 동물은?", ["동호", "토끼"], "동호"],
    ["우리 학교의 교화는?", ["동백꽃", "무궁화"], "동백꽃"],
    ["우리 학교 교가 속 (   )에 들어갈 산은?\n동해에 솟는 해가 지혜를 열고 (   ) 힘찬 정기 혈맥을 이어\n온누리 우려나갈 동호의 별들 진리의 등불 밝혀 큰 뜻 이루세",
     ["백두산", "금정산"], "백두산"],
    ["오늘 점심 메뉴가 아닌 것은?", ["어묵말이", "떡갈비", "치밥"], "떡갈비"],
    ["우리 학교 정문은 어느 쪽?", ["1-1.png", "1-2.png"], "1-1.png"],
    ["우리 학교에 있는 공용실이 아닌 것은?", ["2-1.png", "2-2.png", "2-3.png"], "2-2.png"],
]


if "quiz" not in st.session_state:
    random.shuffle(quiz)
    st.session_state["quiz"] = quiz

if "choices" not in st.session_state:
    st.session_state["choices"] = {}
    for i, q in enumerate(st.session_state["quiz"]):
        shuffled = q[1][:]
        random.shuffle(shuffled)
        st.session_state["choices"][i] = shuffled

if "radio_keys" not in st.session_state:
    st.session_state["radio_keys"] = [
        f"answer_{i}_{uuid.uuid4()}" for i in range(len(quiz))
    ]

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False


for i, no in enumerate(st.session_state["quiz"]):
    st.text(f"{i+1}. {no[0]}")
    options = st.session_state["choices"][i]

    # 이미지 문제
    if all(opt.lower().endswith((".png", ".jpg", ".jpeg")) for opt in options):
        selected = st.radio(
            "",
            options,
            key=st.session_state["radio_keys"][i],
            index=None,
            disabled=st.session_state["submitted"],
            label_visibility="collapsed"
        )

        for opt in options:
            st.image(
                IMAGE_BASE_URL + opt,
                width=IMAGE_WIDTH
            )

    # 텍스트 문제
    else:
        st.radio(
            "",
            options,
            key=st.session_state["radio_keys"][i],
            index=None,
            disabled=st.session_state["submitted"],
            label_visibility="collapsed"
        )


if st.button("정답 제출") and not st.session_state["submitted"]:
    score = 0
    for i, no in enumerate(st.session_state["quiz"]):
        answer_key = st.session_state["radio_keys"][i]
        if st.session_state.get(answer_key) == no[2]:
            score += 1
    st.session_state["score"] = score
    st.session_state["submitted"] = True


if st.session_state["submitted"]:
    st.success(f"점수: {st.session_state['score']} / {len(st.session_state['quiz'])}")


if st.session_state["submitted"]:
    if st.button("초기화 (다시 시작)"):
        st.session_state.clear()
        st.rerun()
