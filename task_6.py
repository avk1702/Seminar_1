print("Введите шестизначное число:  ")
a = input()
n = int(a[0]) + int(a[1]) + int(a[2])
m = int(a[3]) + int(a[4]) + int(a[5])
if n == m:
    print("Это счастливый билет")
else:
    print("Это обычный билет")