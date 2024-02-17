# TODO решите задачу
import json

def task() -> float:
    result = 0
    with open("input.json", "r") as f:
        data = json.load(f)
    for obj in data:
        result += (obj["score"] * obj["weight"])
    return round(result, 3)


print(task())
