nums = [2, 7, 11, 15, -2, 9]
target = 9

def count_pairs_with_sum(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # j ต้องมากกว่า i
            if nums[i] + nums[j] == target:
                count += 1
    return count

# ทดสอบ
nums = [2, 7, 11, 15, -2, 9]
target = 9
print("Total pairs =", count_pairs_with_sum(nums, target))
