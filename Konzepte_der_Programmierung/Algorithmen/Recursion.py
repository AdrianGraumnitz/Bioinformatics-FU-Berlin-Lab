# Five questions:
# 1. Whats the simplest possible input?
# 2. Play around with examples and visualize
# 3. Relate hard cases to simpler cases
# 4. Generalize the pattern
# 5. Write code by combining recursive pattern with the base case

def rec_sum(number: int):
    if number == 0:
        return 0
    
    return number + rec_sum(number-1)


number = 5

#print(rec_sum(number))

def grid_paths(n,m):
    if n == 1 or m == 1:
        return 1
    
    return grid_paths(n-1,m) + grid_paths(n, m -1)



#print(grid_paths(3,3))

def count_partitions(n, m):
    if n == 0 or n == 1:
        return 1
    if m == 0 or  n < 0:
        return 0
    return count_partitions(n-m, m) + count_partitions(n, m-1)

print(count_partitions(-1,2))