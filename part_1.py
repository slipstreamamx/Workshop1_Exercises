# selected_operator = input("Please selet an operator '*', '+', '-', or '/'?: ")
# first_number = int(input("Please enter your first number? "))
# second_number = int(input("Please enter your second number?: "))

answer = 0
sum_result = 0

def calculate(operation, f_num, s_num):
    global answer
    if operation == "+":
        answer = f_num + s_num
    elif operation == "-":
        answer = f_num - s_num
    elif operation == "x":
        answer = f_num * s_num
    else:
        answer = f_num / s_num
    return answer

# print(calculate(operation=selected_operator,f_num=first_number,s_num=second_number))

filePath = r"C:\Users\asado\DevOps\Module 1\Exercises\Workshop Part 1\calc.txt"
with open(filePath, 'r', encoding='utf-8') as f:
    calc_list = f.read()
    for line in calc_list.splitlines(True):
        calc_line = line.split()
        selected_operator = calc_line[1]
        first_number = int(calc_line[2])
        second_number = int(calc_line[3])
        calculate(operation=selected_operator,f_num=first_number,s_num=second_number)
        sum_result += answer


    print(sum_result)
