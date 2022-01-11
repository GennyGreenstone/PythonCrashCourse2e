## 3-4. Guest List: IF you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to diner.

guests = ['sy', 'joe', 'nikki']
print(guests)
message = f", I would greatly appreciate it if you would join me for dinner!"

print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)


## 3-5. Changing Guest List: You just heard one of your guests can't make it, so you need to send out a new set of invitations. You'll have to think of someone else to invite.

print(f"\n Unfortunately, {guests[1].title()} has work so he can't make it")

guests.pop(1)
guests.append('bailey')
print(guests)
## I don't like this but this is the best i can do for the moment 12*30*21

##This next message i want to do a -while- loop to print the invites but i dont remember how to do that right now man

print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)


## 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to diner.

print(f'\n Great news!', guests, ' I have just found a larger dinner table. So more people can join us now!') 

guests.insert(0, 'jerdon')
guests.insert(2, 'alexzandra')
guests.append('grandma')

print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)
print(guests[3].title() + message)
print(guests[4].title() + message)
print(guests[5].title() + message)

## 3-7. You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.

print(f"\n Unfortunately, the new table I ordered won't be here in time. So I only have space for two people")

sorry = guests.pop(0).title()
print(f"I'm really sorry,", sorry, "this is just going to be a small catch up dinner so I have to un-invite you. We'll have dinner soon.")

sorry = guests.pop(0).title()
print(f"I'm really sorry,", sorry, "this is just going to be a small catch up dinner so I have to un-invite you. We'll have dinner soon.")

sorry = guests.pop(0).title()
print(f"I'm really sorry,", sorry, "this is just going to be a small catch up dinner so I have to un-invite you. We'll have dinner soon.")

sorry = guests.pop(0).title()
print(f"I'm really sorry,", sorry, "this is just going to be a small catch up dinner so I have to un-invite you. We'll have dinner soon.")

print(f"Hey,", guests[0].title(), "I hope you can still make it, I would be honored to have you!")
print(f"Hey,", guests[1].title(), "I hope you can still make it, I would be honored to have you!")

del guests[0]
del guests[0]
print(guests)

print(len(guests))