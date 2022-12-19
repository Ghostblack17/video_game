import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px


def run_NA_app() :
        
        st.subheader('북미 판매량 분석')
        img_url = 'https://gisgeography.com/wp-content/uploads/2020/11/North-America-Map-Feature.png'
        st.image(img_url)
        file = st.file_uploader('CSV파일 업로드', type=['csv'])
        if file is not None :
            df = pd.read_csv(file)
            st.dataframe(df)
        
            column_list = df.columns
            selected_columns = st.multiselect('살펴보실 컬럼을 선택해주세요', column_list)
            X = df[selected_columns]
            
            
            st.subheader('북미 역대 플랫폼 판매량')
            df_sorted = df.sort_values('NA_Sales', ascending=False)
            fig2 = px.bar(df_sorted, x='Platform', y='NA_Sales')
            st.plotly_chart(fig2)
            
            
            fig4 = px.pie(df, 'Platform', 'NA_Sales', title='북미 플랫폼 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
            fig4.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig4)
        
            
            fig5 = px.pie(df, 'Genre', 'NA_Sales', title='북미 게임장르 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
            fig5.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig5)
            
            fig6 = px.pie(df, 'Publisher', 'NA_Sales', title='북미 퍼블리셔 역대 판매량', hole = 0.4)
            fig6.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig6)