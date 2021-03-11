# 2. Sum of three Integer adds to ZERO
#    a. Desc -> A program with cubic running time. Read in N integers and counts the
#       number of triples that sum to exactly 0.
#    b. I/P -> N number of integer, and N integer input array
#    c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
#    d. O/P -> One Output is number of distinct triplets as well as the second output is to print the distinct triplets.

from numpy import zeros


# calculating triplets of sum zero
def find_triplets(arr_, len_):
    ls = []
    found = False
    for i in range(0, len_-2):
        for j in range(i+1, len_-1):
            for k in range(j+1, len_):
                if arr_[i] + arr_[j] + arr_[k] == 0:
                    ls.extend([arr_[i], arr_[j], arr_[k]])
                    found = True
    if not found:
        print("Triplets of sum zeros doesn't exist")
        exit()
    else:
        return ls


# separate all the triplets of sum zero from list
def separate(triplet_):
    t = 3
    while t < len(triplet_):
        triplet_.insert(t, ';')
        t += 4
    return triplet_


if __name__ == '__main__':
    try:
        len_arr = int(input('Enter how many elements you want to enter to get a triplet of sum zero : '))
        # Define array
        arr = zeros(len_arr, int)
        # Taking user inputs from user
        for d in range(len_arr):
            print('Enter ', (d+1), ' element : ', end='')
            arr[d] = int(input())
        # check triplets of sum equals to zero
        triplet = find_triplets(arr, len_arr)
        len_triplet = len(triplet)
        # print the triplets
        print('Total ', len_triplet // 3, ' triplets found of sum zero!')
        # separate triplets
        triplets = separate(triplet)
        # print all the triplets of sum zero
        for item in triplets:
            print(item, ' ', end='')
    except Exception as e:
        print(e)
