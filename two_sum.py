def twoSum(nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
nums = list(map(int, input("Enter the array (space-separated): ").split()))
target = int(input("Enter the target: "))

result = twoSum(nums, target)
print("Indices: ", result)
