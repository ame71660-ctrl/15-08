lists = [[0, 1, 7, 2, 4, 8],[1, 3, 5],[6],[]]
for my_list in lists:
   if not my_list:
    print(f'{my_list} => 0')
   else:
    even_elements=my_list[::2]
    total=sum(even_elements)*my_list[-1]
    if len(even_elements)>1:
        print(f"{my_list} => ({ '+'.join(str(x)for x in even_elements)}) * {my_list[-1]} = {total}")
    else:
        print(f"{my_list} => {total}")

