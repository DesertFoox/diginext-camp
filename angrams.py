def group_anagrams(strs):
    anagrams = {}

    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]

    return list(anagrams.values())


def get_input():
    input_strs = input("Enter a list of strings separated by spaces: ").split()
    return input_strs


input_strs = get_input()

output = group_anagrams(input_strs)
print(output)
