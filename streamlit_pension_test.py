#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[27]:


import streamlit as st


# # 

# In[28]:


st.title("인모스트 재무설계 계산기")


# In[29]:


st.subheader("고객 기초정보")


# In[30]:


import streamlit as st

[col1, col2, col3] = st.columns(3, gap="medium")

# 이름 입력
with col1:
    name = st.text_input("이름", key='name_input')

# 성별 선택
with col2:
    sex = ["남성", "여성"]
    client_sex = st.selectbox("성별", sex, key='sex_selectbox')
    
# 담당관리자 선택
with col3:
    partner = ["박배혁", "한세호"]
    client_partner = st.selectbox("담당 관리자", partner, key='partner_selectbox')




# In[37]:


st.markdown("---")


# In[38]:


st.subheader("고객 은퇴정보")


# In[72]:


[col1, col2] = st.columns(2, gap="medium")

with col1:
    # 현재 연령 입력
    age = st.number_input("현재 연령", step=1, format="%d", key="age_input")
    st.write(f"{age}세")
    
    st.write("")
    
    # 월 희망 생활비
    monthly_expense = st.number_input("월 희망 생활비", step=1, format="%d", key="monthly_expense_input")
    st.write(f"{monthly_expense:,.0f}원")

with col2:
    # 은퇴 예상 연령 입력
    retire_age = st.number_input("은퇴 예상 연령", step=1, format="%d", key="retire_age_input")
    st.write(f"{retire_age}세")
    
    st.write("")
    
    # 희망 인출 기간
    withdrawal_period = st.number_input("인출기간 (년)", min_value=1, format="%d", key="withdrawal_period_input")
    st.write(f"{withdrawal_period}년")



# In[75]:


# 연 희망 생활비
st.text("연 생활비")
yearly_expense = monthly_expense *12
st.write(f"{yearly_expense:,.0f}원")


# In[ ]:




