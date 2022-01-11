# 3-2. Greetings: Start with the list you used in exercise 3-1, but instead of just printing each person's name, print a message to them. The text of each message should be the same, but each message should be personalized with the person's name.

names = ['joe', 'alex', 'rob', 'kitty', 'heather']

message = f"I care about you so much,"

print(message + names[0].title())
print(message + names[1].title())
print(message + names[2].title())
print(message + names[-2].title())
print(message + names[-1].title())

# I realize there are a number of ways to do this exercise. I was confused as to how I could do the message with the names list in it while also having a separate print for each person. This is one of the work-arounds I came up with. I also went back to the first time doing this exercise and found that I originally just made numerous message variables.