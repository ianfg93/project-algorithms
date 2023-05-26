def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])
    return merge(left, right)


def merge(left, right):
    new_string = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            new_string.append(left[left_index])
            left_index += 1
        else:
            new_string.append(right[right_index])
            right_index += 1

    new_string.extend(left[left_index:])
    new_string.extend(right[right_index:])

    return new_string


def is_anagram(first_string, second_string):
    first_string = "".join(merge_sort(list(first_string.lower())))
    second_string = "".join(merge_sort(list(second_string.lower())))

    if first_string == "" and second_string == "":
        return (first_string, second_string, False)
    if first_string == second_string:
        return (first_string, second_string, True)
    else:
        return (first_string, second_string, False)
