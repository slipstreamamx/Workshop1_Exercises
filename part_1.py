# selected_operator = input("Please selet an operator '*', '+', '-', or '/'?: ")
# first_number = int(input("Please enter your first number? "))
# second_number = int(input("Please enter your second number?: "))

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
    else:
        answer = int(f_num / s_num)
    return int(answer)


def process_goto(process_line):
    if process_line[1] == "calc":
        operator = process_line[2]
        first_number = int(process_line[3])
        second_number = int(process_line[4])
        calculate(operation=operator,f_num = first_number,s_num =second_number)
        return int(answer)
    
    else:
        return int(process_line[1])


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

filePath = r"C:\Users\asado\DevOps\Module 1\Exercises\Workshop Part 1\goto.txt"
with open(filePath, "r", encoding='utf-8') as f:
    line = f.read().splitlines(True)
    line_hits = set()
    line_number = 1
    while True:
        current_line = line[line_number - 1]
        if current_line in line_hits:
            break
        line_togo = current_line.split()
        new_line = process_goto(line_togo)
        print(current_line)
        print(new_line)
        line_hits.add(current_line)
        line_number = new_line
    print(f"Answer: Line {current_line}{line_number}")



