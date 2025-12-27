#ChatGPT사용

import streamlit as st
import random
import uuid

st.set_page_config(
    page_title="남일 사랑 Test",
    page_icon="mark.png"
)

ACCESS_CODE = "1004" 
IMAGE_BASE_URL = "https://raw.githubusercontent.com/Reimu0826/donghoje/main/image/"
IMAGE_WIDTH = 300

if "authorized" not in st.session_state:
    st.session_state["authorized"] = False

st.title("남일 사랑 Test~!! ")

if not st.session_state["authorized"]:
    code = st.text_input(
        "시작하려면 코드를 입력하세요. (코드는 별관2층 컴퓨터실습실에서 확인 가능합니다.)",
        type="password"
    )
    if st.button("확인"):
        if code == ACCESS_CODE:
            st.session_state["authorized"] = True
            st.rerun()
        else:
            st.error("코드가 틀렸습니다.")
    st.stop()


quiz = [
    ["우리 학교 교목은?", ["7-1.png", "7-2.png"], "7-2.png"],
    ["우리 학교를 상징하는 동물은?", ["동호", "토끼"], "동호"],
    ["우리 학교의 교화는?", ["6-1.png", "6-2.png", "6-3.png"], "6-1.png"],
    ["우리 학교 뒷산 이름은?", ["배산", "남산"], "배산"],
    ["우리 학교 바로 옆에 위치한 초등학교는?", ["배산초", "망미초"], "배산초"],
    ["우리 학교에서 심장충격기가 있는 위치는?", ["보건실 앞", "보건실 안", "교무실 앞"], "보건실 앞"],
    ["우리 학교 강당에 없는 것은?", ["농구대", "탁구대", "미니축구대"], "미니축구대"],
    ["우리 학교 교훈은?", ["성실 진리 협동", "성실 협동 책임"], "성실 진리 협동"],
    ["보건실, 교무실, 도서관이 있는 층을 모두 합하면?", ["4", "5", "6"], "5"],
    ["우리 학교 후문에 있는 절 이름은?", ["백룡사", "흑룡사"], "백룡사"],
    ["우리 학교 별관에 있는 실습실 중에서 층이 다른 것은?", ["미술실", "위클래스", "물리실"], "물리실"],
    ["우리 학교 교가 속 (   )에 들어갈 산은?\n동해에 솟는 해가 지혜를 열고 (   ) 힘찬 정기 혈맥을 이어\n온누리 우려나갈 동호의 별들 진리의 등불 밝혀 큰 뜻 이루세",
     ["백두산", "금정산"], "백두산"],
    ["우리 학교 운동부 종목은?", ["검도", "축구", "요트"], "검도"],
    ["우리 학교 정문은?", ["1-1.png", "1-2.png"], "1-1.png"],
    ["우리 학교에 있는 공용실이 아닌 것은?", ["2-1.png", "2-2.png", "2-3.png"], "2-2.png"],
    ["우리 학교 중앙 현관에 있는 동호 석상은?", ["3-1.png", "3-2.png"], "3-2.png"],
    ["우리 학교 교표는?", ["4-1.png", "4-2.png", "4-3.png"], "4-1.png"],
    ["우리 학교 중앙 현관에 있는 외벽 시계는?", ["5-1.png", "5-2.png"], "5-2.png"],
    ["우리 학교에서 볼 수 없는 풍경은?", ["8-1.png", "8-2.png", "8-3.png"], "8-1.png"],
    ["우리 남일고의 학교 생활이 아닌 것은?", ["9-1.png", "9-2.png", "9-3.png"], "9-3.png"]
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


image_label_maps = {}


for i, no in enumerate(st.session_state["quiz"]):
    st.text(f"{i+1}. {no[0]}")
    options = st.session_state["choices"][i]

    if all(opt.lower().endswith((".png", ".jpg", ".jpeg")) for opt in options):
        label_map = {f"{idx+1}번 사진": opt for idx, opt in enumerate(options)}
        image_label_maps[i] = label_map

        st.radio(
            "",
            list(label_map.keys()),
            key=st.session_state["radio_keys"][i],
            index=None,
            disabled=st.session_state["submitted"],
            label_visibility="collapsed"
        )

        for opt in options:
            st.image(IMAGE_BASE_URL + opt, width=IMAGE_WIDTH)

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
    all_correct = True
    correct_count = 0   # ★ 추가

    for i, no in enumerate(st.session_state["quiz"]):
        answer_key = st.session_state["radio_keys"][i]
        user_answer = st.session_state.get(answer_key)

        if i in image_label_maps and user_answer:
            user_answer = image_label_maps[i][user_answer]

        if user_answer == no[2]:
            correct_count += 1   # ★ 추가
        else:
            all_correct = False

    st.session_state["all_correct"] = all_correct
    st.session_state["correct_count"] = correct_count   # ★ 추가
    st.session_state["submitted"] = True


if st.session_state["submitted"]:
    if st.session_state["all_correct"]:
        st.success("축하합니다, 별관2층 컴퓨터실습실에서 상품을 받아가세요!")
    else:
        st.warning("아쉽네요, 우리 학교에 대해 더 알아봅시다!")

    # ★ 추가: 정답 개수 출력
    st.info(
        f"정답 개수: {st.session_state['correct_count']} / {len(st.session_state['quiz'])}"
    )


if st.session_state["submitted"]:
    if st.button("초기화 (다시 시작)"):
        st.session_state.clear()
        st.rerun()
