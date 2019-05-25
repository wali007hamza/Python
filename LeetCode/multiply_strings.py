import sys
import math


def multiply(num1: str, num2: str):
    list1 = list(num1)
    list2 = list(num2)
    mul_matrix = [[0] * (len(list1) + len(list2) + 1) for i in range(len(list2) + 1)]
    list1.reverse()
    list2.reverse()
    i = 0
    for d2 in list2:
        j = i
        for d1 in list1:
            mul = int(d1) * int(d2)
            mul += mul_matrix[i][j]
            mul_matrix[i][j] = int(mul % 10)
            mul_matrix[i][j + 1] = int(math.floor(mul / 10))
            j += 1

        i += 1

    for j in range(len(list2) + len(list1)):
        col_sum = 0
        for i in range(len(list2)):
            col_sum += mul_matrix[i][j]

        col_sum += mul_matrix[len(list2)][j]

        mul_matrix[len(list2)][j] = int(col_sum % 10)
        mul_matrix[len(list2)][j+1] = int(math.floor(col_sum / 10))

    mul_list = mul_matrix[len(list2)][:len(list1) + len(list2)]
    return mul_list


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        raise AttributeError("Need to pass 2 command line arguments")
    num1 = str(sys.argv[1])
    num2 = str(sys.argv[2])
    if(len(num1) >= len(num2)):
        list1 = num1
        list2 = num2
    else:
        list1 = num2
        list2 = num1
    mul_list = multiply(list1, list2)
    mul_list.reverse()
    s = [str(i) for i in mul_list]
    print(s)
    mul_string = "".join(s)
    print(mul_string)
