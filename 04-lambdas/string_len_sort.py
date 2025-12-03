city = ['kathmandu' , 'newyork' , 'lalitpur','hongkong']
print(city)
##Without  Using lamda


def length(city):
    return len(city)
sort = sorted(city, key=length)
print(sort)

## Using lamda

soort=sorted(city, key=lambda x:len(x))
print(soort)

soort=sorted(city, key=lambda x:len(x) , reverse=True)
print(soort)
