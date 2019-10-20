def christmasTree(n):
    for i in range(n):
        print(("+" * (i * 2 + 1)).center(n * 2 - 1))

christmasTree(5)