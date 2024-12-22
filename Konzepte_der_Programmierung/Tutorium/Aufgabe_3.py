#2 (a)
def asc_desc(number1: int,
             number2: int,
             number3: int):
    print('Ascending') if number1<number2<number3 else print('Descending') if number1>number2>number3 else print('No order')
    
#asc_desc(3,2,3)

# 2(b)
def product(list_number: list):
    '''
    Return the product of the numbers in a list
    
    Args
        list_number: list
    
    Return
        number: int
    '''
    i = 0
    number = 1
    while i < len(list_number):
        number *= list_number[i]
        i+=1
    return number

print(f'The product of the numbers is: {product([2,4,2])}')


def multi():
    new_number = 1
    var = 0
    while var !=1:
        var = int(input('Give a number: '))
        new_number*= var
    print(new_number)   


def wind_velocity(vel):
    
    if vel < 4:
        print('leiser Zug')
    elif vel < 7:
        print('leichte Prise')
'''
< 1 Windstille
[1, 4) leiser Zug
[4, 7) leichte Brise
[7, 11) schwache Brise
[11, 16) m¨aßige Brise
[16, 22) frische Brise
[22, 28) starker Wind
[28, 34) steifer Wind
[34, 41) st¨urmischer Wind
[41, 48) Sturm
[48, 56) schwerer Sturm
[56, 64] orkanartiger Sturm
> 64 Orkan
'''

wind_velocity(input())