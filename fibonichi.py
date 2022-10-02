def fibonacci(n):
  if n <= 1:
        return n
  else:
        return(fibonacci(n-1) + fibonacci(n-2))
print(fibonacci(13))
print(fibonacci(14))
print(fibonacci(15))
print(fibonacci(16))