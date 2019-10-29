# from random import random
#
# class RandomIterator:
#     def __iter__(self):
#         return self
#
#     def __init__(self, k):
#         self.k = k
#         self.i = 0
#
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration
#
# def random_generator(k):
#     for i in range(k):
#         yield random()
#
# gen = random_generator(3)

def IsPrime(n):
   d = 2
   while n % d != 0:
       d += 1
   return d == n

def primes():
    a = 1
    i = 2
    while True:
        a += 1
        if IsPrime(a):
            yield a



print(list(itertools.takewhile(lambda x : x <= 31, primes())))