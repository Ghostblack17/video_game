import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
import seaborn as sb
import plotly.express as px



def run_total_app() :
    

        st.markdown("<h4 style='text-align: center; '>총 판매량 전체 살펴보기</h1>", unsafe_allow_html=True)
        st.markdown("![Alt Text](https://i.pinimg.com/originals/7c/9c/f4/7c9cf4399ad9689edf2df2e1eb763796.gif)")
        
        df = pd.read_csv('data/vgsales.csv', index_col=0)
        
        if st.button('전체 데이터프레임 살펴보기') :
            st.dataframe(df)
        
        
        
            
        column_list = df.columns
        selected_columns = st.multiselect('살펴보실 컬럼을 선택해주세요.', column_list)
        X = df[selected_columns]
        st.dataframe(X)
            
        
        
        st.text('각 국가별 시장영향 끼치는 기준표')
        total_sales = pd.DataFrame({'Country':['NA','EU','JP','Other'],'Sales':[sum(df['NA_Sales']),sum(df['EU_Sales']),
                                                                        sum(df['JP_Sales']),sum(df['Other_Sales'])]},index = ['NA','EU','JP','Other'])

        total_sales['Percentages'] = total_sales['Sales'] / sum(total_sales['Sales']) * 100
        total_sales.sort_values(by = 'Percentages',ascending = False, inplace = True)
        st.dataframe(total_sales)
    
        
        fig = plt.figure(facecolor='whitesmoke')
        axes1 = fig.add_axes([0, 0, 1, 1])
        axes2 = fig.add_axes([0.7, 0, 1, 1])
        axes3 = fig.add_axes([1.4, 0, 1, 1])
        axes4 = fig.add_axes([2.1, 0, 1, 1])

        axes1.pie([total_sales['Percentages'][0], 100-total_sales['Percentages'][0]], startangle=180,
         colors=['royalblue', 'white'])
        axes1.text(-0.27, -0.85,f"{round(total_sales['Percentages'][0],2)}%", fontweight='bold', fontsize=16)
        axes1.text(-0.5, 1.3, 'North America', fontweight='bold', fontsize=16)

        axes2.pie([total_sales['Percentages'][1], 100-total_sales['Percentages'][1]], startangle=-4,
         colors=['royalblue', 'white'])
        axes2.text(0.26, 0.355, f"{round(total_sales['Percentages'][1],2)}%", fontweight='bold', fontsize=16)
        axes2.text(-0.3, 1.3, 'Europe', fontweight='bold', fontsize=16)

        axes3.pie([total_sales['Percentages'][2], 100-total_sales['Percentages'][2]], startangle=95,
         colors=['royalblue', 'white'])
        axes3.text(-0.62, 0.5, f"{round(total_sales['Percentages'][2],2)}%", fontweight='bold', fontsize=16)
        axes3.text(-0.25, 1.3, 'Japan', fontweight='bold', fontsize=16)

        axes4.pie([total_sales['Percentages'][3], 100-total_sales['Percentages'][3]], startangle=130,
         colors=['royalblue', 'white'])
        axes4.text(-0.77, 0.3, f"{round(total_sales['Percentages'][3],2)}%", fontweight='bold', fontsize=16)
        axes4.text(-0.5, 1.3, 'Other countries', fontweight='bold', fontsize=16)

        axes2.text(-0.3,1.8, '국가별 판매량 차지기준', fontweight='bold', color='royalblue', fontsize=24)
        st.pyplot(fig)
        
        
        
        sales_by_na= df.groupby('Year').NA_Sales.sum()
        sales_by_eu= df.groupby('Year').EU_Sales.sum()
        sales_by_jp= df.groupby('Year').JP_Sales.sum()
        sales_by_other= df.groupby('Year').Other_Sales.sum()

        fig5 = px.line(y=[sales_by_na.values,sales_by_eu.values,sales_by_jp.values,sales_by_other.values],x=sales_by_na.index,markers=True,title='판매 국가 비율')
        newnames = {'wide_variable_0':'NA','wide_variable_1':'Europe','wide_variable_2':'Japan','wide_variable_3':'Other'}
        fig5.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )
        st.plotly_chart(fig5)
        st.text('북미가 가장 높다.')
        

        # 장르 순위
        group_pub_global = df.groupby('Publisher').sum()['Global_Sales'].reset_index()
        group_pub_global['Percentages'] = round(group_pub_global['Global_Sales'] / sum(group_pub_global['Global_Sales']) * 100,2)
        group_pub_global.sort_values(by = "Percentages",inplace = True, ascending = False)

        top_10_group_pub_global = group_pub_global.head(10)
        top_10_group_pub_global.sort_values(by = "Percentages",inplace = True)

        fig1 = plt.figure(facecolor='whitesmoke')
        axes1 = fig1.add_axes([0, 0, 1.5, 1.5])

        axes1.barh(width=100, y=top_10_group_pub_global['Publisher'], color='white')
        axes1.barh(width=top_10_group_pub_global['Percentages'], y=top_10_group_pub_global['Publisher'], color='royalblue')
        axes1.text(1, 10, '글로벌 top 10 publishers', color='royalblue', fontsize=22, fontweight='bold')
        axes1.set_facecolor('whitesmoke')
        axes1.set_xlabel('Percent(%)', fontsize=18, color='black')
        axes1.set_ylabel('Publishers', fontsize=18, color='black')

        for p in axes1.patches[10:]:
            width = p.get_width()
            height = p.get_height()
            x, y = p.get_xy() 
            axes1.annotate('{:.2f}%'.format(width), (5+ width, y + height*0.45), ha='center', fontsize=14, color='black')
        st.pyplot(fig1)
        st.text('닌텐도가 가장 인기가 많다.')
        
        
        st.subheader('국가별 장르 판매 비율')
        genre_jp= df.groupby('Genre').JP_Sales.sum()
        genre_eu= df.groupby('Genre').EU_Sales.sum()
        genre_na= df.groupby('Genre').NA_Sales.sum()
        genre_other=df.groupby('Genre').Other_Sales.sum()

        fig2 = px.line(x=genre_eu.index,y=[genre_jp.values,genre_eu.values,genre_na.values,genre_other.values],markers=True)
        newnames = {'wide_variable_0':'Japan','wide_variable_1':'Europe','wide_variable_2':'North America','wide_variable_3':'Other'}
        fig2.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )
        st.plotly_chart(fig2)
        
        
        st.subheader('판매량 Pairplot 살펴보기')
        if st.button('Pairplot 보기') :
            data_pair = df.loc[:,['Year','Platform','Genre','NA_Sales', 'EU_Sales', 'Other_Sales']]
            fig3 = sb.pairplot(data_pair,hue = 'Platform')
            st.pyplot(fig3)

        column_list2 = df.columns[6:]
        fig4 = plt.figure(figsize=(12,10))
        selected_list = st.multiselect('상관분석을 해보실 국가 컬럼을 선택해주세요.', column_list2)
        cor = df[selected_list].corr()
            
        if len(selected_list) >= 2 :
            sb.heatmap(data = cor, annot= True, cmap=plt.cm.CMRmap_r)
            st.pyplot(fig4)