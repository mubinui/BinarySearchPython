def binary_search(list,left,right,elem):
    centre = int((left+right)/2)
    print(centre)
    if right>=left:
        if list[centre]== elem :
            print(">>match Found")

        elif list[centre]>elem:
            binary_search(list,left,centre-1,elem)

        elif list[centre]<elem:
            binary_search(list,centre+1,right,elem)


