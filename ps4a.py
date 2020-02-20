# Problem Set 4A
# Name: <Hossein Karagah>


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    perm_list = []

    if len(sequence) == 1:
        perm_list.append(sequence)
    else:
        first_letter = sequence[0]
        sub_perm_list = get_permutations(sequence[1:])
        for element in sub_perm_list:
            for index in range(len(element)):
                new_element_1 = element[:index] + first_letter + element[index:]
                new_element_2 = element[index:] + first_letter + element[:index]
                if not (new_element_1 in perm_list):
                    perm_list.append(new_element_1)
                if not (new_element_2 in perm_list):
                    perm_list.append(new_element_2)
    return perm_list



if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
   print('---')
   # Put three example test cases here (for your sanity, limit your inputs
   # to be three characters or fewer as you will have n! permutations for a
   # sequence of length n)

   example_input = 'hos'
   print(get_permutations(example_input))
   print('---')

   example_input = 'acc'
   print(get_permutations(example_input))



