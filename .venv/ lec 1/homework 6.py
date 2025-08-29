list=[[1, 2, 3, 4, 5, 6],[1, 2, 3],[1, 2, 3, 4, 5],[1],[]]
for my_list in list:
    if len(my_list)==0:
        result=[[],[]]
    else:
        mid=(len(my_list)+1)//2
        result=[my_list[:mid],my_list[mid:]]
    print(f"{my_list}=>{result}")
