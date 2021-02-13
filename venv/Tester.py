import Search as src


x = int(input("Input a number bro "))

list01 = []
for a in range(x):
    y=int(input())
    list01.append(y)

search_item = int(input())

src.binary_search(list01, 0, len(list01),search_item)
