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
        
        file = st.file_uploader('CSV파일 업로드', type=['csv'])
        if file is not None :
            df = pd.read_csv(file)
            st.dataframe(df)
        
            column_list = df.columns
            selected_columns = st.multiselect('살펴보실 컬럼을 선택해주세요', column_list)
            X = df[selected_columns]
            
        
            st.dataframe(X)
            st.subheader('기본 통계 데이터')
            st.dataframe( df.describe() )    
            
            
            st.subheader('글로벌 역대 플랫폼 판매량')
            df_sorted = df.sort_values('Global_Sales', ascending=False)
            fig2 = px.bar(df_sorted, x='Platform', y='Global_Sales')
            st.plotly_chart(fig2)
            
            
            fig4 = px.pie(df, 'Platform', 'Global_Sales', title='글로벌 플랫폼 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
            fig4.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig4)
        
            
            fig5 = px.pie(df, 'Genre', 'Global_Sales', title='글로벌 게임장르 역대 판매량', color_discrete_sequence = px.colors.sequential.Viridis,
             hole = 0.4)
            fig5.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig5)
            
            fig6 = px.pie(df, 'Publisher', 'Global_Sales', title='글로벌 퍼블리셔 역대 판매량', hole = 0.4)
            fig6.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig6)
            
            fig7 = plt.figure(figsize=(12,10))
            selected_list = st.multiselect('상관분석을 해보고싶은 컬럼을 선택하세요.', column_list)
            cor = df[selected_list].corr()
            
            if len(selected_list) >= 2 :
                sb.heatmap(data = cor, annot= True, cmap=plt.cm.CMRmap_r)
                st.pyplot(fig7)