def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def get_input():
    input_str = input("Enter a list of integers separated by spaces: ")
    nums = list(map(int, input_str.split()))
    return nums


nums = get_input()

output = longest_consecutive(nums)
print(output)
