input = [55, 64, 76, 98, 34, 67, 30]




def init(AVG):
    sum = 0
    for element in AVG:
        sum += element
    return sum/len(AVG) 



def sorter(IN):
    smaller = []
    average = init(IN)
    while len(IN) > 1:
        for element in IN:
            if element < average:
                smaller.append(element)
        IN = smaller
        smaller = []
        print(IN)
        average = init(IN)

    



print(sorter([64, 76, 98, 67]))