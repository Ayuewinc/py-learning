import json

dict = {
        "animals": {
        "dog": [
            {
                "name": "Rufus",
                "age":15
            },
            {
                "name": "Marty",
                "age": 16
            }
        ]
    }
}

data = dict["animals"]["dog"]
for d in data:
    print(type(d))
    print(d.get('name'))