# (x, y, is_empty_space)



def create_grid_from_file(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    x = 0
    y = 0
    map_points = {}

    for line in lines:
        x = 0
        for char in line:
            map_points[(x, y)] = char is '.'
            x += 1
        y += 1
    return { 'grid': map_points, 'map_height': len(lines), 'map_width': len(lines[0]) - 1  }

def next_toboggan_spot(point, trajectory):
    return (point[0] + trajectory[0], point[1] + trajectory[1])

def spot_has_tree(point, grid):
    return not grid[point]

def main():
    tree_count = 0
    grid = create_grid_from_file('input1.txt')
    point = (0, 0)
    trajectory = (7, 1)

    while point[1] < grid['map_height']:
        if spot_has_tree(point, grid['grid']): tree_count += 1
        point = next_toboggan_spot(point, trajectory)

    print(tree_count)


if __name__ == "__main__":
    main()