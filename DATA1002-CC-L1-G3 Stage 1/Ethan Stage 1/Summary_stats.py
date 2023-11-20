import pandas as pd

# Summary Statistics (Mileage Range):
df2 = pd.read_csv("germany_final.csv")
mileage = df2['mileage']
max_mileage = max(mileage)
min_mileage = min(mileage)
print(f"Mileage ranges from {min_mileage} to {max_mileage}.")

# Summary Statistics (Price Range):
prices = df2['price(USD)']
max_price = max(prices)
min_price = min(prices)
print(f"Price ranges from ${min_price} to ${max_price}.")

# Summary Statistics (Car Brands):
brands = df2['brand']
car_brands = list(pd.unique(brands))
brand_count = 0
for values in car_brands:
    brand_count += 1
print(f"There are a total of {brand_count} car brands.")

# Summary Statistics (Data volume per brand):
car_dic = {}
brands = df2['brand']
for brand in brands:
    if brand not in car_dic:
        car_dic[brand] = 1
    else:
        car_dic[brand] += 1
for key in car_dic:
    print(f"{key} : {car_dic[key]}")

