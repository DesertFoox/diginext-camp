def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def get_input():
    matrix = []
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    print("Enter the matrix row by row (numbers separated by spaces):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Row {i+1} should have {cols} columns. Please enter again:")
            row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    target = int(input("Enter the target number: "))
    return matrix, target


matrix, target = get_input()

result = search_matrix(matrix, target)
print(result)
