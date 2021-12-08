from sys import exit


def check_input(string_expression):
    """
    Syntax errors on a calculator
    1. An open bracket without closing parenthesis
    2. Missing numbers in an equation (e.g. "12*+5", "12+/4", missing numbers between operators)
    3. Using Minus sign instead of the negative symbol (Not Applicable)
    """

    # Remove whitespace
    str_expr = string_expression.replace(' ', '')

    # Case 1. An open bracket without closing parenthesis
    # -> match the number of parenthesis
    left_p = str_expr.count("(")
    right_p = str_expr.count(")")
    if left_p != right_p:
        print("Syntax Error")
        exit()

    # Case 2. Missing numbers in an equation
    # -> check invalid repeated operators
    re_oper = [
        "*+",
        "+*",
        "/+",
        "+/",
        "**",
        "//",
        "-+",
        "++",
        "---"
    ]

    for oper in re_oper:
        if str_expr.find(oper) != -1:
            print("Syntax Error")
            exit()
        else:
            continue

    """
    Invalid input on the calculator
    1. String is not digits
    2. String is not operators
    3. String is not decimal (e.g. "." )
    4. String is not parenthesis (e.g. "(", ")" )
    """

    # Invalid input
    # -> check invalid string as input
    for each in str_expr:
        if each not in '01234567890+-*/.()':
            print("Invalid Input")
            exit()
