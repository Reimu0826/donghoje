#ChatGPT사용

import streamlit as st
import random
import uuid

ACCESS_CODE = "1234"
IMAGE_BASE_URL = "https://raw.githubusercontent.com/Reimu0826/donghoje/main/image/"
IMAGE_WIDTH = 300

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
    ["오늘 점심 메뉴가 아닌 것은?", ["어묵말이", "]()]()
