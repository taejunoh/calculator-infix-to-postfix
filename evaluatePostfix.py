from Stack import Stack

"""
Evaluate the postfix expression and get a result of the initial equation
"""


def evalPost(post_list):
    val_stack = Stack()

    for post in post_list:
        # Numbers into a value stack
        if type(post) is float:
            val_stack.push(post)

        # Operators
        # calculate two numbers then add new value to the value stack
        elif post == '+':
            n1 = val_stack.pop()
            n2 = val_stack.pop()
            val_stack.push(n2 + n1)

        elif post == '-':
            n1 = val_stack.pop()
            n2 = val_stack.pop()
            val_stack.push(n2 - n1)

        elif post == '*':
            n1 = val_stack.pop()
            n2 = val_stack.pop()
            val_stack.push(n2 * n1)

        elif post == '/':
            n1 = val_stack.pop()
            n2 = val_stack.pop()
            val_stack.push(float(n2 / n1))

    # Get the final value after calculating all
    return val_stack.pop()
