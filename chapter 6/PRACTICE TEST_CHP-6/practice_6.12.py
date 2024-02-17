name_1=input("enter the name")
name_2=input("enter the name")

# string concatenate
name=name_1+name_2
print("name")

# to lower
lower=name.lower()
print(lower)

t=lower.count("t")
r=lower.count("r")
u=lower.count("u")
e=lower.count("e")

true=  t + r + u + e


l=lower.count("l")
o=lower.count("0")
v=lower.count("v")
e=lower.count("e")

love= l + o + v + e

# concatenation
combine=str(true)+str(love)
love_score=(int(combine))
print(love_score)



if(love_score<10 or love_score>90):
    print("you love score ",love_score)
elif(love_score>=40 or love_score<=50):
    print("your love score untill",love_score)
else:
    print("not",love_score)