seconds_input=int(input('Введіть кількість секунд ( від 0 до 8640000): ' ))
days,remainder=divmod(seconds_input,24*60*60)
hours,remainder=divmod(remainder,60*60)
minutes,seconds=divmod(remainder,60)

if days % 10 ==1 and days % 100 !=11:
    day_word="день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word="дні"
else:
    day_word="днів"
time_str=f"{days} {day_word},{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(time_str)
