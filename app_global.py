import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px


def run_global_app() :
        
        st.subheader('글로벌 판매량 분석')
        img_url = 'https://img.freepik.com/premium-vector/blank-white-world-map-isolated-blue-background-world-map-vector-template-website-infographics-design-flat-earth-world-map-illustration_157943-728.jpg?w=2000'
        st.image(img_url)
        
        df = pd.read_csv('data/vgsales.csv')
        
        st.subheader('글로벌 역대 플랫폼 판매량')
        df_platform = df.groupby('Platform', as_index=False)['Global_Sales'].sum()
        if st.button('글로벌 데이터프레임 보기') :
            st.text('많이 팔린 플랫폼 순서대로 정렬')
            st.dataframe(df_platform.nlargest(31,'Global_Sales') )
            
        column_list = df.columns[6:]
        
        
        df_sorted = df.sort_values('Global_Sales', ascending=False )
        fig2 = px.bar(df_sorted, x='Platform', y='Global_Sales')
        fig2.update_layout( barmode = 'stack' , xaxis = { 'categoryorder' : 'total descending' } )
        st.plotly_chart(fig2)
        st.text('글로벌은 소니의 플레이스테이션2가 가장 많이 판매되었습니다.')
            
            
        fig4 = px.pie(df, 'Platform', 'Global_Sales', title='글로벌 플랫폼 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
        fig4.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig4)
        
            
        fig5 = px.pie(df, 'Genre', 'Global_Sales', title='글로벌 게임장르 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
        fig5.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig5)
        
        
        fig6 = px.pie(df, 'Publisher', 'Global_Sales', title='글로벌 게임 퍼블리싱 역대 판매량', hole = 0.4)
        fig6.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig6)