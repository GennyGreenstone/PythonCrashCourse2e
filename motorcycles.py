#original list
print(f"1----")
print(f"play with lists")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print(f"2---")
#changing an element of a list
motorcycles[0] = 'ducati'
print(motorcycles)

print(f"3---")
#Append/add new item to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

print(f"4---")
#Append/add new items to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print(f"5---")
#Insert new items into the list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

print(f"6---")
###remove items from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

print(f"7---")
##remove a specific item using Del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)
#Once this is done you can no longer access the deleted item

print(f"8---")
##pop()items off the top of a list and you can still access the item for other uses
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(f"9---")
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

print(f"10---")
##You can remove or pop() specific items from a list also
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

print(f"11---")
##Remove an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print(f"12---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
##\n means "new line"