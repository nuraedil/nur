#Boolean Values

#1
print(10 > 9)
print(10 == 9)
print(10 < 9)
#2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#3
print(bool("Hello"))
print(bool(15))
#4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#8
def myFunction() :
  return True

print(myFunction())
#9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#10
x = 200
print(isinstance(x, int))
#ex1
print(10>9)
#ex2
print(10 == 10)
#ex3
print(10<9)
#ex4
print(bool("abc"))
#ex5
print(bool(0))


#Python operators

#1
print(10+5)
#2
print((6 + 3) - (6 + 3))
#3
print(100 + 5 * 3)
#4
print(5 + 4 - 7 + 3)
#ex1
print(10*5)
#ex2
print(10/2)
#ex3
fruits = ["apple", "banana"]
if "apple in fruits":
    print("yes, apple is a fruit")
#ex4
if(5 != 10):
    print("5 and 10 is not equal")
#ex5
if 5 == 10 or 4 == 4:
    print("At least one statement is true")


#Python lists

#1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#5
list1 = ["abc", 34, True, 40, "male"]
#6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#ex2
fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"
#ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")


#Python tuples

#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#6
tuple1 = ("abc", 34, True, 40, "male")
#7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#9
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#10
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#11
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#12
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#14
histuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#15
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#16
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#17
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#18
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#19
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#20
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#21
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#ex1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#ex2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#ex3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#ex4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


#Python sets

#1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#2
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#3
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
#5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#7
set1 = {"abc", 34, True, 40, "male"}
#8
myset = {"apple", "banana", "cherry"}
print(type(myset))
#9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#10
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#11
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#12
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#13
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

#14
print(thisset)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#15
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#16
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#17
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#18
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#Python dictionaries 

#1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#4
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#5
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#6
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#7
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
#ex1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#ex2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
#ex3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#ex4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#ex5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()


#Python if else
#1
a = 33
b = 200
if b > a:
  print("b is greater than a")
#2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#4
a = 2
b = 330
print("A") if a > b else print("B")
#ex1
a = 50
b = 10
if a > b:
  print("Hello World")
#ex2
a = 50
b = 10
if a != b:
  print("Hello World")
#ex3
a = 50
b = 10
if a == b:
  print("YES")
else:
  print("NO") 
#ex4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
#ex5
a = 50
b = 10
c = 50
d = 10
if a == b and c == d:
  print("Hello")
#ex6
a = 50
b = 10
c = 50
d = 10
if a == b or c == d:
  print("Hello") 
#ex7
if 5 > 2:
  print("YES")
#ex8
a = 2
b = 5
print("YES") if a == b else print("NO")
#ex9
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")


#Python while loops
#1
i = 1
while i < 6:
  print(i)
  i += 1
#2
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#ex1
i = 1
while i < 6:
  print(i)
  i += 1
#ex2 
i = 1
while i < 6:
  if i == 3:
    break 
  i += 1 
#ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#ex4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#python for loops
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#2
for x in "banana":
  print(x)
#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#5
for x in range(6):
  print(x)
#6
for x in range(2, 6):
  print(x)
#7
for x in range(2, 30, 3):
  print(x)
#8
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)  
#ex3
for x in range(6):
  print(x)
#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)