
def calculate(side):
    if side < 0:
        return None
    try:
        volume = side * side * side
        return volume
    except ValueError:
        return None
        
if __name__ == "__main__":
    side = int(input("Input a side length: "))
    print("Volume = " + str(calculate(side)))
