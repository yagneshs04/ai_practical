V = ["A", "B", "C", "D", "E", "F", "G"]
C = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("B", "E"),
     ("C", "E"), ("C", "F"), ("D", "E"), ("E", "F"), ("E", "G"), ("F", "G")]
D = ["Monday", "Tuesday", "Wednesday"]

def backtrack(a={}):
    if len(a) == len(V): return a
    v = next((x for x in V if x not in a), None)
    for d in D:
        if all(d != a.get(x) for x, y in C if y == v) and backtrack({**a, v: d}):
            return backtrack({**a, v: d})

def main():
    print(backtrack())

if __name__ == "__main__":
    main()