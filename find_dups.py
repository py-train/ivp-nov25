

def find_duplicates_1(nums):
    duplicates = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])
    return duplicates


def find_duplicates_2(nums):
    nums.sort()
    duplicates = []
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            duplicates.append(nums[i])
    return list(set(duplicates))  # remove any accidental repeats


def find_duplicates_3(nums):
    duplicates = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] = -nums[index]
    # Optional: restore modified list if needed
    return duplicates


def find_duplicates_4(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)



if __name__ == '__main__':
    from gen_dups import generate_duplicate_test_data

    data, dups = generate_duplicate_test_data(size=12, num_duplicates=2, dup_count=3, random_seed=42)
    dups_found = find_duplicates_3(data)

    assert dups_found == dups, f'Correct dups not found, {dups_found} != {dups}'

