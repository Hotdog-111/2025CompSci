def stairs(steps):
    for i in range(steps-1):
        if i+1 == steps-1:
            print((3+i)*"#" + "]___")
        else:

            print((3+i)*"#" + "]_")



NumberOfSteps = int(input())
print("___")
stairs(NumberOfSteps)
