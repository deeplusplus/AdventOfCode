import re

def bag_contains_shiny_gold(bag_name, bag_contents, rule_dict):
    # print('Checking:', bag_name, '\nContents:', bag_contents, '\n')
    if 'shiny gold' in bag_contents:
        return True
    
    for inner_bag_name in bag_contents:
        if bag_contains_shiny_gold(inner_bag_name, rule_dict[inner_bag_name], rule_dict):
            return True
        else:
            pass
    return False



def process_line_to_rule(line):
    split_line = line.split('bag')
    rule_name = split_line[0].strip()
    contents = []

    if split_line[1] is not 's contain no other':
        for chunk in split_line:
            match = re.search('[0-9]', chunk)
            if match:
                # contents.append((chunk[match.start() + 2:-1], chunk[match.start()]))
                contents.append(chunk[match.start() + 2:-1])

    return (rule_name, contents)

def main():
    file = open('input.txt')
    lines = file.readlines()
    rules = {}
    count = 0

    for line in lines:
        rule_tuple = process_line_to_rule(line)
        print(rule_tuple)
        rules[rule_tuple[0]] = rule_tuple[1]


    for key, value in rules.items():
        # print('-----------------------')
        if bag_contains_shiny_gold(key, value, rules):
            count += 1

    print(count)

if __name__ == "__main__":
    main()