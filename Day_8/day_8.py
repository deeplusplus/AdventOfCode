# [number, type, sign, quantity, has been run]

accumulator_count = 0

def execute_and_get_next_instruction(instruction_to_execute, instructions):
    next_index = 0
    global accumulator_count

    if instruction_to_execute[1] == 'nop':
        instruction_to_execute[4] = True
        next_index = instruction_to_execute[0] + 1
        return instructions[next_index]
    elif instruction_to_execute[1] == 'acc':
        instruction_to_execute[4] = True
        accumulator_count += int(instruction_to_execute[2] + instruction_to_execute[3])
        print("inside", accumulator_count)
        next_index = instruction_to_execute[0] + 1
        return instructions[next_index]
    else:
        instruction_to_execute[4] = True
        next_index = instruction_to_execute[0] + int(instruction_to_execute[2] + instruction_to_execute[3])
        return instructions[next_index]


def make_instruction_list(line, instruction_number):
    instruction_type = line[0:3]
    instruction_sign = line[4]
    instruction_quantity = line[5:]    

    return [instruction_number, instruction_type, instruction_sign, instruction_quantity, False]



def main():
    file = open('input.txt')
    lines = file.readlines()
    ordered_instructions = []
    instruction_number = 0
    global accumulator_count

    for line in lines:
        ordered_instructions.append(make_instruction_list(line.strip(), instruction_number))
        instruction_number += 1

    instruction_to_execute = ordered_instructions[0]

    while not instruction_to_execute[4]:
        print("begin", accumulator_count)
        instruction_to_execute = execute_and_get_next_instruction(instruction_to_execute, ordered_instructions)
        print("end", accumulator_count)

    print(instruction_to_execute)
    print(accumulator_count)

if __name__ == "__main__":
    main()