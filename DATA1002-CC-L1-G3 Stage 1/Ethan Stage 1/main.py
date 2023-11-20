import pandas as pd
# Import Data
df = pd.read_csv("germany_cars.csv")
df1 = df.loc[:,["make", "year", "mileage", "price"]]

# Check for NA values
na_check = pd.isnull(df1).sum()
print(na_check)

# Data Cleaning
df1 = df1.rename(columns = {"make":"brand", "price": "price(EUR)"})
df1["price(EUR)"] = df1["price(EUR)"]*0.99
df1 = df1.rename(columns = {"price(EUR)":"price(USD)"})
print(df1)

# Write clean data to new csv
df1.to_csv("/Users/ethan_yong_1/Documents/USYD_Projects/germany_final.csv")




