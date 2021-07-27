#!/usr/bin/env python
# coding: utf-8

# # Sidharth Jahagirdar - ssj180009@utdallas.edu / 6822834728

# # Case Study 2

# # Importing Libraries and dataset

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df=pd.read_csv(r"C:\Users\sidha\Desktop\Stout Case Study\Case Study 2\casestudy.csv")


# In[3]:


df.head()


# # Insights 2017

# <b>Total revenue for year 2017 = 31417495.03

# In[4]:


rev2017=round(sum(df[df['year']==2017]['net_revenue']),2)
rev2017


# <b>New customer revenue for year 2017 = 28676607.64

# In[5]:


all2017=list(df[df['year']==2017]['customer_email'])
prev2017=list(df[df['year']<2017]['customer_email'])
new2017=set(all2017)-set(prev2017)
new2017=list(new2017)
revNew2017=round(sum(df.loc[(df['year']==2017)&(df['customer_email'].isin(new2017))]['net_revenue']),2)
revNew2017


# <b>Existing Customer Growth for year 2017 = -4744565.19<br>
#     There is a decline in revenue from existing customer

# In[6]:


revEx2017=round(rev2017-revNew2017,2)
revEx2017
all2016=list(df[df['year']==2016]['customer_email'])
prev2016=list(df[df['year']<2016]['customer_email'])
new2016=set(all2016)-set(prev2016)
new2016=list(new2016)
revNew2016=round(sum(df.loc[(df['year']==2016)&(df['customer_email'].isin(new2016))]['net_revenue']),2)
revNew2016
rev2016=round(sum(df[df['year']==2016]['net_revenue']),2)
revEx2016=round(rev2016-revNew2016,2)
round(revEx2017-revEx2016,2)


# <b>Revenue lost from attrition = 23110294.94

# Assumption -<br>
# eg. There are 100 customers in 2015, 80 of them carryforward to 2016, 20 of them opt out the service, 30 new customers join the service in 2016. The loss of revenue due to attrition will be the loss of revenue due to the customers who are quitting(20 customers in this case).

# In[7]:


lost2017=list(set(all2016)-set(all2017))
revLost2017=round(sum(df.loc[(df['year']==2016)&(df['customer_email'].isin(lost2017))]['net_revenue']),2)
revLost2017


# <b>Existing Customer Revenue Current Year(2017) =2740887.39

# In[8]:


revEx2017


# <b>Existing Customer Revenue Prior Year(2016)=7485452.58

# In[9]:


revEx2016


# <b>Total Customers Current Year(2017)=249987

# In[10]:


len(set(list(df[df['year']==2017]['customer_email'])))


# <b>Total Customers Previous Year(2016)=204646

# In[11]:


len(set(list(df[df['year']==2016]['customer_email'])))


# <b>New Customers(2017)=228262

# In[12]:


len(new2017)


# <b>Lost Customers(2017)=183687

# In[13]:


len(list(set(all2016)-set(all2017)))


# # Insights 2016 

# <b>Total revenue for year 2016=25730943.59

# In[14]:


rev2016


# <b>New Customer Revenue for year 2016=18245491.01

# In[15]:


revNew2016


# <b>Existing Customer Growth for year 2016

# Insufficient data, to calculate 2016 existing customer growth, one would need a list of existing customers in 2015.
# To get the existing customers in 2015, we would need data for 2014 and prior, which falls out of the scope of the dataset

# <b>Revenue lost from attrition=21571632.07

# Assumption -<br>
# eg. There are 100 customers in 2015, 80 of them carryforward to 2016, 20 of them opt out the service, 30 new customers join the service in 2016. The loss of revenue due to attrition will be the loss of revenue due attrition will be the loss of revenue due to the customers who are quitting(20 customers in this case).

# In[16]:


all2015=list(df[df['year']==2015]['customer_email'])
lost2016=list(set(all2015)-set(all2016))
revLost2016=round(sum(df.loc[(df['year']==2015)&(df['customer_email'].isin(lost2016))]['net_revenue']),2)
revLost2016


# <b>Existing Customer Revenue for current year(2016)=7485452.58

# In[17]:


revEx2016


# <b>Existing Customer Revenue for Prior Year(2015)

# Insufficient data, to calculate existing customer revenue for 2015, one would need to get the existing customers in 2015, for which we would need data for 2014 and prior, which falls out of the scope of the dataset

# <b>Total Customers Current Year(2016)=204646

# In[18]:


len(set(list(df[df['year']==2016]['customer_email'])))


# <b>Total Customers Previous Year=231294

# In[19]:


len(set(list(df[df['year']==2015]['customer_email'])))


# <b>New Customers=145062

# In[20]:


