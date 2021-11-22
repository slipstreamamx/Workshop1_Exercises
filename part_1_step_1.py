selected_operator = input("Please selet an operator '*', '+', '-', or '/'?: ")
first_number = int(input("Please enter your first number? "))
second_number = int(input("Please enter your second number?: "))

answer = 0

def calculate(operations, f_num, s_num):
    global answer
    if operations == "+":
        answer = f_num + s_num
    elif operations == "-":
        answer = f_num - s_num
    elif operations == "*":
        answer = f_num * s_num
    else:
        answer = f_num / s_num
    return answer

print(calculate(operations=selected_operator,f_num=first_number,s_num=second_number))



