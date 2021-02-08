
def calculate(side):
    try:
        if int(side) < 0:
            return None
        volume = side * side * side
        return volume
    except ValueError:
        return None
        
if __name__ == "__main__":
    side = input("Input a side length: ")
    print("Volume = " + str(calculate(side)))
