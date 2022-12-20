import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px



def run_total_app() :
        st.subheader('총 판매량 전체 살펴보기')
        st.markdown("![Alt Text](https://i.pinimg.com/originals/7c/9c/f4/7c9cf4399ad9689edf2df2e1eb763796.gif)")

        file = st.file_uploader('분석 CSV파일을 업로드시켜주세요.', type=['csv'])
        if file is not None :
            df = pd.read_csv(file)
            st.dataframe(df)
            
            column_list = df.columns
            selected_columns = st.multiselect('살펴보실 컬럼을 선택해주세요.', column_list)
            X = df[selected_columns]
            st.dataframe(X)
            
            
        column_list2 = df.columns[6:]
        fig1 = plt.figure(figsize=(12,10))
        selected_list = st.multiselect('상관분석을 해보고싶은 컬럼을 선택하세요.', column_list2)
        cor = df[selected_list].corr()
            
        if len(selected_list) >= 2 :
            sb.heatmap(data = cor, annot= True, cmap=plt.cm.CMRmap_r)
            st.pyplot(fig1)