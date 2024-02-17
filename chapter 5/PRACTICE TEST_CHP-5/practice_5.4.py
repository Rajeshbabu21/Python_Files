student_data = [{ 'ram':97,
                 'roll_no ' : 20222,
                 'age' : 28
                 }, 
{
                'raj':97,
                 'roll_no ' : 20221,
                 'age' : 23

}]
print(student_data)

def add_new(name):
    new_data = {}
    new_data["name"] = name
    student_data.append(new_data)
add_new("rajesh")
print(student_data)