import streamlit as st


def run_home_app() :
    st.subheader('콘솔게임기기 전세계 게임시장')
    
    img_url = 'https://images.nintendolife.com/8d9f4fa15395f/1280x720.jpg'
    st.image(img_url)
    
    st.text('플레이스테이션 소개 영상')
    st.video("https://youtu.be/eECNpQ67JRo")
    st.video("https://youtu.be/iFtvSkL13Gg")
    
    
    st.text('닌텐도 스위치 소개 영상')
    st.video("https://youtu.be/4mHq6Y7JSmg")
    st.video("https://youtu.be/WlbIxRUpFMM")
    
    st.text('XBOX 소개 영상')
    st.video("https://youtu.be/0tUqIHwHDEc")


    st.text('전세계 게임시장 분석 내용입니다.')
    st.text('자세한 내용을 보시려면 화면 왼쪽에 있는 해당 국가 탭으로 이동해주세요.')