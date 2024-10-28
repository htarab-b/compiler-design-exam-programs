grammar = ["id", "E+E", "E*E", "(E)"]

def shift_reduce_parse(input_string):
    stack = []
    input_list = list(input_string)
    
    print("STACK \t INPUT \t ACTION")

    while input_list:
        symbol = input_list.pop(0)
        stack.append(symbol)
        print("$" + ''.join(stack) + "\t" + ''.join(input_list) + "$\tSHIFT " + symbol)
        
        for rule in grammar:
            rule_len = len(rule)
            if ''.join(stack[-rule_len:]) == rule:
                for _ in range(rule_len):
                    stack.pop()
                stack.append('E')
                print("$" + ''.join(stack) + "\t" + ''.join(input_list) + "$\tREDUCE TO E (" + rule + ")")
                
print("GRAMMAR is E->E+E \n E->E*E \n E->(E) \n E->id")
input_string = input("Enter input string: ")
shift_reduce_parse(input_string)