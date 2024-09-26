import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')
st.header('Real-Time/Live DataScience Dashboard')
data=pd.read_csv('bank.csv')
with st.expander('show data'):
    st.write(data)
jobs=data['job'].unique()
with st.expander('show jobs'):
    st.write(jobs)
option=st.selectbox('select a job',jobs)
df = data[data['job']==option]
st.write(df)
average=df['age'].mean()
st.write(round(average))

married_count=df['marital'].value_counts()['married']

average_bank_balance=df['balance'].mean()

col1,col2,col3=st.columns(3)
with col1:
   st.metric(label='average age',value=round(average))
with col2:
    st.metric(label='married count',value=(married_count))
with col3:
    st.metric(label='average bank balance',value=round(average_bank_balance))
fig=px.density_heatmap(data_frame=df,x='marital',y='age')
#st.plotly_chart(fig)
fig1=px.histogram(data_frame=df,x='age')
#st.plotly_chart(fig1)
col4,col5=st.columns(2)
with col4:
    st.plotly_chart(fig)
with col5:
    st.plotly_chart(fig1)

