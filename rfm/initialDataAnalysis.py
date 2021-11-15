import matplotlib.pyplot as plt
import pandas as pd

Online_Retail = pd.read_csv("../data/OnlineRetail.csv", encoding= 'unicode_escape', low_memory=False)
Online_Retail.info()
print(Online_Retail.shape)


Online_Retail.head(3)

#we only need two columns for the plot
Online_Retail_plot = Online_Retail[['Country','CustomerID']].drop_duplicates()
print(Online_Retail_plot.shape)

#plotting Country value counts
Online_Retail_plot.Country.value_counts()[:15].plot(kind='bar', figsize = (20,12))
plt.savefig("../fig/countryValueCounts.png")

#Online_Retail_g holds the records for Germany.
Online_Retail_g = Online_Retail[Online_Retail.Country == 'Germany']
print(Online_Retail_g.shape)

print("Purchase records in Germany\n")
print(Online_Retail_g.head(4))

# to check if the data has any cancelled values
dup_Online_Retail_g = Online_Retail_g.loc[Online_Retail_g['Quantity'] < 0]
print("Checking if the data has any cancelled values\n")
print(dup_Online_Retail_g)


# as we see we have cancelled items which appear as negative quantity is dropped from data
print("Removing cancelled items purchase records\n")
Online_Retail_g = Online_Retail_g.loc[Online_Retail_g['Quantity'] > 0]
print(Online_Retail_g.shape)

print(Online_Retail_g.head(3))
Online_Retail_g.info()

#Converting string date to datetime field
Online_Retail_g['InvoiceDate'] = pd.to_datetime(Online_Retail_g['InvoiceDate'])
Online_Retail_g.info()






