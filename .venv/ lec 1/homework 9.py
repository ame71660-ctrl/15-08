while True:
    num1=float(input("Введіть перше число: "))
    num2=float(input("Введіть друге число: "))
    operator=input("Введіть операцію (+,-,*,/):) ")

    if operator == "+":
        result= num1+num2
    elif operator == "-":
        result=num1-num2
    elif operator == "*":
        result =num1*num2
    elif operator == "/":
        if num2!=0:
            result=num1/num2
        else:
            print("Помилка: ділення на нуль!")
            continue
    print("Результат",result)

    cont =input("Бажаєте продовжити? (yes/y or not/n): "). lower()
    if  cont not in ("yes", "y", "no", "n"):
        print("Какулятор завершено ")
        break



