bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
###^This outcome shows the brackets when printed
print(bicycles[0])
###^This prints just one item from the list, neatly formatted
print(bicycles[0].title())
###^Here, using a string method, python formats the item to be capitalized
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)