name = str(input("Enter a name:"))
a = int(input("Enter marks of maths:"))
b = int(input("Enter marks of science:"))
c = int(input("Enter marks of social:"))
total_marks = a+b+c
print("Total marks:",total_marks)
average_marks = (a+b+c)/2
print("Average_marks:",average_marks)
if  80< a and b and c < 100:
    print("print A grade")
elif 60 < a and b and c < 80:
    print("print B grade")
elif 40 <  a and b and c < 60:
    print("print C grade")
elif 0 < a and b and c < 40:
    print("print D grade")
else:
    print("error")