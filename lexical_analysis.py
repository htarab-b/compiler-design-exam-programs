keywords = ["void", "using", "namespace", "int", "include", "iostream", "std", "main", "cin", "cout", "return", "float", "double", "string"]
operators = ["+", "-", "*", "/", "^", "&&", "||", "=", "==", "&", "|", "%", "++", "--", "+=", "-=", "/=", "*=", "%="]
symbols = ["(", "{", "[", ")", "}", "]", "<", ">", "()", ";", "<<", ">>", ",", "#"]

def classify_token(token):
    if token in operators:
        return "operator"
    if token in keywords:
        return "keyword"
    if token in symbols:
        return "symbol"
    if token.isdigit():
        return "constant"
    return "identifier"

code = input()
s = ""
for char in code:
    if char != ' ':
        s += char
    else:
        if s:
            print(f"{s} is a {classify_token(s)}")
            s = ""
if s:  # Final token
    print(f"{s} is a {classify_token(s)}")
