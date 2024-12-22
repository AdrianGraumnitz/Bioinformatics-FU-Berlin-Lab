import time




def block2(phrase: list,
           row: int = 80):
    new_phrase = ''
    count = 0
    for i in range(len(phrase)):
        letter_count = 0
        word = phrase[i]
        for j in range(len(phrase[i])):
            letter_count +=1
            
            print(len(phrase[i]) + len(new_phrase))
            if len(phrase[i] + new_phrase) - row == 1:
                new_phrase += ' ' + phrase[i] + '\n'
                
                
                               
            if count == row: #row and phrase[i][j] != ' ':
                if letter_count != len(phrase[i]):
                    new_phrase += '-' + '\n' + phrase[i][j]
                else:
                    new_phrase += '\n' + phrase[i][j]
            else:
                new_phrase += phrase[i][j]
            count += 1
            
            if letter_count == len(phrase[i]):      
                new_phrase += ' '
           
            
        #new_phrase += ' '
        count+=1
        print()
    print(new_phrase)

phrase = ['Auf', 'ein', 'neues', 'Mal', 'sehen', 'wie', 'das', 'alles', 'funkioniert', 'und', 'so', 'weiter', 'und', 'so', 'fort','kkk', 'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk']

#block2(phrase)
#print(len('Auf ein neues Mal sehen wie das alles funkioniert und so weiter und so fort kkkk'))




# 2a)
def rek_fib(n):
     
    if n <= 1:
        return n
    
    return ((rek_fib(n-1))+(rek_fib(n-2)))

#print(rek_fib(5))

# c)
def fibonacci_recursive_with_dict(n, memo=None):
    if memo is None:
        memo = {}  
    if n in memo:
        return memo
    
    
    if n <= 1:
        memo[n] = n
        return memo
    
    
    memo = fibonacci_recursive_with_dict(n - 1, memo)
    memo = fibonacci_recursive_with_dict(n - 2, memo)
    
    
    memo[n] = memo[n - 1] + memo[n - 2]
    
    return memo
    
#print(fibonacci_recursive_with_dict(4))

#   n   3
#       (3-1)           (3-2)
#   n   (2)             +1  
#       (2-1)  (2-2)
#   n   +1      +0


start_time = time.time() 
#print(fibonacci_recursive_with_dict(35))
#print(rek_fib(35))
end_time = time.time() 
#print(end_time-start_time)

def iter_fibonacci(number):
    
    start_time = time.time()
    if number == 0:
        return [], start_time - time.time()
    if number == 1:
        return [1], start_time - time.time()
    
    fib_list = [1,1]
    
    for _ in range(2, number):
        fib_list.append((fib_list[-1]+fib_list[-2]))
        
    end_time = time.time()
    
    return fib_list, end_time-start_time

#print(iter_fibonacci(35))

#e) Variante 1
def opt_iter_fibonacci(number):
    
    start_time = time.time()
    
    fib_list = [1,1]
    
    for _ in range(2,number-1):
        
        fib_list[0] = fib_list[-1]+ fib_list[-2]
        fib_list[1] = fib_list[-1]+ fib_list[-2] 
        
    end_time = time.time()
    return fib_list, end_time-start_time

print(opt_iter_fibonacci(5))

#e) Variante 2
def opt_iter_fibonacci2(number):
    count1 = 1
    count2 = 1
    
    for _ in range(2,number):
        print(count1)
        count1 += count2
        print(count2)
        count2 += count1
    return count1,count2

#opt_iter_fibonacci2(35)



# 3b) Ausgaberklärung in der PDF
def f(x, y):
    print("f: x = " + str(x) + ", y = " + str(y) + ".")
    x = x + y
    y = 2 * x
    print("f: x = " + str(x) + ", y = " + str(y) + ".")
a = 2
b = 4
#print("main: a = " + str(a) + ", b = " + str(b) + ".")
#f(a, b)
#print("main: a = " + str(a) + ", b = " + str(b) + ".")

#c) Ausgaberklärung in der PDF
def f():
    print("Hier ist f.")
    return 5
def g(a):
    x = a
    y = 2 * a
    return x + y
#z = g(f())
#print("main: z = " + str(z) + ".")


#test_list = [1,2,3,4, 5, 6, 7]

#print(test_list[-2:])