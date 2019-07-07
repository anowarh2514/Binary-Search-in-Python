def Binary_Search(list,n):
    low = 0
    up = len(list) - 1
    while low <= up:
        mid = (low + up) // 2
        if list[mid] == int(n):
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                low = mid + 1
            else:
                up = mid - 1
    return False

pos = -1

list = [1,5,8,10,15,18,21,25,29,30,33,35,38,42,45,48,50,52,54,60]

n =input("Input The Number You Searching For = ")

if Binary_Search(list,int(n)):
    print("The Number Is Found At: ", pos+1)
else:
    print("Not Found")
