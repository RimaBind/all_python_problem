def commonElements(a, b):
    output = []
    for num1 in a:
        for num2 in b:
            if num1 == num2:
                output.append(num1)
    return output  # Yeh line dono 'for' loops ke bahar honi chahiye

a = [1, 12, 34, 5, 8, 9]
b = [2, 2, 5, 7, 8, 9, 12]

print("Common Elements :", commonElements(a, b))