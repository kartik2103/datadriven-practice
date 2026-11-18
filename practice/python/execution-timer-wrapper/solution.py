import time


def make_timed(func):
#Original function mein kabhi 0 arguments hain, kabhi 1, kabhi 2.
#Isliye hum ek inner function banayenge.
#Kyunki hum original function ko directly execute nahi karna chahte.
#Hum chahte hain ki:
#1. Pehle timer start ho.
#2. Original function execute ho.
#3. Timer stop ho.
#4. Original output return ho.
    def wrapper(*args):
      start = time.time()
      #original function ka output.
      result = func(*args)
      end = time.time()
      elapsed = end - start
      print(elapsed)
      return result 
    return wrapper 

@make_timed
def answer():
  return 42


@make_timed
def double(n):
  return n * 2


@make_timed
def add(x, y):
  return x + y


@make_timed
def greet(greeting, name):
  return greeting + name


@make_timed
def pair(a, b):
  return [a, b]


JOBS = {
  "answer": answer,
  "double": double,
  "add": add,
  "greet": greet,
  "pair": pair,
}


def run_timed(job, args=None):
    if args is None:
       args = []
    
    return JOBS[job](*args)
  
