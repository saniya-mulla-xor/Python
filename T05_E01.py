import json


def roundtrip(obj):
    return json.loads(json.dumps(obj))


sample = {
    "name": "Asha",
    "age": 30,
    "married": False,
    "scores": (90, 85),
    "nickname": None,
    "height": 1.68,
}

compact = json.dumps(sample)
print(f"compact: {compact}")
print("indented:")
print(json.dumps(sample, indent=2, sort_keys=True))

restored = roundtrip(sample)
print(
    f"scores type before: {type(sample['scores']).__name__} "
    f"| after: {type(restored['scores']).__name__}"
)
print(
    f"married after: {restored['married']} "
    f"| nickname after: {restored['nickname']}"
)
print(f"equal after round trip: {restored == sample}")
print(f"int keys: {roundtrip({1: 'a', 2: 'b'})}")

try:
    json.dumps({"items": {1, 2, 3}})
except TypeError as error:
    print(f"TypeError: {error}")