import string

m = input("Enter a regular expression: ")
n = len(m)
t = [[' ' for _ in range(10)] for _ in range(10)]
r = 0

for i in range(n):
    if m[i] == '|':
        t[r + 1][r + 2] = m[i - 1]
        t[r + 3][r + 4] = m[i + 1]
        t[r][r + 1] = 'E'
        t[r][r + 3] = 'E'
        t[r + 2][r + 5] = 'E'
        t[r + 4][r + 5] = 'E'
        r += 5
    elif m[i] == '*':
        t[r + 1][r + 2] = m[i - 1]
        t[r - 1][r] = 'E'
        t[r][r + 1] = 'E'
        t[r][r + 3] = 'E'
        t[r + 2][r + 1] = 'E'
        t[r + 2][r + 3] = 'E'
        r += 3
    elif m[i] == '+':
        t[r][r + 1] = m[i - 1]
        t[r + 1][r] = 'E'
        r += 1
    else:
        if i + 1 < n and m[i] in string.ascii_letters and m[i + 1] in string.ascii_letters:
            t[r][r + 1] = m[i]
            t[r + 1][r + 2] = m[i + 1]
            r += 2

print("\n", end="")
for j in range(r + 1):
    print(f" {j}", end="")
print("\n" + "_" * 35)

for i in range(r + 1):
    for j in range(r + 1):
        print(f" {t[i][j]}", end="")
    print(f" | {i}")

print(f"\nStart state: 0\nFinal state: {r}")