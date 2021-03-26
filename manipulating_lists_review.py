inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#wow congrats Jiho
#find the number of elements in a list w len()
inventory_len = len(inventory)
print(inventory_len)

#call a single element from a list with []
first = inventory[0]
print(first)

#using the index [-1] gives the last element
last = inventory[-1]
print(last)

#call multiple elements within a list by slicing
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

#remove first index in slice to include elements up to 2nd index
first_3 = inventory[:3]
print(first_3)

#count instances of a certain element in a list w .count()
twin_beds = inventory.count("twin bed")
print(twin_beds)

#remove an element with .pop()
removed_item = inventory.pop(4)
print(removed_item)

#add an element with .insert()
inventory.insert(10, "19th Century Bed Frame")
print(inventory)

#sort an inventory with .sort() or sorted()
inventory.sort()
print(inventory)
