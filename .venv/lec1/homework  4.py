num1=float(input("Введіть перше число: "))
num2=float(input("Введіть друге число: "))
num_nam=(input("Ведіть яку дію ви хочете зробити: (+,-,*,/): "))
if num_nam == "+":
    print(num1+num2)
elif num_nam=="-":
    print(num1-num2)
elif num_nam=="*":
    print(num1*num2)
elif num_nam=="/":
    if num2!=0:
        print(num1/num2)
    else:
        print("Ділення на нуль неможливе!")
else:
    print("Невідома операція")




