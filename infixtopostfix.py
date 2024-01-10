def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    def is_operator(char):
        return char in precedence
    
    def higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]
    
    postfix_steps = []
    postfix_notation = []
    operator_stack = []

    for char in expression:
        if char.isalnum():
            postfix_notation.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_notation.append(operator_stack.pop())
            operator_stack.pop()  # Discard '('
        elif is_operator(char):
            while operator_stack and operator_stack[-1] != '(' and higher_precedence(operator_stack[-1], char):
                postfix_notation.append(operator_stack.pop())
            operator_stack.append(char)

        # Append a copy of postfix_notation to postfix_steps
        postfix_steps.append(postfix_notation.copy())

    while operator_stack:
        postfix_notation.append(operator_stack.pop())

    # Append the final postfix notation to postfix_steps
    postfix_steps.append(postfix_notation.copy())

    return postfix_steps

def display_postfix_steps(expression):
    postfix_steps = infix_to_postfix(expression)

    for i, postfix_notation in enumerate(postfix_steps):
        print(f"Postfix Notation {i + 1}: {' '.join(postfix_notation)}")

if __name__ == "__main__":
    infix_expression = input("Enter infix expression: ")
    display_postfix_steps(infix_expression)