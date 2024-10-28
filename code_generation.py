operators = ['+', '-', '*', '/', '(', ')']
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

def infix_to_postfix(expression):
    expression = expression.replace(" ", "")
    stack = []
    output = []

    for char in expression:
        if char not in operators:
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def infix_to_prefix(expression):
    reversed_expr = expression[::-1].replace('(', 'temp').replace(')', '(').replace('temp', ')')
    postfix = infix_to_postfix(reversed_expr)
    return postfix[::-1]

expression = "(a+b)*(c+d)"
postfix = infix_to_postfix(expression)
prefix = infix_to_prefix(expression)

print(f"Infix: {expression}")
print(f"Postfix: {postfix}")
print(f"Prefix: {prefix}")