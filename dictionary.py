me={
    "name":"mohammad",
    "family":"ordookhani",
    "email":"m.samnjead92@gmail.com"
}
print(me)
# me.pop("name")
# me.popitem()
# print(me)

second={
    "age":50
}
second.update(me)
print(second)
print("---------------------------")
second["name"]="sara"
print(second)