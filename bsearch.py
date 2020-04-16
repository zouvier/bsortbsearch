''' Created by Zoumana Cisse'''
lst = [222,289,190,173,164,34,178,81,64,163,177,220,151,149,144,85,169,275,167,54,187,95,104,56,203,79,287,280,147,141,30,62,258,112,58,148,254,283,15,216,154,38,8,126,223,152,98,46,294,202,298,113,90,210,218,237,136,290,226,158,122,268,91,140,117,295,114,229,248,118,246,12,47,65,204,53,32,171,212,133,194,189,269,7,67,234,135,87,296,102,130,33,127,21,193,231,191,228,297,18,86,69,24,236,49,157,162,196,291,215,10,251,59,161,20,265,11,16,249,245,77,84,101,23,134,207,74,179,68,221,214,80,168,96,243,155,160,165,105,108,36,55,124,40,281,39,4,82,63,264,17,110,146,129,208,119,170,35,174,184,5,42,282,14,292,142,232,273,26,60,57,224,185,219,156,3,252,235,70,286,293,99,25,255,103,1,66,192,284,37,175,22,198,123,225,106,195,276,27,261,88,253,109,9,93,143,274,279,13,288,145,83,256,201,181,262,299,72,240,131,115,120,139,6,125,31,271,182,52,239,200,121,263,242,43,159,138,128,107,97,259,247,150,48,183,172,89,100,266,277,2,285,76,209,41,197,278,78,227,153,137,213,241,51,300,75,29,50,206,71,267,250,260,205,230,166,92,176,270,94,211,111,28,188,73,186,19,116,44,45,257,233,238,132,180,272,244,199,61,217]

# bubble sort algorithim
def sorting_alg(listed):
    index_length = len(listed)-1
    sortedd = False
    while not sortedd:
        sortedd =True
        for i in range(0,index_length):
            if listed[i] > listed[i+1]:
                sortedd = False
                listed[i], listed[i+1] = listed[i+1], listed[i]
    return listed

# binary search algorithm
def number_search(listing, target):
    index_length = len(listing)-1
    found = False
    min = 0
    max = index_length
    '''checks if the number we are targeting is at either ends of the list
    if its higher or lower than the middle point the respective point will switch
    with the middle point and become the new value (shown below)'''
    while not found:
        middle = int((min + max)/2)
        if listing[middle] == target:
            found = True
        elif listing[middle] > target:
            max = middle
        elif listing[middle] < target:
            min = middle
    print('the Number ' + str(target) + ' was found at index: ')
    return middle


s_listed = sorting_alg(lst)

print(number_search(s_listed, 4))

indexed = number_search(s_listed, 4)

print(indexed)
