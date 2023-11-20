import pandas as pd

#Importing the Data
original_file = pd.read_csv("USA_cars_datasets.csv")
#print(original_file)
new_file = original_file.loc[:,["price","brand","year","mileage"]]

#Check for NA values
print("Total Number of NA Values for each")
na_values = pd.isnull(new_file).sum()
print(na_values)  #There is no NA values

#Data Cleaning
new_file = new_file.drop(labels=[545], axis=0) #Removing the data from 1993 as the price and mileage is 0
new_file["mileage"] = new_file["mileage"]*1.609
print("MAX MILEAGE:", max(new_file["mileage"]))
print("MIN MILEAGE:", min(new_file["mileage"]))

print("MAX PRICE : ", max(new_file["price"]))
print("MIN PRICE : ", min(new_file["price"]))
#New Cleaned File
new_file.to_csv("/Users/sebastianklemens/Desktop/DATA1002 /USA_cars_cleaned.csv")

#Creating a dictionary for the year and average mileage
year_mileage = {}
is_first_line = True

for row in open("USA_cars_cleaned.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    year = values[3]
    mileage = float(values[4])
    if year in year_mileage:
        year_mileage[year].append(mileage)
    else:
        year_mileage[year] = [mileage]

for key in sorted(year_mileage) :
    mileage = year_mileage[key]
    average_mileage = sum(mileage) / len(mileage)

    print(f'{key} : {average_mileage}')
