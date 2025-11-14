

import random

def generate_duplicate_test_data(size, num_duplicates=1, dup_count=2, random_seed=None):
    """
    Generates test data for duplicate element finder.
    Args:
        size (int): Total size of the array; must be >= num_duplicates * dup_count.
        num_duplicates (int): How many unique numbers should be duplicated.
        dup_count (int): How many times each duplicate value should appear in total (>=2).
        random_seed (int, optional): For reproducible results.
    Returns:
        tuple: (test_list, correct_duplicates_list)
    """
    if random_seed is not None:
        random.seed(random_seed)
    if size < num_duplicates * dup_count:
        raise ValueError("size is too small for the requested number of duplicates.")

    # Possible unique elements from 1 to size
    all_numbers = list(range(1, size + 1))

    # Pick numbers to duplicate
    duplicates = random.sample(all_numbers, num_duplicates)
    correct_duplicates = sorted(duplicates)

    # Start with non-duplicate numbers
    # Remove chosen duplicates from pool temporarily for their first appearance
    available = [x for x in all_numbers if x not in duplicates]
    result = available.copy()

    # Add duplicated numbers, appearing dup_count times each
    for dup in duplicates:
        result.extend([dup] * dup_count)

    # Shuffle the list to randomize positions
    random.shuffle(result)
    # Trim to desired size
    final_result = result[:size]
    random.shuffle(final_result)
    return final_result, correct_duplicates


if __name__ == '__main__':
    # Example usage:
    test_list, correct_dups = generate_duplicate_test_data(size=20, num_duplicates=3, dup_count=2, random_seed=42)
    print("Generated test list:", test_list)
    print("Duplicates inserted:", correct_dups)

