#intial_speed (i)= 30
i = 18.5
while i <= 80:
    print("speed of the vehicles:",i)
    i = i + 10

list1 = ["speed of bike = 18.5,28.5,38.5","speed of car = 48.5,58.5,78.5","speed of Truck = 28.5,38.5,48.5","speed of bus = 28.5,38.5,48.5"]
print(list1)
x = (18.5+28.5+38.5)/2
print("average_speed_of_bike:",x)
y = (48.5+58.5+68.5)/2
print("average_speed_of_car:",y)
z = (28.5+38.5+48.5)/2
print("average_speed_of_Truck:",z)
m = (28.5+38.5+48.5)/2
print("average_speed_of_bus:",m)
if x and y and z and m < 40:
    print("The traffic was slow")
elif 40 < x and y and z and m < 80:
    print("The traffic was normal")
elif x and y and z and m > 80:
    print("The traffic was fast")
else :
    print("The traffic was zero traffic")
    