import json

apple = {
    "name" : "Biraj",
    "age" : 19,
    "height" : 175,
    "weight" : 78,
}

conversion = json.dumps(apple)
print(conversion)

json_str = '{"name":"Ram","age":22,"height":155,"weight":50}'
convert = json.loads(json_str)
print(convert)