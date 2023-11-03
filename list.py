# list in python

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# length

print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(type(list1))

# list
thislist1 = list(("apple", "banana", "cherry"))
# note the double round-brackets
print(thislist1)

# find list

print(thislist[2:3])

# d
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[4:])

# loop
thislist4 = ["apple", "banana", "cherry"]
if "apple" in thislist4:
    print("Yes, 'apple' is in the fruits list")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)