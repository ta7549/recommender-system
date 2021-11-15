from recency import Online_Retail_g_recency
from frequency import Online_Retail_g_frequency
from monetary import Online_Retail_g_monetary
from initialDataAnalysis import Online_Retail_g
import numpy as np
import pandas as pd
import math
import random
import seaborn as sns
import pandas_profiling as pp
import matplotlib.pyplot as plt
import datetime as dt

print("\nConcat of recency, frequency and monetary dataframes ")
Online_Retail_g_rfm = pd.concat([Online_Retail_g_recency, Online_Retail_g_frequency, Online_Retail_g_monetary], axis =1, join="inner")
print(Online_Retail_g_rfm.head())

print("\n Removing duplicated columns")
Online_Retail_g_rfm = Online_Retail_g_rfm.loc[:,~Online_Retail_g_rfm.columns.duplicated()]

print("\nrfm dataframe head(10)")
print(Online_Retail_g_rfm.head(10))

print("\nrfm dataframe tail(10)")
print(Online_Retail_g_rfm.tail(10))

print("\n Clustering the data into 3 clusters")
Online_Retail_g_rfm['R_clusters'] = pd.qcut(Online_Retail_g_rfm['Recency'], 3, ['1','2','3'])
Online_Retail_g_rfm['F_clusters'] = pd.qcut(Online_Retail_g_rfm['Frequency'], 3, ['3','2','1'])
Online_Retail_g_rfm['M_clusters'] = pd.qcut(Online_Retail_g_rfm['Monetary'], 3, ['3','2','1'])
print("\n rfm dataframe after clustering head(10)")
print(Online_Retail_g_rfm.head(10))


print("\n rfm dataframe after clustering tail(10)")
print(Online_Retail_g_rfm.tail(10))

print("\n Calculating combined rfm score")
Online_Retail_g_rfm['Combinedrfm_score'] = Online_Retail_g_rfm.R_clusters.astype(str)+ Online_Retail_g_rfm.F_clusters.astype(str) + Online_Retail_g_rfm.M_clusters.astype(str)
print("\n rfm dataframe after Calculating combined rfm score head(10)")
print(Online_Retail_g_rfm.head(10))


print("\nCustomer purchase records with rfm score of 111 - TOP PERFORMING CUSTOMERS - head(10) ")
Online_Retail_g_rfm_111 = Online_Retail_g_rfm[Online_Retail_g_rfm['Combinedrfm_score'] == '111']
print(Online_Retail_g_rfm_111.head(10))

print("\nCustomer purchase records with rfm score of 111 - TOP PERFORMING CUSTOMERS - tail(10) ")
print(Online_Retail_g_rfm_111.tail(10))


print("\nCustomer purchase records with rfm score of 222 - AVERAGE PERFORMING CUSTOMERS - head(10) ")
Online_Retail_g_rfm_222 = Online_Retail_g_rfm[Online_Retail_g_rfm['Combinedrfm_score'] == '222']
print(Online_Retail_g_rfm_222.head(10))

print("\nCustomer purchase records with rfm score of 222 - AVERAGE PERFORMING CUSTOMERS - tail(10) ")
print(Online_Retail_g_rfm_222.tail(10))



print("\nCustomer purchase records with rfm score of 333 - LEAST PERFORMING CUSTOMERS - head(10) ")
Online_Retail_g_rfm_333 = Online_Retail_g_rfm[Online_Retail_g_rfm['Combinedrfm_score'] == '333']
print(Online_Retail_g_rfm_333.head(10))

print("\nCustomer purchase records with rfm score of 333 - LEAST PERFORMING CUSTOMERS - tail(10) ")
print(Online_Retail_g_rfm_333.tail(10))


