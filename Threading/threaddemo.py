import threading

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_prime(n):
    for i in range(2, n + 1):
        if isPrime(i):
            print(f"Prime : {i}", '\n')

def fibonacci(n):
    if n < 1:
        return "NA"
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    print(f"\n{n}th fibonacci no. is {b}", '\n')
    
prime_thread = threading.Thread(target=generate_prime, args=(20, ))
fibonacci_thread = threading.Thread(target=fibonacci, args=(9, ))

prime_thread.start()
fibonacci_thread.start()

prime_thread.join()
fibonacci_thread.join()