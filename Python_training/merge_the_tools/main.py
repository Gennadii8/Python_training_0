import math


def merge_the_tools(string, k):
    string_length = len(string)
    number_of_rows = math.ceil(string_length / k)
    # print(f"{string_length}")
    # print(f"{number_of_rows}")
    string.split()
    counter = 0
    while counter != number_of_rows:
        current_row = string[0:k]
        # print(current_row)
        list_of_unique_values = []
        one_string_output = ''
        for one_symbol in current_row:
            if one_symbol not in list_of_unique_values:
                list_of_unique_values.append(one_symbol)
        # print(list_of_unique_values)
        for one_value in list_of_unique_values:
            one_string_output += str(one_value)
        print(one_string_output)
        string = string[k:]
        counter += 1


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


"""
https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD
"""