len(new2016)


# <b>Lost Customers(2016)=171710

# In[21]:


all2015=list(df[df['year']==2015]['customer_email'])
len(list(set(all2015)-set(all2016)))


# # Insights 2015

# <b>Total revenue for year 2015=29036749.19

# In[22]:


rev2015=round(sum(df[df['year']==2015]['net_revenue']),2)
rev2015


# <b>New Customer Revenue for the year 2015

# Insufficient data, to calculate the revenue from new customers in 2015, we would need a list of new customers in 2015. To get the list of new customers in 2015, we will need access to data from 2014 and before, which falls out of the scope of the dataset.

# <b>Existing Customer Growth for the year 2015

# Insufficient data, to calculate the existing customer growth for the year 2015, we would need a list of existing customers in 2015. To get the list of existing customers in 2015, we will need access to data from 2014 and before, which falls out of the scope of the dataset.

# <b>Revenue lost from attrition

# Insufficient data, to calculate the revenue loss due to attrition in 2015, we would need a list of lost customers in 2015. To get the list of lost customers in 2015, we will need access to data from 2014 and before, which falls out of the scope of the dataset.

# <b>Existing Customer Revenue Current Year

# Insufficient data, to calculate the existing customer revenue for the year 2015, we would need a list of existing customers in 2015. To get the list of existing customers in 2015, we will need access to data from 2014 and before, which falls out of the scope of the dataset.

# <b>Existing Customer Revenue Prior Year(2014)

# No data available for 2014.

# <b>Total Customers Current Year(2015)=231294

# In[23]:


len(all2015)


# <b>Total Customers Previous Year

# No data available for 2014.

# <b>New Customers(2015)

# Insufficient data, to calculate the number of new customers in 2015, we would need a list of new customers in 2015. To get the list of new customers in 2015, we will need access to data from 2014 and before, which falls out of the scope of the dataset.

# <b>Lost Customers(2015)

# Insufficient data, to calculate the number of lost customers in 2015, we would need a list of customers in 2014. To get the list of customers in 2014, we will need access to data from 2014 and before, which falls out of the scope of the dataset.

# # Plots

# In[24]:


temp=df.groupby(['year']).sum()['net_revenue'].reset_index()
temp
height=list(temp['net_revenue'])
height
bars=('2015','2016','2017')
y_pos = np.arange(len(bars))
plt.figure(figsize=(12, 6))
plt.bar(y_pos, height,color='#99ccff',edgecolor='black')
plt.xticks(y_pos, bars)
plt.xlabel('Year',fontsize=16)
plt.ylabel('Net Revenue-Normalized to 10^7 scale',fontsize=16)
plt.title('Yearly Revenue',fontsize=20)
plt.show()


# <b>Based on the yearly revenue, 2017 seems to be the best performing year, followed by 2015, and at last place 2016

# In[25]:


temp=df.groupby(['year']).count()['net_revenue'].reset_index()
temp
height=list(temp['net_revenue'])
height
bars=('2015','2016','2017')
y_pos = np.arange(len(bars))
plt.figure(figsize=(12, 6))
plt.bar(y_pos, height,color='#99ccff',edgecolor='black')
plt.xticks(y_pos, bars)
plt.xlabel('Year',fontsize=16)
plt.ylabel('Total Customer Count',fontsize=16)
plt.title('Customer base per year',fontsize=20)
plt.show()


# <b> A similar trend as the yearly revenue, is observed in the total customer count per year. The best performing year is 2017, followed by 2015, and at last place 2016

# In[26]:


df.groupby(['year']).sum()
top=df.groupby("customer_email").sum().sort_values("net_revenue",ascending=False).head(10)['net_revenue']
top=pd.DataFrame(top).reset_index()
top
plt.figure(figsize=(12, 6))
sns.barplot(x=top["customer_email"], y=top["net_revenue"], palette="rocket")
plt.xticks(rotation=80)

plt.xlabel('Customers',fontsize=16)
plt.ylabel('Net revenue over 3 years',fontsize=16)
plt.title('Top 10 customers',fontsize=20)
plt.show()


# <b>The above chart shows the most profitable customers for all the years combined, based on revenue contributed by these customers

# In[27]:


sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
plt.figure(figsize=(12, 6))
# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="year", y="net_revenue",
            palette=["b",'g','m'],
            data=df)
sns.despine(offset=10, trim=True)
plt.xlabel('Year',fontsize=16)
plt.ylabel('Net revenue',fontsize=16)
plt.title('Distribution of net revenue over years',fontsize=20)
plt.show()


# <b>The distribution of net revenue across the years appear to be very similar, indicating a constant trend/performance over these years.

# In[ ]:




