
# In python it doenst normally colide but if colides than is it automatically fixed . the below is jsut a manual represenrtation of collosion ( AI )
class BadHash:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 1  # all objects will have the same hash → collision

    def __eq__(self, other):
        return self.value == other.value

# Create dictionary with "colliding" keys
fruits = {
    BadHash("apple"): 4,
    BadHash("banana"): 5,
    BadHash("orange"): 6
}

# Access values
for key in fruits:
    print(key.value, fruits[key])
