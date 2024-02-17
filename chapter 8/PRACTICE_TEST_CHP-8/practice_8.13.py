# month = input("enter the month") 
# print(month)

# def no_of_days(month):
#     if month == "feb":
#         return 29
#     elif month == "jan":
#         return 30
#     elif month == "march":
#         return 30
#     else:
#         return 29
    
# days = no_of_days(month)
# print(days)


# hacker rank
year = int(input("enter the year"))
print(year)

def is_leap(year):
    if year%4 == 0 or year%400 == 0 :
        return True
    else : 
        if year%100 == 0:
           return False
           
output = is_leap(year)
print(output)

