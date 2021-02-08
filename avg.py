

def calculate(elements):
    sum = 0
    if not elements:
        return None
    try:
        for i in elements:
            sum += i
        return sum / len(elements)
    except TypeError:
        return None


if __name__ == "__main__":
    lst = []
    n = int(input("Enter the number of elements of your list : "))

    for i in range(0,n):
        ele = int(input())
        lst.append(ele)

    print(calculate(lst))