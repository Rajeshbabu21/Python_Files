height = int(input("enter the height"))
width = int(input("enter the width"))

def paint(height, width):
    no_of_cans = (height*width)/7
    print(f"no_of_cans is {no_of_cans}")

paint(height, width)    