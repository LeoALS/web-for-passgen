
#Lists

list1 = ['they', 'hello', 'iscream', 'car', 'toilet']
list2 = ['How', 'Hi', 'Morning', 'are', 'am', 'fine', 'I', 'you', 'studying', 'Good']
list3 = ['Apple', 'for', 'doing', 'fine', 'I', 'Thanks', 'asking', 'am']
Nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

inp2 = int(input("hvor mange ord vil du ha? "))
inp = int(input("hvor mange tall vil du ha? "))


#randomizer and print

import random

List = (list1) + (list2) + (list3)

r = 1
while r <= inp2:
    print(random.choice(List), end="")
    r = r +1

i = 1
while i <= inp:
    print(random.choice(Nums), end="")
    i =i +1

input("")
