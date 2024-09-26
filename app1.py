import streamlit as st
import plotly.express as px
import pandas as pd
st.set_page_config(layout='wide')
st.header('Dashboard of TB by WHO')
data=pd.read_csv('TB_Burden_Country.csv')
st.write(data)
options=st.sidebar.selectbox('Select Year',data['Year'].unique())
df=data[data['Year']==options]
st.write(df)
print(df.columns)
col1,col2=st.columns(2)

with col1:               
 st.metric('Death Rate',df['Estimated number of deaths from TB (all forms, excluding HIV)'].size)
with col2:
 st.metric('Mortality Rate',df['Estimated mortality of TB cases who are HIV-positive, per 100 000 population'].size)

col3,col4=st.columns(2)

with col3:
    st.subheader('Death rate Chart')
    fig=px.bar(data_frame=df.iloc[:10],x='Estimated number of deaths from TB (all forms, excluding HIV)',y='Country or territory name')
    st.plotly_chart(fig)
with col4:
    st.subheader('Mortality rate Chart')
    fig=px.bar(data_frame=df.iloc[:10],x='Estimated mortality of TB cases who are HIV-positive, per 100 000 population',y='Country or territory name')
    st.plotly_chart(fig)

fig=px.choropleth(locations=df['ISO 3-character country/territory code'],color=df['Estimated prevalence of TB (all forms)'])
st.write(fig)

options1=st.sidebar.selectbox('Select Country',data['Country or territory name'].unique())
df1=data[data['Country or territory name']==options1]
st.write(df1)

col5,col6=st.columns(2)

with col5:
   st.metric('Number of cases',df1['Estimated number of incident cases (all forms)'].size)
with col6:
   st.metric('Number of death',df1['Estimated number of deaths from TB in people who are HIV-positive'].size)

col7,col8=st.columns(2)
  
with col7:
    st.subheader('chart of no.of cases')
    fig=px.bar(data_frame=df,x='Estimated number of incident cases (all forms)',y='Country or territory name')
    st.write(fig)
with col8:
    st.subheader('chart of no.of deaths from TB whose HIV positive')
    fig=px.bar(data_frame=df,x='Estimated number of deaths from TB in people who are HIV-positive',y='Country or territory name')
    st.write(fig)

