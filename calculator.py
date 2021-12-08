from inputValidation import checkInput
from tokenizeInfix import splitTokens
from infixToPostfix import infToPost
from evaluatePostfix import evalPost

def calculate():
    # Take text or string as input
    print("Please enter a mathematical expression. Type 'exit' to leave.")

    while True:
        string_expression = input()
        if string_expression == "exit":
            break
        else:
            # Input validation
            checkInput(string_expression)

            # Tokenize infix expression
            tokens = splitTokens(string_expression)

            # Turn infix to postfix
            postfix = infToPost(tokens)

            # Evaluate postfix
            result = evalPost(postfix)

            # Get a result
            print(result)
            break


if __name__ == '__main__':
    calculate()
