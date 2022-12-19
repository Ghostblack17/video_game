import streamlit as st
from app_home import run_home_app
from app_global import run_global_app
from app_NA import run_NA_app
from app_EU import run_EU_app
from app_JP import run_JP_app
from app_other import run_other_app


def main() :
    
    st.title('비디오게임 게임시장 분석')
    
    menu = ['Home','Global_Sales', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
    choice = st.sidebar.selectbox('메뉴', menu)
    
    if choice == 'Home' :
        run_home_app()
        
    elif choice == 'Global_Sales' :
        run_global_app()
    
    elif choice == 'NA_Sales' :
        run_NA_app()
        
    elif choice == 'EU_Sales' :
        run_EU_app()
        
    elif choice == 'JP_Sales' :
        run_JP_app()
    
    elif choice == 'Other_Sales' :
        run_other_app()


if __name__ == '__main__' :
    main()