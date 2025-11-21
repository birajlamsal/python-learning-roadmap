student: dict[str, str | int]={
    "name":"Biraj Lamsal",
    "age":22,
    "class": 12,
    "faculty": "sci"
}

print(student)

print(student["name"])
print(student["age"])
print(student["faculty"])

student["address"] = "Kathmandu"
print(student)

del student["faculty"]
print(student)

student["age"]=10
print(student)

student.clear()
print(student)