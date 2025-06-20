def bubble_sort(data):
    # TODO: Implement bubble sort
    length = len(data)
    for pass_num in range(length -1,0,-1):
        for i in range(pass_num):
            if data[i]>data[i + 1]:
                #manual swap without tuple unpacking
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
    return data            

