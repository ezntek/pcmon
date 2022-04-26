import json
firstDict = {
    "a" : "b",
    "b" : "d",
    "c" : "f"
}
secondDict = {
    "1" : 2,
    "2" : True,
    "3" : "string"
}

def first():
    with open("test.json", "w") as j:
        j.writelines(json.dumps(firstDict))
def second():
    with open("test.json", "w") as j:
        j.writelines(json.dumps(secondDict))

c = input("1 or 2")

if c == "1":
    first()
    exit()
elif c == "2":
    second()
    exit