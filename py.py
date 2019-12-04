def temperature(day, month, temp):
    print(day + "." + month + " ", end="")
    print("   "*(temp+5) + "-", end="")
    print()
def temperatureaxis():
    print("      ", end="")
    for i in range(-5,16):
        print("{:02d} ".format(i), end="")
    print()