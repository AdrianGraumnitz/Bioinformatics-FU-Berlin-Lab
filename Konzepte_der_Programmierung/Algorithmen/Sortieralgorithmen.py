
# Selection Sort

# min(List[U], int) : int # U is an arbitrary type 
# Precondition: 0<=i<len(xs), the elements of xs are from a totally ordered universe. 
# Effect: None 
# Result: The index of the smallest element in xs[i:] is returned. 
'''Tests: Your exercise ;-) ''' 
def min(xs, i):
    n = len(xs) 
    m = i 
    for j in range(i+1, n):
        if xs[j] < xs[m]: # if we have a smaller element m 
            m = j
    return m


# selectionsort(List[U]) : NoneType 
# U is an arbitrary type 
# Precondition: The elements of xs are from a totally ordered universe. 
# Effect: The elements of xs are sorted in increasing order. 
# Result: None 
'''Tests: Your exercise ;-) '''
def selection_sort(xs):
    n = len(xs)
    for i in range(n):
        mini = min(xs, i)
        xs[mini], xs[i] = xs[i], xs[mini]
        print(xs)
    return xs

unordered = [4,5,3,2,8,6]
#print(selection_sort(unordered))


# Insertionsort

# insert(List[U], int) : NoneType # U is an arbitrary type 
# Precondition: 0<=i<len(xs), the elements on the postions 0...i-1 are sorted 
# Effect: the elements on the positions 0...i are sorted 
# Result: None 
'''Tests: Your exercise ;-)'''

def insert(xs, i):
    key = xs[i]
    j = i
    while(j > 0 and xs[j-1] > key):
        xs[j] = xs[j-1]
        j-=1
        print(xs)
    xs[j] = key
    return xs

#print(insert(unordered,3))

def insertion_sort(xs):
    
    for i in range(len(xs)):
        
        x = insert(unordered,i)
    return x

#print(insertion_sort(unordered))


# Mergesort

# merge(List[U], List[U], List[U]) : NoneType 
# U is an arbitrary type 
# Precondition: len(left) + len(right) == len(xs), left and right are sorted inc. 
# Result: None 
# Effect: The elements of left and right are in xs sorted increasingly.
'''Tests: Your exercise ;-)'''

def merge(left, right, xs):
    # l is the index of the first element of left, that has not been copied to xs 
    # r is the index of the first element of right, that has not been copied to xs
    l = 0
    r = 0
    while l + r < len(xs):
        if l == len(left): # No more elements in left
            xs[l + r] = right[r]
            r += 1
        elif r == len(right): # No more elements in right
            xs[l + r] = left[l]
            l += 1
        elif left[l] <= right[r]: # In left is the smaller element
            xs[l+r] = left[l]
            l += 1
        else: # left[l] > right[r] # In right is the smaller element
            xs[l+r] = right[r]
            r +=1
xs = [4, 2, 6, 3]
left = [2, 4]
right = [3, 6] #Perfekt zum lernen

merge(left, right, xs)
print(xs)

# mergesort(List[U]) : NoneType 
# U is an arbitrary type 
# Precondition: The elements of xs are from a totally ordered universe. 
# Effect: The elements of xs are sorted in increasing order.
# Result: None 
'''Tests: Your exercise ;-)'''

def mergesort(xs):
    n = len(xs)
    if n <= 1: # recursion anchor
         # take a copy of the left and right half of xs 
         # (This corresponds to the lower part of the figure from above.)
         return xs
    left = xs[:n//2]
    right = xs[n//2:]
    # sort the two copies recursively
    print(left,right)
    mergesort(left)
    mergesort(right)
    
    merge(left, right, xs)
    return xs

test1 = [3,5,4,8,9,2]
#print(mergesort(test1))
#print(test1[:len(test1)//2], test1[len(test1)//2:])

# Quicksort

# partition(List[U], int, int) : int # U is an arbitrary type
# Precondition: 0 <= start < end <=len(xs), 
# the elements of xs are from a totally ordered universe
# Effect: If l is the return value, then all elements are still in xs, and
#   for start <= i < l we have xs[i] < xs[l] and 
#   for l < i < end we have xs[l] <= xs[i] 
# Result: The index of the pivot element is returned 
'''Tests: Your exercise ;-)'''

def partition(xs, start, end):
    pivot = xs[start]
    l = start
    for i in range(start + 1, end):
        if xs[i] < pivot:
            l = l + 1
            xs[i], xs[l] = xs[l], xs[i]
    xs[start], xs[l] = xs[l], xs[start]
    return l

#print(partition(test1, 0 , len(test1)))

# quicksort(List[U]) : NoneType 
# U is an arbitrary type 
# Precondition: The elements of xs are from a totally ordered universe. 
# Effect: The elements of xs are sorted in increasing order. 
# Result: None 
'''Tests: Your exercise ;-)'''

def quicksort(xs):
    # This help function sorts the elements in xs between 
    # start (inclusive) and end (exclusive)
    def quicksort_help(start, end):
        if (end - start <= 1): # Recursion anchor
            return
        # The splitting part. 
        # This corresponds to the lower part of the figure above.
        split = partition(xs, start, end) # split the index of the pivot elements
        # sort the two remaining lists recursively
        quicksort_help(start, split)
        quicksort_help(split + 1, end)
    quicksort_help(0, len(xs))
    return xs
#print(quicksort(test1))

ZEILENLAENGE = 15
def blocksatz(woerter):
    zeilen = []
    # erstelle die einzelnen Zeilen
    wort_index = 0
    # Wiederhole, bis alle Wörter in Zeilen untergebracht sind
    while wort_index < len(woerter):
        # erstelle einer einzelnen Zeile
        #   Sammle die Wörter (sammle Wörter bis eine Zeile voll ist)
        #   Erstelle Zeile aus den Wörtern
        zeilen_woerter = [woerter[wort_index]]
        ges_laenge = len(woerter[wort_index])
        wort_index += 1
        while wort_index < len(woerter) and ges_laenge + 1 + len(woerter[wort_index]) <= ZEILENLAENGE:
            zeilen_woerter.append(woerter[wort_index])
            ges_laenge += 1 + len(woerter[wort_index])
            wort_index += 1
        print(zeilen_woerter)
        if len(zeilen_woerter) == 1:
            wort = zeilen_woerter[0]
            if len(wort) > ZEILENLAENGE:
                zeile = wort[:ZEILENLAENGE]
            else:
                zeile = wort
                for i in range(ZEILENLAENGE - len(wort)):
                    zeile += ' '
    return zeilen
bla = ['Huhuhu', 'das', 'ist', 'ja', 'krass', 'oder?']
print(blocksatz(bla))