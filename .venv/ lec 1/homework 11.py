import string
user_input=input('Введіть літери через дефіс,напр.а-с: ')
start, end =user_input.split('-')
letters=string.ascii_lowercase+string.ascii_uppercase
start_index=letters.index(start)
end_index=letters.index(end)
print(letters[start_index:end_index+1])

