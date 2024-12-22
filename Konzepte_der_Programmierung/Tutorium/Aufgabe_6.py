a_list = [1, 2, 2, 1, 1, 2, 1]


def rec_counter(list_element: list, sec_list:list):
    if list_element <=1:
        return
    

#Aufgabe 3

sec_list = [1,1,2,3,4,5,6]
trip_list = [1,2,3,4,5,6,7]
fourth_list = [9,8,7,6,5,4]
bla = [2,4,3]
def if_sorted(unsorted: list):
    
    up = 1 
    down = 1
    count = 1
    for i in range(1,len(unsorted)):
        
        if unsorted[i-1]<unsorted[i]:
            count += 1
            up = 2
            down = 0
        if unsorted[i-1]==unsorted[i]:
            count+= 1
            up = 1
            
        if unsorted[i-1]>unsorted[i]:
            down = 2
            count += 1
            up = 0
        if unsorted[i-1]==unsorted[i]:
            count+=1
            down = 1
            count += 1
        
    
    return up, down
    
print(if_sorted(sec_list))