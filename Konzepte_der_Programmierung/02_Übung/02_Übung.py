def triangle_area(height: float, length: float):
    '''
    Calculate the triangle area
    Args:
        height: float
        length: float
    Return:
        triangle area: float
    '''
    return (height*length)/2

triangle = triangle_area(5, 4)

print(triangle)


def leap_year(year: int):
    '''
    Calculate the leap year
    
    Args
        year: int
    Return
        Leap year: int
    '''
    return year%4==0


def mersenne_number(number:int):
    '''
    Calculate the mersenne number
    
    Args
        number: int
    Return
        mersenne number: int
    '''
    if number > 0:
        return((1 << number)-1)

print(mersenne_number(1))

def lowercase_letter(letter: str):
    '''
    Determinded the lowercase letter with the ascii table
    '''
    if ord(letter) > 64 and ord(letter) < 91 and len(letter)==1:
        return chr(ord(letter) + 32)
    
print(lowercase_letter('A'))

def cinema_ticket(age: int):
    return 10 if age < 12 else 12 if age <= 18 or age >= 65 else 14

print(cinema_ticket(19))


'''
Integer
1+1
7*300

Float
1.5 * 2.3
12.4/5

Bool
True or False
x<=y

String
'Hello' + 'World'
2*'Hello'
'''

# Aufgabe 3
#(d)

def count_numbers(number_1: int,
                  number_2: int,
                  number_3: int):
    count = 0

    if number_1 != number_2:
        count += 1
    if number_1 != number_3:
        count += 1
    if number_2 != number_3:
        count += 1
        
    print(f'Counted different numbers: {count}')
    print(f'Are the numbers different: {count == 3}')
    print(f'Are the numbers equal: {count == 0}')
    
  
count_numbers(1,1,1)
#(b)
