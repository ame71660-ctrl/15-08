lists=[[[0, 1, 0, 12, 3],[0],[1, 0, 13, 0, 0, 0, 5],[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]]]
for my_list in lists[0]:
    zeros=my_list.count(0)
    non_zeros=[x for x in my_list if x!=0]
    result=non_zeros +[0]*zeros
    print(f"{my_list} -> {result}")
