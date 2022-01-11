## 3-8. Seeing the World: Think of at least five places in the world you'd like to visit.

#store loacations in a list, print list
sights = ['disney', 'tokyo', 'ireland', 'iceland', 'texas']
print(sights)

#use sorted() to print list in alphabetical order without modifying the actual list
print(sorted(sights))

#show list still in original order by printing agin
print(sights)

#use sorted() to print list in reverse alphabetical without changing the original order
print(sorted(sights,reverse=True))

#show list still in original order by printing again
print(sights)

#use reverse() to change order of list and print
sights.reverse()
print(sights)

#use reverse() again to change order of list. print to show back to original
sights.reverse()
print(sights)

#use sort() to change your list so it's sorted in alphabetical, print
sights.sort()
print(sights)

#use sort() to change your list so it's sorted in reverse alphabetical, print
sights.sort(reverse=True)
print(sights)