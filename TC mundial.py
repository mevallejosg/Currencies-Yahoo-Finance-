#!/usr/bin/env python
# coding: utf-8

# In[51]:


# Importamos las librerías necesarias para el trabajo
import yahoo_finance as yahoo
import numpy as np
import pandas as pd
import datetime
from pandas_datareader import data


# In[52]:


# Definimos las fechas que vamos a trabajar
start = datetime.datetime(2018,1,1)
end = datetime.datetime(2022,10,24)


# In[53]:


# Colocamos las monedas de interés (principales economías del mundo)
list_of_tickers = ['USDAUD=X',,'USDARS=X','USDBRL=X','USDCAD=X','^TNX','USDCNY=X','USDCLP=X','USDCOP=X','USDHKD=X','USDHUF=X','USDIDR=X','USDINR=X','USDILS=X','USDJPY=X','USDKRW=X','USDMYR=X','USDMXN=X','USDPEN=X','USDPHP=X','USDPLN=X','USDCZK=X','USDRON=X','USDRUB=X','USDSAR=X','USDSGD=X','USDZAR=X','USDSEK=X','USDCHF=X','USDTWD=X','USDTHB=X','USDTRY=X','USDGBP=X','USDVND=X','USDEUR=X']


# In[54]:


# Incorporamos lo predefinido para crear un dataframe
currencies = data.DataReader(list_of_tickers, 'yahoo', start, end)['Adj Close']


# In[55]:


currencies


# In[56]:


# Exportamos a excel
currencies.to_excel('TC mundial.xlsx', sheet_name='Monedas', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, inf_rep='inf', freeze_panes=None, storage_options=None)


# In[ ]:




