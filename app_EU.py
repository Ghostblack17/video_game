import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px


def run_EU_app() :
        
        st.subheader('유럽 판매량 분석')
        img_url = 'https://gisgeography.com/wp-content/uploads/2020/11/Europe-Map-Feature.jpg'
        st.image(img_url)
        
        df = pd.read_csv('data/vgsales.csv')
        
        df_platform = df.groupby('Platform', as_index=False)['EU_Sales'].sum()
        st.subheader('유럽 역대 플랫폼 판매량')
        if st.button('데이터프레임 보기') :
            st.text('많이 팔린 기기 순서대로 정렬')
            st.dataframe(df_platform.nlargest(31,'EU_Sales') )
        
        
        st.subheader('유럽 역대 플랫폼 판매량')
        df_sorted = df.sort_values('EU_Sales', ascending=False)
        fig2 = px.bar(df_sorted, x='Platform', y='EU_Sales')
        st.plotly_chart(fig2)
        
        
        fig4 = px.pie(df, 'Platform', 'EU_Sales', title='유럽 플랫폼 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
        fig4.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig4)
 
 
        fig5 = px.pie(df, 'Genre', 'EU_Sales', title='유럽 게임장르 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
        fig5.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig5)
        
        
        
        fig6 = px.pie(df, 'Publisher', 'EU_Sales', title='유럽내 게임 퍼블리싱 역대 판매량', hole = 0.4)
        fig6.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig6)