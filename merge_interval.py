def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]

        if current[0] <= last_merged[1]:
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged.append(current)

    return merged


def get_input():
    input_str = input("Enter a list of intervals (e.g., (1,3) (2,6) (8,10)): ")
    intervals = []
    input_str = input_str.replace("(", "").replace(")", "")
    for interval in input_str.split():
        start, end = map(int, interval.split(","))
        intervals.append((start, end))
    return intervals


intervals = get_input()

output = merge_intervals(intervals)
print(output)
