def add_leaf(leaves, operand):
    if operand in leaves:
        return leaves[operand]
    leaves[operand] = operand
    return operand

def get_or_create_node(nodes, value, left, right):
    key = (value, left, right)
    if key in nodes:
        return nodes[key]

    label = f"t{len(nodes) + 1}"
    nodes[key] = label
    return label

def build_dag(expression):
    nodes = {}
    leaves = {}
    stack = []

    for symbol in expression:
        if symbol.isalpha():
            leaf = add_leaf(leaves, symbol)
            stack.append(leaf)
        else:
            right = stack.pop()
            left = stack.pop()
            node = get_or_create_node(nodes, symbol, left, right)
            stack.append(node)

    return stack.pop(), nodes

def print_dag(nodes):
    for (value, left, right), label in nodes.items():
        print(f"{label} = {left} {value} {right}")

expression = ['a', 'b', '+', 'c', '*', 'b', '+']
root, nodes = build_dag(expression)
print("DAG Representation:")
print_dag(nodes)