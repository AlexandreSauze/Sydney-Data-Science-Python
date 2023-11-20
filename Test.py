# sales is a list of pairs; each pair is (location_of_store, amount_in_dollars) 
sales = [("Sydney",410),("Cairns",31),("Hobart",15),("Cairns",32)]
# comment here describing the purpose of dict1
dict1 = {}
for tup in sales:
     location = tup[0]
     amount = tup[1]
     if location not in dict1:
        dict1[location] = [amount]
     else:
        dict1[location].append(amount)
