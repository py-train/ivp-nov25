from collections import defaultdict

def group_anagrams1(words):
    # Dictionary to hold sorted word as key and list of anagrams as value
    anagram_map = defaultdict(list)

    for word in words:
        # Sort the word and use as key
        sorted_word = word.sort()
        anagram_map[sorted_word].append(word)

    # Return the grouped anagrams as a list of lists
    return list(anagram_map.values())



if __name__ == '__main__':
    input_words1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    input_words2 = ["dormitory", "dirty room", "Listen", "Silent",
                    "a decimal point", "I'm a dot in place"]
    grouped = group_anagrams1(input_words1)

    print("Grouped Anagrams:")
    for group in grouped:
        print(group)
