import streamlit as st
from app_home import run_home_app

def main() :
    
    st.title('비디오게임 게임시장 분석')
    
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)
    
    if choice == 'Home' :
        run_home_app()


if __name__ == '__main__' :
    main()