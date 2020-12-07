import re

# { container_bag: color, contents: [(name, count), (name, count)]}

def bag_contents_include_shiny_gold(contents):
    for rule_tuple in contents:
        if rule_tuple[0] == 'shiny gold':
            return True

def rule_has_shiny_gold(rule, rules):
    if rule['container_bag'] == 'shiny gold':
        return True
    elif bag_contents_include_shiny_gold(rule['contents']):
        return True
    elif len(rule['contents']) is 0:
        return False


def process_line_to_rule(line):
    split_line = line.split('bag')
    rule = { 'container_bag': split_line[0].strip(), 'contents': [] }

    if split_line[1] is not 's contain no other':
        for chunk in split_line:
            match = re.search('[0-9]', chunk)
            if match:
                rule['contents'].append((chunk[match.start() + 2:-1], chunk[match.start()]))

    return rule

def main():
    file = open('testinput.txt')
    lines = file.readlines()
    rules = []
    count = 0

    for line in lines:
        rules.append(process_line_to_rule(line))

    for rule in rules:
        if rule_has_shiny_gold(rule, rules):
            count += 1

    print(count)

if __name__ == "__main__":
    main()