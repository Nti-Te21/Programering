list = [8, 4, 5, 6, 9 ,7, 15 ,10]
def listsort():
    print(list)
    list_length = len(list)
    for i in list:
        for tal in range(0,list_length-1):
            if list[tal] > list[tal+1]:
                list[tal],list[tal+1]=list[tal+1],list[tal]
    print(list)
listsort()