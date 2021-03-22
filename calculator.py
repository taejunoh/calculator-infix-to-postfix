from input_validation import check_input
from tokenize_infix import split_tokens
from infix_to_postfix import inf_to_post
from evaluate_postfix import eval_post


def calculate():
    # Take text or string as input
    print("Please enter a mathematical expression. Type 'exit' to leave.")

    while True:
        string_expression = input()
        if string_expression == "exit":
            break
        else:
            # Input validation
            check_input(string_expression)

            # Tokenize infix expression
            tokens = split_tokens(string_expression)

            # Turn infix to postfix
            postfix = inf_to_post(tokens)

            # Evaluate postfix
            result = eval_post(postfix)

            # Get a result
            print(result)
            break


if __name__ == '__main__':
    calculate()
