##permanently sort list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

##permanently reverse sort list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


##temporarily sorted function

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print(len(cars))