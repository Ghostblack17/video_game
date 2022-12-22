import streamlit as st
from tkinter.tix import COLUMN
from pyparsing import empty


st.set_page_config(layout="wide")


def run_home_app() :
    
    st.markdown("<h5 style='text-align: center; '>콘솔게임기 Market Analysis</h1>", unsafe_allow_html=True)
    
    img_url = 'https://images.nintendolife.com/8d9f4fa15395f/1280x720.jpg'
    st.image(img_url)
    
    st.text('전세계 게임시장 분석 내용입니다.')
    st.text('상세 내용을 보시려면 화면 왼쪽에 있는 해당 국가 탭으로 이동해주세요.')
    
    tab1, tab2, tab3 = st.tabs(["Playstation", "Nintendo", "Xbox"])

    with tab1:
        st.text('플레이스테이션 소개 영상')
        st.video("https://youtu.be/eECNpQ67JRo")
        st.video("https://youtu.be/iFtvSkL13Gg")

    with tab2:
        st.text('닌텐도 스위치 소개 영상')
        st.video("https://youtu.be/4mHq6Y7JSmg")
        st.video("https://youtu.be/WlbIxRUpFMM")

    with tab3:
        st.text('XBOX 소개 영상')
        st.video("https://youtu.be/0tUqIHwHDEc")
        st.video("https://youtu.be/R-bi-tcamBI")
