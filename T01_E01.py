def list_stats(nums):
    if not nums:
        return {
            "max": None,
            "min": None,
            "total": 0,
            "average": 0.0,
            "descending": [],
            "every_second": [],
        }

    return {
        "max": max(nums),
        "min": min(nums),
        "total": sum(nums),
        "average": sum(nums) / len(nums),
        "descending": sorted(nums, reverse=True),
        "every_second": nums[::2],
    }


numbers = [14, 3, 9, 27, 8, 21, 5, 18]
stats = list_stats(numbers)

print(f"max: {stats['max']}")
print(f"min: {stats['min']}")
print(f"total: {stats['total']}")
print(f"average: {stats['average']:.2f}")
print(f"descending: {stats['descending']}")
print(f"every second: {stats['every_second']}")
