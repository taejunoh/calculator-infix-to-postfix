"""
Turn an infix expression as input into tokens in a list
"""


def split_tokens(string_expression):
    # Remove whitespace
    str_expr = string_expression.replace(' ', '')

    tokens = []
    num = ""
    i = 0
    while i < len(str_expr):
        # Deal with "-"
        if (
            # The equation starts with "-"
            (str_expr[i] == "-" and i == 0) or
            # case "(-" (e.g. "(-4)" )
            (str_expr[i] == "-" and str_expr[i-1] == "(") or
            # case "*-", "/-", "+-", "--" (e.g. "4*-4", "5/-5", "6+-6", "7--7")
            (str_expr[i] == "-" and str_expr[i-1] in "*/+-")
        ):
            num += str_expr[i]

        # Deal with "-." (e.g. ".1", ".2")
        elif str_expr[i] == "." and str_expr[i+1].isdigit():
            num += str_expr[i]

        # String is digits
        elif (str_expr[i].isdigit()):
            num += str_expr[i]
            # Check float with a decimal point
            for j in range(i+1, len(str_expr)):
                if (str_expr[j].isdigit() or str_expr[j] == "."):
                    num += str_expr[j]
                    i += 1
                else:
                    break

            # Add float into the list
            tokens.append(float(num))
            num = ""

        else:
            tokens.append(str_expr[i])

        i += 1

    return tokens
