import random

# int
a=random.randint(1,3)
print(a)

# range
b=random.randrange(1,5)
print(a)

# float 0.0 t0  1.0
c=random.random()
print(c)

# float range
d=random.uniform( 1,10)
print(d)

# random choice
print("hi")
list=[1,2,3,4,5,6,7,8,9,0,'raj']
e=random.choice(list)
print(e)

# for random shuffle
l=[1,2,3,4,5,6,7,8,9,9,0,'raj']
f=random.shuffle(l)
print(l)
