import re

def make_bag(bag_name, rule_dict):
    return (bag_name, rule_dict[bag_name])

def make_bag_contents(a_bag, rule_dict):
    contents = [rule_dict[a_bag[0]]]
    for bag in rule_dict[a_bag[0]]:
        for i in range(0, int(bag[1])):
            contents.append(make_bag_contents(bag, rule_dict))
    return contents

def bag_contains_shiny_gold(bag_name, bag_contents, rule_dict):
    if 'shiny gold' in bag_contents:
        return True
    
    for inner_bag_name in bag_contents:
        if bag_contains_shiny_gold(inner_bag_name, rule_dict[inner_bag_name], rule_dict):
            bag_contains_shiny_gold(inner_bag_name, rule_dict[inner_bag_name], rule_dict)
            return True
        else:
            pass
    return False

def bags_in_shiny_gold_bag(rule_dict):
    bag = make_bag('shiny gold', rule_dict)
    bag_with_contents = make_bag_contents(bag, rule_dict)
    return bag_with_contents



def process_line_to_rule(line):
    split_line = line.split('bag')
    rule_name = split_line[0].strip()
    contents = []

    if split_line[1] is not 's contain no other':
        for chunk in split_line:
            match = re.search('[0-9]', chunk)
            if match:
                contents.append((chunk[match.start() + 2:-1], chunk[match.start()]))
                # contents.append(chunk[match.start() + 2:-1])

    return (rule_name, contents)

def main():
    file = open('testinput.txt')
    lines = file.readlines()
    rules = {}
    count = 0

    for line in lines:
        rule_tuple = process_line_to_rule(line)
        rules[rule_tuple[0]] = rule_tuple[1]

    print(bags_in_shiny_gold_bag(rules))


if __name__ == "__main__":
    main()