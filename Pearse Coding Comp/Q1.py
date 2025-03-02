def find_next_terms(a, b, c):
    nums = sorted([a, b, c])  # Sort the numbers to establish order

    d1 = nums[1] - nums[0]  # Common difference for ascending order
    d2 = nums[2] - nums[1]  # Common difference for ascending order

    if d1 == d2:
        ascending_next = nums[2] + d1  # Next term in ascending order
        descending_next = nums[0] - d1  # Next term in descending order
    else:
        ascending_next = nums[0] + d2  # Next term in ascending order
        descending_next = nums[2] - d2  # Next term in descending order

    print(min(ascending_next, descending_next))
    print(max(ascending_next, descending_next))


# Read input
numbers = [int(input().strip()) for _ in range(3)]
find_next_terms(*numbers)