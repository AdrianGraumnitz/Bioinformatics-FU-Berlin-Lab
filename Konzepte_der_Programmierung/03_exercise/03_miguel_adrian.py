import random
import matplotlib.pyplot as plt

#Authors: Miguel Angel Gama Marroquin and Adrian Graumnitz


#2.(a)
def pyramid(number: int):
    '''
    Prints a centered pyramid of numbers from 1 to the specified number.
    
    Args:
        number(int): The height of the pyramid
    '''
    
    row = ''
    space = number
    for i in range(1, number + 1):
        print(space * ' ', row + str(i) + row[::-1])
        row += str(i)
        space -= 1
    
# Uncomment for execution
#pyramid(int(input('Give a number for height of the triangle:')))

#(b)
def inf_sum(num: int):
    '''
    Calculates the sum of all integers from 1 to a specified number.

    Args:
        num (int): The upper limit of the range to sum. Must be a positive integer.

    Returns:
        int: The sum of all integers from 1 to `num`.
    '''
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum
#print(inf_sum(int(input('Give a number ' ))))

def gauß(num):
    '''
        Calculates the sum of all integers from 1 to a specified number with Gauß algorithm.
        
        Args
            num (int): The upper limit of the range to sum. Must be a positive integer.

        Returns:
            int: The sum of all integers from 1 to `num`.

    '''
    return int((num*(num + 1))/2)

#print(gauß(int(input('Give a number ' ))))

#(c)

def calculate(num1: int,
              num2: int):
    '''
    Divide two numbers, if the iterator arrives at 5 the program stops.
    
    Args
        num1 (int): First number
        num2 (int): Second number
    '''
    for i in range(num1,-1, -1):
        if i==10:
            break
        print(i / num2)
        
#calculate(100,2)

def forever_alone(list_months: list):
    '''
    Give's out the month without the february
    
    Args
        list_months (list): includes all months of the year
    '''
    for i in list_months:
        if i == 'february':
            continue
        print(i)
        
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#forever_alone(months)




#d)
def measure():
    '''
    Calculates the average of a series of user-inputted numbers.    
    '''
    num = 1
    total = 0
    count = 0
    while num != 0:
        num = int(input('Please give a number '))
        if num == 0:
            break
        total += num
        count += 1
    print(f'Measure: {total/count}')
        
        
#measure()

#3 (a)(b)
def coin_of_destiny(repeat: int = 0,
                    step: int = 0,
                    count: int = 0):
    '''
    Determines the average number of coin tosses needed to reach a specified step value,
    or simulates a sequence of coin tosses for plotting.

    Args:
        repeat (int): The number of simulations to run to calculate the average coin tosses needed to reach `step`.
        step (int): A positive integer representing the target value to reach through coin tosses.
        count (int): If non-zero, the function simulates `count` coin tosses and returns the resulting states at each toss.

    Returns:
        dict: A dictionary representing the state at each coin toss for plotting if `count` is specified.
        float: The average number of tosses needed to reach `step`.
    '''
    num = 0
    count_list =[]
    total = 0
    diagram = {}
    
    if count != 0:
        for i in range(count):
            coin = random.randint(0, 1)
            
            if num == 0: 
                num = 1
            if coin == 0:
                num -= 1
            else:
                num += 1
                
            diagram[i] = num
        return diagram
    
    for _ in range(repeat):
        num = 0
        count = 0
        while num != step:
            coin = random.randint(0, 1)
            
            if num == 0: 
                num = 1
            if coin == 0:
                num -= 1
            else:
                num += 1
            count += 1
        count_list.append(count)
        
        
    for i in range(len(count_list)):
        total += count_list[i]
    return total/len(count_list)

step = 20
repeat = 1000
print(f'Average coin throws to arrive {step} steps: {coin_of_destiny(repeat = repeat, step = step):.2f} ')
diagramm = coin_of_destiny(count = 100)

plt.figure('Zufalls Spaziergang')
plt.title('Zufalls Spaziergang')
plt.plot(diagramm.keys(), diagramm.values())
plt.xlabel('Coin throw')
plt.ylabel('Place')
plt.show()


