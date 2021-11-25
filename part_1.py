# selected_operator = input("Please selet an operator '*', '+', '-', or '/'?: ")
# first_number = int(input("Please enter your first number? "))
# second_number = int(input("Please enter your second number?: "))

from os import replace


answer = 0
sum_result = 0


def calculate(operation, f_num, s_num):
    global answer
    if operation == "+":
        answer = int(f_num + s_num)
    elif operation == "-":
        answer = int(f_num - s_num)
    elif operation == "x":
        answer = int(f_num * s_num)
    elif operation == "/":
        answer = int(f_num / s_num)
    else:
        return int(answer)


def process_goto(line_to_process):
    if line_to_process[1] == "calc":
        operator = line_to_process[2]
        first_number = int(line_to_process[3])
        second_number = int(line_to_process[4])
        calculate(operation=operator,f_num = first_number,s_num =second_number)
        return int(answer)
    
    else:
        return int(line_to_process[1])


def process_remove(line_to_process, current_line, file_line):
    line_to_remove = int(line_to_process[1])
    if line_to_remove <= current_line:
        line_to_process_next = current_line
    else:
        line_to_process_next = current_line + 1
    file_line.pop(line_to_remove)
    return line_to_process_next


def process_replace(line_to_process, current_line, file_line):
    line_to_repace = int(line_to_process[1])
    line_to_copy = int(line_to_process[2])
    copied_line = file_line[line_to_copy - 1]
    file_line.pop(line_to_repace - 1)
    file_line.insert(line_to_repace -1, copied_line)
    return current_line + 1

def process_all(line_to_process, current_line, file_line):
    instructions = line_to_process[0]
    if instructions == "goto":
        return process_goto(line_to_process)
    elif instructions == "remove":
        return process_remove(line_to_process, current_line, file_line)
    elif instructions == "remove":
        return process_remove(line_to_process, current_line, file_line)
    else:
        raise Exception("Unexpected Instruction!")




# # print(calculate(operation=selected_operator,f_num=first_number,s_num=second_number))

# filePath = r"C:\Users\asado\DevOps\Module 1\Exercises\Workshop Part 1\calc.txt"
# with open(filePath, 'r', encoding='utf-8') as f:
#     calc_list = f.read()
#     for line in calc_list.splitlines(True):
#         calc_line = line.split()
#         selected_operator = calc_line[1]
#         first_number = int(calc_line[2])
#         second_number = int(calc_line[3])
#         calculate(operation=selected_operator,f_num=first_number,s_num=second_number)
#         sum_result += answer
#     print(sum_result)

filePath = r"C:\Users\asado\DevOps\Module 1\Exercises\Workshop Part 1\remove.txt"
with open(filePath, "r", encoding='utf-8') as f:
    file_line = f.read().splitlines(True)
    line_hits = set()
    line_number = 1
    while True:
        current_line = file_line[line_number - 1]
        if current_line in line_hits:
            break
        line_to_process = current_line.split()
        new_line = process_all(line_to_process, line_number, file_line)
        print(current_line)
        print(new_line)
        line_hits.add(current_line)
        line_number = new_line
    print(f"Answer: Line {line_number} {current_line}")



