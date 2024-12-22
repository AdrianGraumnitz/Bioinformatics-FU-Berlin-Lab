def rev_digits(number:int):
    '''order = []
    concat = ''
    for i in range(len(str(number))):        
        order.insert(0, str(number)[i])
        print(order)
    for j in range(len(order)):
        concat += order[j]
    return concat'''
    return str(number)[::-1]
    
#print(rev_digits(123))

def list_length(lst: list):
    # Basisfall: Leere Liste hat Länge 0
    if lst == []:
        return 0
    # Rekursiver Fall: Zähle 1 und rufe die Funktion mit dem Rest der Liste auf
    return 1 + list_length(lst[1:])

#print(list_length([10,2,3,6]))

def rec_prod(prod_list: list):
    
    if prod_list == []:
        return 1
    
    return prod_list[0] * rec_prod(prod_list[1:])

#print(rec_prod([2,2,4]))

def rec_min(min_list: list = [1]):
    
    if len(min_list) == 1:
        return min_list[0]
    
    if min_list[0] < min_list[1]:
        min_list[1] = min_list[0]
        return rec_min(min_list[1:])
    
    return rec_min(min_list[1:])
    
print(rec_min([10,4,9,7]))


def reverse_number(n, result=0): #12, 3 / 1, 32, 
    # Basisfall: Wenn n zu 0 wird, ist die Umkehrung vollständig
    if n == 0:
        return result
    # Berechne das nächste Ergebnis und rufe die Funktion rekursiv auf
    else:
        return reverse_number(n // 10, result * 10 + n % 10)

# Beispielverwendung
number = 123
reversed_number = reverse_number(number)
#print(reversed_number)  # Ausgabe: 321
#print(1//10)


def rec_reverse(numb, arg = 0):
    if numb == 0:
        return arg
    return rec_reverse(numb//10, arg*10 + numb%10)

#print(rec_reverse(32984392849329843298123))