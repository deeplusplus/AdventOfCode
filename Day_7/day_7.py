import re

def bags_in_shiny_gold_bag(rules_dict):
    return 0

def bag_contains_shiny_gold(bag_name, bag_contents, rule_dict):
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
        print(rule_tuple)
        rules[rule_tuple[0]] = rule_tuple[1]

    print(rules)

    # print(bags_in_shiny_gold_bag(rules))


if __name__ == "__main__":
    main()