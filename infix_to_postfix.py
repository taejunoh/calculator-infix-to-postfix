from Stack import Stack
"""
Turn a tokenized infix expression into a postfix expression
"""


def inf_to_post(tokens):
    # Precedence of operators
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    op_stack = Stack()
    post_list = []

    for token in tokens:
        # Float into a postfix list
        if type(token) is float:
            post_list.append(token)

        # "(" into an operator stack
        elif token == '(':
            op_stack.push(token)

        # ")", remove parenthesis not added to the postfix list
        elif token == ')':
            # pop from the operator stack until "("
            while op_stack.peak() != '(':
                post_list.append(op_stack.pop())

            op_stack.pop()

        # Operators
        else:
            # add to the operator stack if empty
            if not op_stack:
                op_stack.push(token)

            # the operator stack if not empty
            else:

                while len(op_stack) > 0:
                    # precedance in the operator stack is higher
                    if prec[op_stack.peak()] >= prec[token]:
                        # add to the postfix list
                        post_list.append(op_stack.pop())
                    else:
                        break

                op_stack.push(token)

    # Add remains in the operator stack into the postfix list
    while op_stack:
        post_list.append(op_stack.pop())

    return post_list
