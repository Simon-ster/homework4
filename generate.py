def calculate(f,l):
    if str(f).isdigit():
        return None
    elif f == "" or l == "":
        return str(f) + str(l)
    else:
        return str(f) + " " + str(l)

if __name__ == "__main__":
    first = str(input("Enter your first name: "))
    last = str(input("Enter your last name: "))

    print(calculate(f,l))