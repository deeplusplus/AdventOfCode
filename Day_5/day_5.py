def turn_row_into_binary(column_string):
    binary_string = ''

    for char in column_string:
        if char is 'B':
            binary_string += '1'
        else:
            binary_string += '0'
    return binary_string

def turn_column_into_binary(column_string):
    binary_string = ''

    for char in column_string:
        if char is 'R':
            binary_string += '1'
        else:
            binary_string += '0'
    return binary_string

def get_seat_row(seat_string):
    return int(turn_row_into_binary(seat_string[:7]),2)

def get_seat_column(seat_string):
    return int(turn_column_into_binary(seat_string[7:]),2)

def get_seat_id(row, column):
    return (row * 8) + column

def main():
    file = open('input.txt', 'r')
    max_seat_id = -1
    seat_ids = []
    my_seat_id = 0

    lines = file.readlines()

    for line in lines:        
        row = get_seat_row(line.strip())
        column = get_seat_column(line.strip())
        seat_id = get_seat_id(row, column)
        seat_ids.append(seat_id)
        if max_seat_id < seat_id:
            max_seat_id = seat_id

    seat_ids.sort()

    for i in range(0, len(seat_ids) + 1):
        if seat_ids[i+1] - seat_ids[i] == 2:
            my_seat_id = seat_ids[i] + 1
            print(my_seat_id)
    print(max_seat_id)


if __name__ == "__main__":
    main()