import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud

# read dataset

data = pd.read_csv("../data/OnlineRetail.csv", encoding= 'unicode_escape', low_memory=False)
data.info()


#converting the string data field to datatype datetime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data.info()

#taking purchase records from Germany only for the purpose of this project.
filter1=data["Country"]=="Germany"
data = data[filter1]

# removing null value records and removing white spaces in description column for consistency
print(data.columns[data.isnull().any()])
data["Description"].value_counts()
data['Description'] = data['Description'].str.strip()

# removing cancelled item records from the dataset
data.dropna(subset =['InvoiceNo'], inplace = True)
data['InvoiceNo'] = data['InvoiceNo'].astype('str')
data = data[~data['InvoiceNo'].str.contains('C')]

# making dataset ready to input for implementing Apriori and Fp growth algorithms

# Selecting specific columns InvoiceNo,Description and aggregating the records in description for every invoice no

data = data[["InvoiceNo","Description"]]
new_df = pd.DataFrame(columns=list(data["Description"].unique()))
print("Unique items in the dataset:", new_df.shape[1])

# creating a binary matrix having items in the description as column headers
data_new = data.groupby('InvoiceNo').agg({'Description': lambda x: list(x)})
for index, row in data_new.iterrows():
    value = row['Description']
    temp=[]
    for column in new_df.columns:
            for i in value:
                if i == column:
                    temp.append(column)
    encoded_rows = []
    for column in new_df.columns:
        if column in temp:
            encoded_rows.append(1)
        else:
            encoded_rows.append(0)
    new_df=new_df.append(pd.Series(encoded_rows, index=new_df.columns), ignore_index=True)

print(new_df.head(3))
data = pd.DataFrame(data_new['Description'].tolist())

allTransactions = []
for i in range(0, data.shape[0]):
    for j in range(0, data.shape[1]):
        allTransactions.append(data.values[i, j])

allTransactions = np.array(allTransactions)

transDf = pd.DataFrame(allTransactions, columns=["items"])
transDf["incident_count"] = 1

indexNames = transDf[transDf['items'] == "nan"].index
transDf.drop(indexNames, inplace=True)

dfTable = transDf.groupby("items").sum().sort_values("incident_count", ascending=False).reset_index()
dfTable.head(50).style.background_gradient(cmap='Oranges')


s=data[0].to_string(index=False)

# wordcloud visualization for top 50 popular items in the dataset

plt.rcParams['figure.figsize'] = (15, 15)
wordcloud = WordCloud(background_color = 'lightpink', width = 1000,  height = 1000, max_words = 50).generate(s)
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Most Popular Items',fontsize = 40, fontweight='bold')
plt.savefig("../fig/wordcloud.png")

#Frequency of 40 Most popular items plot
plt.rcParams['figure.figsize'] = (18, 7)
color = plt.cm.summer(np.linspace(0, 1, 40))
data[0].value_counts().head(40).plot.bar(color = color)
plt.title('Frequency of 40 Most Popular Items', fontsize = 40, fontweight='bold')
plt.xticks(rotation = 90 )
plt.grid()
plt.savefig("../fig/40MostPopular.png")

# creating a dataframe which consists of top 50 popular items
first50 = dfTable["items"].head(50).values # Select Top50
new_df = new_df.loc[:,first50] # Extract Top50
print("top 50 items: ", new_df.columns)


