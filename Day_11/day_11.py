def create_grid_from_file(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    x = 0
    y = 0
    map_points = {}

    for line in lines:
        x = 0
        for char in line.strip():
            map_points[(x, y)] = char
            x += 1
        y += 1
    return { 'grid': map_points, 'map_height': len(lines), 'map_width': len(lines[0]) - 1  }

def all_adjacents_seats_are_empty(grid, point_tuple):
    seat_x = point_tuple[0]
    seat_y = point_tuple[1]

    left_up = grid[(seat_x - 1, seat_y - 1)]
    left = grid[(seat_x - 1, seat_y)]
    left_down = grid[(seat_x - 1, seat_y + 1)]

    center_up = grid[(seat_x, seat_y - 1)]
    center_down = grid[(seat_x, seat_y + 1)]

    right_up = grid[(seat_x + 1, seat_y - 1)]
    right = grid[(seat_x + 1, seat_y)]
    right_down = grid[(seat_x + 1, seat_y + 1)]

    return (left_up == 'L' and left == 'L' and left_down == 'L'
        and center_up == 'L' and center_down == 'L'
        and right == 'L' and right_up == 'L' and right_down == 'L')

def process_map(grid):
    new_grid = {}
    for x in range(1, grid['map_width'] - 1):
        for y in range(1, grid['map_height'] - 1):
            #Floor stays floor
            if grid[(x, y)] == '.':
                new_grid[(x,y)] = '.'
            #If seat is empty and adjacents are empty seat becomes ocuppied
            elif grid[(x,y)] == 'L' and all_adjacents_seats_are_empty(grid, (x,y)):
                new_grid[(x,y)] = '#'
            #If seat is occuppied
            elif grid[(x,y)] == '#' and four_or_more_adjacents_are_occuppied(grid, (x,y)):
                new_grid[(x,y)] = 'L'
            else:
                new_grid[(x,y)] = grid[(x,y)]
    return new_grid

def main():
    grid = create_grid_from_file('testinput.txt')
    last_occuppied_seats = 0
    new_occuppied_seats = -1

    # while True:
    new_grid = process_map(grid)
        # new_occuppied_seats =  count_occuppied_seats(new_grid)
        # if new_occuppied_seats == last_occuppied_seats:
            # print(new_occuppied_seats)
            # break
        # else:
            # last_occuppied_seats = new_occuppied_seats
    print(new_grid)

if __name__ == '__main__':
    main()