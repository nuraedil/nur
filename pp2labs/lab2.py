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

    


