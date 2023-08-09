#!/usr/bin/env python
# coding: utf-8

# In[18]:


#pip install streamlit
# streamlit hello       #이 코드는 쥬피터에서 실행하면 안됨. CMD에서 입력해야 함.
#pip install streamlit_jupyter


# In[7]:


import streamlit as st
from streamlit_jupyter import StreamlitPatcher, tqdm

StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers
import pandas as pd


# In[8]:


st.title('Inmost Daily Performance')


# In[9]:


from datetime import date, time, datetime, timedelta
today = date.today()
yesterday = date.today() - timedelta(3)


# In[12]:


st.write(today)


# In[15]:


df = pd.read_excel("C:/Users/advis/Desktop/데일리모니터링 (version 2).xlsx")


# In[16]:


from PIL import Image


# In[21]:


st.subheader("대표MP")
image_file = 'C:/Users/advis/Pictures/Screenshots/스크린샷 2023-08-09 112049.png'
image_local = Image.open(image_file)
st.image(image_local)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




