import streamlit as st


def run_home_app() :
    st.subheader('닌텐도 스위치 & 플레이스테이션 전세계 게임시장')
    
    img_url = 'https://cdn.mos.cms.futurecdn.net/JpW3zxwNtfR439QHsvVFt5.jpg'
    st.image(img_url)
    
    st.text('닌텐도 스위치 관련 영상')
    st.video("https://youtu.be/4mHq6Y7JSmg")
    st.video("https://youtu.be/WlbIxRUpFMM")
    
    st.text('플레이스테이션 관련 영상')
    st.video("https://youtu.be/eECNpQ67JRo")
    st.video("https://youtu.be/iFtvSkL13Gg")

    st.text('게임시장 분석 내용입니다.')
    st.text('자세한 내용은 화면 왼쪽에 있는 사이드바 해당관련 탭으로 이동해주세요.')