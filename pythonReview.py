#Start Here

print("Hello world!")
message = "Bonjour monde!"
print(len(message))
print(message[0])
print(type(message))
print(type(3))
print(type("3"))
print(3*3)
print(3*"3")
print(len("greg")==4)

a = 10
b = 3

print(a+b) # Add
print(a-b) # Subtract
print(a*b) # Multiply
print(a/b) # Divide
print(a//b) # Floor Division
print(a**b) # Power
print(a%b) # Modulo

professors = ["greg","kianoosh","richard","patricia","debra"] #Mutable (modifiable), Ordered (has indexes)
print(professors[0])
print(professors[-1])
professors.append("leo")
print(professors)
professors.extend(["heather","kevin","jason"])
print(professors)
professors.insert(2,"trevor")
print(professors)
professors[3]="mark"
print(professors)

print(professors[:]) ## creates a copy of this list (cannot modify a list you are currently looping)
professors.remove("kianoosh")
print(professors.index("mark"))
x = professors.pop(6)
print(x)
print(len(professors))
print(type(professors))

professors.sort()
professors.sort(reverse=True)

for i in professors:
    print(i.title())
print("FIU")

# Dictionaries are lists by labels, not indecision.
water_data = {
    "temperature":[78,89,92],
    "pH":[6.5,6.7,6.3],
    "oxygen":[7.2,5.6,3.5]
}

print(water_data["oxygen"])

import pandas as pd
df = pd.DataFrame(water_data)
print(df)

