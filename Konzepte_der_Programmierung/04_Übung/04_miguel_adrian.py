import random

# Authors: Miguel Angel Gama Marroquin und Adrian Graumnitz
#List of References:
#harmonic harmonic_measure: https://www.sciencedirect.com/topics/mathematics/harmonic-measure
#recursion in Python: https://www.python-kurs.eu/rekursive_funktionen.php
#Docstrings created in co work with ChatGPT


def harmonic_measure(range_of_number: int):
    """
    Calculate the harmonic measure of a given number.

    Args:
        range_of_number (int): The number for which the harmonic measure is calculated. 
                                Must be a positive integer.

    Returns:
        float: The harmonic measure, calculated as the ratio of the input number 
               to the harmonic sum.
    """
    harmonic_sum = 0  
    for i in range(1, range_of_number + 1): 
        harmonic_sum += 1 / i
    return range_of_number / harmonic_sum  

#print(harmonic_measure(5))


# 1. a,b
def gotta_catch_em_all(n_to_catch:int,
                       num_experiment: int):
    '''
    """
    Simulates a series of experiments where randomly selected numbers (e.g., people or objects) 
    are repeatedly "hit" until each number has been hit at least once.
    
    Parameters
    ----------
    n_to_catch : int
        The number of numbers that should be "hit" in each experiment.
        
    num_experiment : int
        The number of experiments to be conducted.
        
    Returns
    -------
    str
        A formatted string containing:
        - Max values (max_value): The maximum number of hits for each number across experiments
        - Min values (min_value): The minimum number of hits for each number across experiments
        - Average hits (measure): The average number of hits per number across all experiments
        - List of tries (count_list): The number of attempts in each experiment until all numbers were hit
        - Highest frequent number: The number with the highest total number of hits across experiments
        - Frequent: The total hit count for the most frequently hit number
    
    Example
    -------
    >>> gotta_catch_em_all(10, 100)
    Max values: [...]
    Min values: [...]
    Measure: [...]
    List of tries: [...]
    Highest frequent number: ...
    Frequent: ...
    """
    '''
    max_value = [0] * n_to_catch
    min_value = [1000] * n_to_catch
    measure = [0] * n_to_catch
    count_list = [0] * num_experiment
    frequent = [0] * n_to_catch
    index = 0
    number = 0
    
    for j in range(num_experiment):
        empty_list = n_to_catch*[0]
        count = 0
        
        while 0 in empty_list:
            empty_list[random.randrange(n_to_catch)] += 1
            count+=1
        #print(empty_list)
        
        for i in range(len(empty_list)):
            if empty_list[i] > max_value[i]:
                max_value[i]= empty_list[i]
            if empty_list[i] < min_value[i]: 
                min_value[i] = empty_list[i]
                
            frequent[i] += empty_list[i]
            measure[i] += empty_list[i]
        count_list[j] = count
        
        for k in range(len(frequent)):
            if frequent[k] > number:
                index = k+1
                number = frequent[k]
            
    measure = [value / num_experiment for value in measure]
    
    return f'Max values: {max_value}\nMin values: {min_value}\nMeasure: {measure}\nList of trys: {count_list}\nHighest frequent number: {index}\nFrequent: {number} '


#print(gotta_catch_em_all(10,100))
#print(gotta_catch_em_all(100,100))
#print(gotta_catch_em_all(1000,100))

# 2.
#a) Die Idee ist durch eine Rekursion (eine wiederholte aufrufung der selben Funktion) die annäherung an die Wurzel aus dem Gewünschten zu erhalten. Die Funktion kann das mit einem beliebigen x Wert diese ziel erreicht werden kann
#b)
def square_with_newton(square_number: float,
                       guess: int,
                       count: int = 10):
    """
    Calculate the square root of a number using Newton's method (also known as 
    the Newton-Raphson method).

    Args:
        square_number (float): The number whose square root is to be calculated.
                                Must be a positive number.
        guess (int): The initial guess for the square root. A positive number is expected.
        count (int, optional): The number of iterations to perform for refining the guess.
                               Default is 10.

    Returns:
        float: The estimated square root of the given number after the specified number 
               of iterations.
    """
    
    if count == 0:
        return guess
    new_guess = (1/2)*(guess + (square_number/(guess)))
    
    return square_with_newton(square_number=square_number,
                              guess = new_guess,
                              count=count -1)
    

#print(square_with_newton(17, 25))

#c)
# Die Idee ist sich dem z Wert durch eine Schleife anzunähern. Die Schleife ist genauer (zumindest auf meinem Rechner, da ich ab einem bestimmten Count keine Rekursionen mehr durchführen kann).
# Dafür ist Rekursion schneller (Effizienter). Wir finden den Zweiten Ansatz besser der er leichter nachzuvollziehen ist.
def square_search(number: int):
    """
    Approximate the square root of a given number using interval halving.

    Args:
        number (int): The number whose square root is to be approximated. Must be a positive number.

    Returns:
        float: The approximated square root of the given number after interval halving.
        int: The number of iterations it took to find the approximation.
    """
    z: int
    x = 1
    y = number
    count = 0
    
    for _ in range(100):
        z = (x+y)/2
        if z**2> number:
            y = z
        else:
            x = z
            count += 1
    
    return z

#print(square_search(10000))

'''
# 3.
# Wenn der Zeilen 108 und 113 nicht auskommentiert wären würden bloß die Zeilen 102-107 bzw. 102-112 ausgeführt werden. Und bloß Zeile 104, 106 bzw 104, 106, 109, 112 ausegegeben werden. 
a = [1, 3, (4, 2)]              # Gültig
b = (a, a, [1, 5, 4, 3])        # Gültig
print(b[1][2])                  # Gültig Ausgabe: (4, 2)
b[1][2] = "wer"                 # Gültig 
print(b)                        # Gültig Ausgabe: ([1, 3, 'wer'], [1, 3, 'wer'], [1, 5, 4, 3])
a[2][1]                         # Gültig
#a[2][1] = "wann"               # Ungültig Tupel ist immutable
print(b)                        # Gültig Ausgabe: ([1, 3, 'wer'], [1, 3, 'wer'], [1, 5, 4, 3])
b[2][1]                         # Gültig
b[2][1] = ["wo", "wie"]         # Gültig
print(b)                        # Gültig Ausgabe: ([1, 3, 'wer'], [1, 3, 'wer'], [1, ['wo', 'wie'], 4, 3])
#b[2] = [2, 4]                  # Ungültig Tupel ist immutable
print(b)                        # Gültig Ausgabe: ([1, 3, 'wer'], [1, 3, 'wer'], [1, ['wo', 'wie'], 4, 3])
a = "warum"                     # Gültig
print(b)                        # Gültig Ausgabe: ([1, 3, 'wer'], [1, 3, 'wer'], [1, ['wo', 'wie'], 4, 3])
'''