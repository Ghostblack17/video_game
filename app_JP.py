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
        file = st.file_uploader('CSV파일 업로드', type=['csv'])
        if file is not None :
            df = pd.read_csv(file)
            st.dataframe(df)
        
            column_list = df.columns
            selected_columns = st.multiselect('살펴보실 컬럼을 선택해주세요', column_list)
            X = df[selected_columns]
            
            
            st.subheader('일본 역대 플랫폼 판매량')
            df_sorted = df.sort_values('JP_Sales', ascending=False)
            fig2 = px.bar(df_sorted, x='Platform', y='JP_Sales')
            st.plotly_chart(fig2)
            
            
            fig4 = px.pie(df, 'Platform', 'JP_Sales', title='일본 플랫폼 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
            fig4.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig4)
        
            
            fig5 = px.pie(df, 'Genre', 'JP_Sales', title='일본게임장르 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
            fig5.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig5)
            
            fig6 = px.pie(df, 'Publisher', 'JP_Sales', title='일본 퍼블리셔 역대 판매량', hole = 0.4)
            fig6.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig6)