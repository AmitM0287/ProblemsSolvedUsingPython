def permutations(word):
    """
    This function print all the permutation of a string.
    :param word: It's accept word as a parameter.
    :return: It's return a list of all possible permutation.
    """
    if len(word) == 1:
        return word
    list_ = permutations(word[1:])
    char = word[0]
    result = []
    for item in list_:
        for word_ in range(len(item)+1):
            result.append(item[:word_] + char + item[word_:])
    return result


if __name__ == '__main__':
    print(permutations('ABC'))
