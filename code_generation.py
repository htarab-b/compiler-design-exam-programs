class ExpressionConverter:
   def __init__(self, expression):
       self.expression = expression.replace(" ", "")
       self.operators = set(['+', '-', '*', '/', '(', ')'])
       self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
   
   def infix_to_postfix(self):
       stack = []  # operator stack
       output = []  # output list
 
       for char in self.expression:
           if char not in self.operators:  # if operand, add to output
               output.append(char)
           elif char == '(':  # if '(', push to stack
               stack.append(char)
           elif char == ')':  # if ')', pop until '('
               while stack and stack[-1] != '(':
                   output.append(stack.pop())
               stack.pop()  # remove '('
           else:  # operator encountered
               while stack and stack[-1] != '(' and self.precedence[char] <= self.precedence[stack[-1]]:
                   output.append(stack.pop())
               stack.append(char)
 
       # pop all the operators from the stack
       while stack:
           output.append(stack.pop())
 
       return ''.join(output)
 
   def infix_to_prefix(self):
       def reverse_expression(expr):
           expr = expr[::-1]
           expr = list(expr)
           for i in range(len(expr)):
               if expr[i] == '(':
                   expr[i] = ')'
               elif expr[i] == ')':
                   expr[i] = '('
           return ''.join(expr)
 
       reversed_expr = reverse_expression(self.expression)
       reversed_postfix = self.infix_to_postfix_expression(reversed_expr)
       return reversed_postfix[::-1]
 
   def infix_to_postfix_expression(self, expr):
       stack = []
       output = []
 
       for char in expr:
           if char not in self.operators:
               output.append(char)
           elif char == '(':
               stack.append(char)
           elif char == ')':
               while stack and stack[-1] != '(':
                   output.append(stack.pop())
               stack.pop()
           else:
               while stack and stack[-1] != '(' and self.precedence[char] <= self.precedence[stack[-1]]:
                   output.append(stack.pop())
               stack.append(char)
 
       while stack:
           output.append(stack.pop())
 
       return ''.join(output)
 
# Example usage
if __name__ == "__main__":
   expression = "(a+b)*(c+d)"
   converter = ExpressionConverter(expression)
 
   postfix = converter.infix_to_postfix()
   prefix = converter.infix_to_prefix()
 
   print(f"Infix: {expression}")
   print(f"Postfix: {postfix}")
   print(f"Prefix: {prefix}")