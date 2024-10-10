l = input("Enter Left Non-Terminal (e.g., A->): ")[0]
r1, r2 = input("Enter the productions (separated by /): ").split('/')

def remove_left_recursion(left, recursive, non_recursive):
    print("\nLeft Recursion Detected!")
    modified = recursive[1:]
    print("Solution:")
    print(f"\t\t{left} -> {non_recursive}{left}'")
    print(f"\t\t{left}' -> {modified}{left}' / ε")

if l == r1[0]:
    remove_left_recursion(l, r1, r2)
elif l == r2[0]:
    remove_left_recursion(l, r2, r1)