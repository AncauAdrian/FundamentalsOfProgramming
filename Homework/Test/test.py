def generate(x, DIM):
    if len(x) == DIM:
        print(x)

    if len(x) > DIM:
        return

    x.append(0)
    for i in range(0, DIM):
        x[-1] = i
        generate(x[:], DIM)


generate([], 3)