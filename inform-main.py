class Data:
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone


you = Data("Blake", "Front st.", "20", "xxx-xxx-xxxx")
friends = Data("Rachel", "St.", "12", "xxx-xxx-xxxx")

print(you.name, you.address, you.age, you.phone)
print(friends.name, friends.address, friends.age, friends.phone)
