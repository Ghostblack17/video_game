import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px


def run_JP_app() :
        
        st.subheader('일본 판매량 분석')
        img_url = 'https://static.vecteezy.com/system/resources/previews/003/249/618/original/simple-black-map-of-japan-isolated-on-white-background-free-vector.jpg'
        st.image(img_url)
        
        df = pd.read_csv('data/vgsales.csv')
        
        df_platform = df.groupby('Platform', as_index=False)['JP_Sales'].sum()
        st.subheader('일본 역대 플랫폼 판매량')
        if st.button('데이터프레임 보기') :
            st.text('많이 팔린 기기 순서대로 정렬')
            st.dataframe(df_platform.nlargest(31,'JP_Sales') )
        
        
        st.subheader('일본 역대 플랫폼 판매량 차트')
        df_sorted = df.sort_values('JP_Sales', ascending=False)
        fig2 = px.bar(df_sorted, x='Platform', y='JP_Sales')
        fig2.update_layout( barmode = 'stack' , xaxis = { 'categoryorder' : 'total descending' } )
        st.plotly_chart(fig2)
        st.text('일본 기준으로 닌텐도 DS가 가장 많이 판매되었습니다.')
        
        
        fig4 = px.pie(df, 'Platform', 'JP_Sales', title='일본 역대 플랫폼 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
        fig4.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig4)
        
            
        fig5 = px.pie(df, 'Genre', 'JP_Sales', title='일본 게임장르 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
        fig5.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig5)
        
        
        fig6 = px.pie(df, 'Publisher', 'JP_Sales', title='일본 게임 퍼블리싱 역대 판매량', hole = 0.4)
        fig6.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig6)