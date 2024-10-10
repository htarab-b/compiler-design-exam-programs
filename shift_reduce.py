# Global variables
a = []
stk = []
act = "SHIFT->"

def check():
    ac = "REDUCE TO E"
    patterns = [('id', 1), ('E+E', 2), ('E*E', 2), ('(E)', 2)]
    
    for pattern, reduce_len in patterns:
        for z in range(len(stk) - reduce_len):
            if ''.join(stk[z:z + reduce_len + 1]) == pattern:
                stk[z] = 'E'
                del stk[z + 1:z + reduce_len + 1]
                print(f"\n${''.join(stk)}\t{''.join(a)}$\t{ac}")
                return

print("GRAMMAR is :\n E->E+E \n E->E*E \n E->(E) \n E->id")
a = list(input("Enter input string: "))

print("STACK \t INPUT \t ACTION")
while a:
    if ''.join(a[:2]) == 'id':
        stk.extend(a[:2])
        a[:2] = [' ', ' ']
        print(f"\n${''.join(stk)}\t{''.join(a)}$\t{act}id")
        check()
    else:
        stk.append(a.pop(0))
        print(f"\n${''.join(stk)}\t{''.join(a)}$\t{act}symbols")
        check()
