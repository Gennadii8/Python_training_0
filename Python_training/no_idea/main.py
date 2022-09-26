
def calculate_happiness(line_1, line_2, good_set, bad_set):
    all_numbers = line_1 + line_2
    print(all_numbers)
    for one_element in all_numbers:
        if one_element == '' or one_element == ' ':
            all_numbers.remove(one_element)
    print(all_numbers)

    for one_elem in good_set:
        if one_elem == '' or one_elem == ' ':
            good_set.remove(one_elem)
    print(good_set)
    for one_el in bad_set:
        if one_el == '' or one_el == ' ':
            bad_set.remove(one_el)
    print(bad_set)



    #
    # string_length = len(string)
    # number_of_rows = math.ceil(string_length / k)
    # # print(f"{string_length}")
    # # print(f"{number_of_rows}")
    # string.split()
    # counter = 0
    # while counter != number_of_rows:
    #     current_row = string[0:k]
    #     # print(current_row)
    #     list_of_unique_values = []
    #     one_string_output = ''
    #     for one_symbol in current_row:
    #         if one_symbol not in list_of_unique_values:
    #             list_of_unique_values.append(one_symbol)
    #     # print(list_of_unique_values)
    #     for one_value in list_of_unique_values:
    #         one_string_output += str(one_value)
    #     print(one_string_output)
    #     string = string[k:]
    #     counter += 1


if __name__ == '__main__':
    first_line = list(input())
    second_line = list(input())
    positive_set = list(input())
    negative_set = list(input())

    calculate_happiness(first_line, second_line, positive_set, negative_set)
"""
https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true 
"""
