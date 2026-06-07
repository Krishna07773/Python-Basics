
per = float(input("enter your percentage: "))
   
if per < 0 or per > 100:
    print("Invalid Percentage")
elif per >= 90:
    print("A+")
elif per >= 80:
    print("A")
elif per >= 70:
    print("B")
elif per >= 60:
    print("C")
elif per >= 40:
    print("D")
else:
    print("Fail")