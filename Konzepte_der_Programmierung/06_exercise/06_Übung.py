#Authors: Miguel Angel Gama Marroquin und Adrian Graumnitz

#Aufgabe 1

def iter_merge_sort(unsorted: list):
    '''
    Peforms an iterative merge sort.Prepare function for the merge. 
    Slices the unsorted list in an iterative way and gives the slices as an argument for the merge
    
    Args
        unsorted(list): Takes unsorted list as an argument
    
    '''
    size = 1
    while size < len(unsorted):
        left = 0
        while size + left < len(unsorted):
            #right = min(left + size * 2, len(unsorted))
            if left + size * 2 < len(unsorted):
                right = left + size * 2
            else:
                right = len(unsorted)
            iter_merge(front_part = unsorted[left: left + size],
                       back_part = unsorted[left + size: right],
                       unordered_list = unsorted,
                       start_point = left)
            left += size * 2
        size *= 2
            

def iter_merge(front_part: list,
               back_part: list,
               unordered_list: list,
               start_point: int):
    '''
    Merges to sorted sublists in the original list
    
    Args
        frontpart(list): First sublist
        backpart(list): Second sublist
        unordered_list(list): original list
        start_point(int): The index where original list gets merged with the sublists 
    '''
    left = 0
    right = 0
    while left < len(front_part) and right < len(back_part):
        if front_part[left] < back_part[right]:
            unordered_list[start_point] = front_part[left]
            left += 1
        else:
            unordered_list[start_point] = back_part[right]
            right += 1
        start_point += 1
    
    while left < len(front_part):
        unordered_list[start_point] = front_part[left]
        left += 1
        start_point += 1
        
    while right < len(back_part):
        unordered_list[start_point] = back_part[right]
        right += 1
        start_point += 1

test1 = [4,5,3,7,1,9,8,2,6]  
test2 = [7,5,8,4,2,1,8,3,9,6,] 
#iter_merge_sort(test2)
#print(test2)


# Aufgabe 2
# a)

def bubblesort(unsorted_list: list):
    '''
    The bubblesort algorithmen compares the numbers pair wise and swaps them inplace from the smallest on the left to highest on the right
    
    Args
        unsorted_list(list): The list that gets ordered
    '''
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list)-1-i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list

def flour_sack_comparison(sorted_list: list):
    '''
    Compares the weights of adjacent elements in a sorted list to find flour sacks that differ by exactly 10 grams.
    
    Args
        sorted_list(list): Takes a sorted list
        
    Return
        flour_sack_list(list): Gives the number of the "flour sacks" back not the index of the elements
    '''
    flour_sack_list = []
    for k in range(1,len(sorted_list)):
        if sorted_list[k] - sorted_list[k-1] == 10:
            flour_sack_list.append((k + 1, sorted_list[k]))   # Notation: I dont want to use the normal Index I want the number of the Flour Sack, in the real world the doesn't start count by 0
        
    return flour_sack_list

test3 = [1020, 1070, 1080, 2000, 2010] 

flour_sack_list = (flour_sack_comparison(bubblesort(test3)))
#print(f'The bigger flour sacks with a difference of 10 grams are:: {[f'Number: {flour_sack_list[i][0]} with a weight of: {flour_sack_list[i][1]} grams ' for i in range(len(flour_sack_list))]}')

# b)

# I know its not the perfect "binary search" implementation but this is our idea and not copied and it works also well with concept of "Divide and Conquer" :D
def binary_sort2(sorted_list: list,
                number: int):

    left = sorted_list[:len(sorted_list)//2]
    right = sorted_list[len(sorted_list)//2:]
            
    return binary_search(left,
                          right,
                          number)
        
    
def binary_search(left: list,
                  right: list,
                  number: int):
    
    if len(right) == 1 and right[0] == number:
        return True
        #return right[0]
    elif len(left) == 1 and left[0] == number:
        return True
        #return left[0]
    elif len(right) == 1  and right[0] != number:
        return False
        #return number
    if len(left) == 1 and left[0] != number:
        return False
        #return number
            
    if number < right[0]:
        return binary_search(left[:len(left)//2], 
                             left[len(left)//2:],
                             number)
    if number > left[len(left)-1]:
        return binary_search(right[:len(right)//2], 
                             right[len(right)//2:],
                             number)
    
    
sorted_list = [1,2,3,4,5,6,10,11,12]

#print(binary_sort2(sorted_list, 10000))


gouda = [150,200, 1000, 1110]
emmentaler = [100, 450, 900,1000]
roquefort = [34, 92,134,700]

gouda = [150]
emmentaler = [100, 450]
roquefort = [34, 92,134]

cheese = [gouda, emmentaler, roquefort]

def a_lot_of_cheese(cheese: list[list]):
    '''
    Compares the elements of a two-dimensional list to a weight number of 1234.
    
    Args:
        cheese (list): A two-dimensional list containing three sublists, each representing a different type of cheese 
                       (Gouda, Emmentaler, Roquefort) with their corresponding weights.
                       cheese[0] is for Gouda, cheese[1] is for Emmentaler, cheese[2] is for Roquefort.
    
    Returns:
        dict: A dictionary with the indices (1-based) of the cheeses that sum up to 1234 grams, or a message if no combination is found.
    '''
    for i in range(len(cheese[0])):
        weight = 1234 - gouda[i]
        
        for j in range(len(cheese[1])):
            new_weight = weight - emmentaler[j]
            
            if binary_sort2(cheese[2],
                         new_weight):
                return f'There is a combination:\n Gouda number: {i + 1}\n Emmentaler number: {j + 1}\n Roquefort number: {cheese[2].index(new_weight) + 1}'
                # Like in the other exercise i start to count at 1 cause it exist no cheese with number 0
            
    return f'Therea are no combination of Gouda, Emmentaler and Roguefort to get the exact weight of 1234'            
   
print(a_lot_of_cheese(cheese))



