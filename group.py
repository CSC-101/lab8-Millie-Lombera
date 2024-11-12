def groups_of_3(arr: list[int]) -> list[list[int]]:
    grouped_list = []
    for i in range(0, len(arr), 3):
        grouped_list.append(arr[i:i + 3])
    return grouped_list

