A = float(input("enter number A:"))
B = float(input("enter number B:"))

print("addition is:", A+B)
print("Subtraction is:", A-B)
print("Multiplication is:", A*B)
if B!=0:
    print("Division is:", A/B)
    print("integer division is:", A//B)
    print("remainder is:", A%B)
else:
    print("division not possible")