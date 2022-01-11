### In order to have both names printed, would i need to use a list?
first_name = "ada"
first_name = "gabe"
last_name = "lovelace"
last_name = "calderon"
full_name = f"{first_name} {last_name}"
full_name = f"{first_name} {last_name}"
### ^ This second full name variable is unnecessary 
print(full_name)

print(f"Hello, {full_name.title()}!")

message = f"Hey, {full_name.title()}!"
print(message)