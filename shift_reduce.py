# Grammar:
# E -> E + E
# E -> E * E
# E -> ( E )
# E -> id

# Define parsing rules and actions
grammar = ["id", "E+E", "E*E", "(E)"]

def shift_reduce_parse(input_string):
    stack = []
    input_list = list(input_string)
    
    print("STACK \t INPUT \t ACTION")

    while input_list:
        # Shift step
        symbol = input_list.pop(0)
        stack.append(symbol)
        print("$" + ''.join(stack) + "\t" + ''.join(input_list) + "$\tSHIFT " + symbol)
        
        # Reduce step
        while True:
            for rule in grammar:
                rule_len = len(rule)
                if ''.join(stack[-rule_len:]) == rule:
                    for _ in range(rule_len):
                        stack.pop()  # Remove symbols of the rule
                    stack.append('E')  # Reduce to 'E'
                    print("$" + ''.join(stack) + "\t" + ''.join(input_list) + "$\tREDUCE TO E (" + rule + ")")
                    break
            else:
                break

# Test the parser
print("GRAMMAR is E->E+E \n E->E*E \n E->(E) \n E->id")
input_string = input("Enter input string: ")
shift_reduce_parse(input_string)