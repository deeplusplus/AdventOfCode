def get_numbers():
    file = open('input_2.txt', 'r')
    numbers_as_strings = file.readlines()
    numbers = [int(number_as_string) for number_as_string in numbers_as_strings]    
    return numbers

def find_two_entries():
    numbers = get_numbers()
    number_1 = -1
    number_2 = -1
    number_3 = -1
    found_triplet = False

    while not found_triplet and len(numbers) > 0:
        possible_number_1 = numbers.pop(0)
        for possible_number_2 in numbers:
            for possible_number_3 in numbers[2:-1]:
                if possible_number_1 + possible_number_2 + possible_number_3 == 2020:
                    print('Found the triplet')
                    number_1 = possible_number_1
                    number_2 = possible_number_2
                    number_3 = possible_number_3
                    found_triplet = True


    print(number_1, number_2, number_3)
    print(number_1 * number_2 * number_3)