import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

df = pd.read_csv('car_price_prediction.csv')
print(f'the dataset has {df.shape[0]} rows and {df.shape[1]} columns befor removeing duplicates.')
print(f'Datasettet har 18 søyler som er {df.keys()}')
df.drop_duplicates(inplace=True)
print(f'the dataset has {df.shape[0]} rows and {df.shape[1]} columns after removeing duplicates.')
df_new = df[['Manufacturer', 'Model', 'Mileage', 'Price']] #makes a new dataframe with the chosen columns
df_new['Mileage'] = df_new['Mileage'].apply(lambda x:str(x).replace("km"," "))#removes the km part of the mileage string
df_new['Mileage'] = df_new['Mileage'].astype(str).astype(float) #convertes the string to an int
print(f'A summary of the Mileage and price columns in the datasett')
print(df_new[['Mileage','Price']].describe())

sns.boxplot(df_new['Mileage'])
plt.title("Box Plot before median imputation")
plt.show()

q1 = df_new['Mileage'].quantile(0.25)
q3 = df_new['Mileage'].quantile(0.75)
iqr = q3-q1
Lower_tail = q1 - 1.5 * iqr
Upper_tail = q3 + 1.5 * iqr
med = np.median(df_new['Mileage'])
for i,j in zip(df_new.index,df_new['Mileage']):
    if j > Upper_tail or j < Lower_tail:
            df_new= df_new.drop(i)
sns.boxplot(df_new['Mileage'])
plt.title("Box Plot after median imputation")
print(df_new[['Mileage','Price']].describe())

plt.show()
print(df_new)
df_new.to_csv('Car_price_prediction_clean.csv',index = False)
'''''''''
this section covers the data integration'''

def combine_data(dataset1,dataset2,atributes):
    return pd.concat([dataset1[liste],dataset2[liste]],keys = atributes,ignore_index=True)

df_USA = pd.read_csv('USA_cars_cleaned.csv')
print(df_USA.keys())
df_USA['Manufacturer'] = df_USA['brand']
df_USA['Mileage'] = df_USA['mileage']
df_USA['Price'] = df_USA['price']
del df_USA['brand'], df_USA['mileage'], df_USA['price']
liste = ['Manufacturer','Price','Mileage']
data = combine_data(df_new,df_USA,liste)
df_german = pd.read_csv('germany_final.csv')
df_german['Price'] = df_german['price(USD)']
df_german['Manufacturer'] = df_german['brand']
df_german['Mileage'] = df_german['mileage']
del df_german['mileage'],df_german['brand'],df_german['price(USD)']
data1 = combine_data(data,df_german,liste)
data1.to_csv('data1.csv',index = False)
df_bel = pd.read_csv('Belarus Used Cars Prices_clean.csv')
print(df_bel.keys())
df_bel['Price'] = df_bel['priceUSD']
df_bel['Mileage'] = df_bel['mileage(kilometers)']
df_bel['Manufacturer'] = df_bel['make']
del df_bel['priceUSD'],df_bel['mileage(kilometers)'],df_bel['make']

data_final = combine_data(data1,df_bel,liste)
data_final.to_csv('data_final.csv')