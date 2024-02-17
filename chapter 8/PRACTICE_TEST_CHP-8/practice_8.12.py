def formatted(name):
    if name =="":
        return "you have entered the empty string"
    else:
        return name.title()
    
formatted_name = formatted("")
print(formatted_name)