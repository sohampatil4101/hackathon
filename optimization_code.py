class Operand:
    def __init__(self, l, r):
        self.l = l
        self.r = r

def main():
    op = []
    pr = []
    print("Enter the Number of Values:")
    n = int(input())

    for i in range(n):
        print("left: ", end="")
        l = input()
        print("right: ", end="")
        r = input()
        op.append(Operand(l, r))

    print("Intermediate Code")
    for i in range(n):
        print(op[i].l + "=" + op[i].r)

    z = 0
    for i in range(n - 1):
        temp = op[i].l
        for j in range(n):
            if temp in op[j].r:
                pr.append(Operand(op[i].l, op[i].r))
                z += 1

    pr.append(Operand(op[n - 1].l, op[n - 1].r))
    z += 1

    print("\nAfter Dead Code Elimination")
    for k in range(z):
        print(pr[k].l + "=" + pr[k].r)

    for m in range(z):
        tem = pr[m].r
        for j in range(m + 1, z):
            if pr[j].r in tem:
                t = pr[j].l
                pr[j].l = pr[m].l
                for i in range(z):
                    if t in pr[i].r:
                        a = pr[i].r.index(t)
                        pr[i].r = pr[i].r[:a] + pr[m].l + pr[i].r[a + 1:]

    print("Eliminate Common Expression")
    for i in range(z):
        print(pr[i].l + "=" + pr[i].r)

    for i in range(z):
        for j in range(i + 1, z):
            if pr[i].l == pr[j].l and pr[i].r == pr[j].r:
                pr[i].l = ''

    print("Optimized Code")
    for i in range(z):
        if pr[i].l != '':
            print(pr[i].l + "=" + pr[i].r)

if __name__ == "__main__":
    main()


# output

# Enter the Number of Values:
# 5
# left: a
# right: 9
# left: b
# right: c+d
# left: e
# right: c+d
# left: f
# right: b+e
# left: r
# right: f
# Intermediate Code
# a=9
# b=c+d
# e=c+d
# f=b+e
# r=f

# After Dead Code Elimination
# b=c+d
# e=c+d
# f=b+e
# r=f
# Eliminate Common Expression
# b=c+d
# b=c+d
# f=b+b
# r=f
# Optimized Code
# b=c+d
# f=b+b
# r=f
