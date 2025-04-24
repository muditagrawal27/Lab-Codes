def prime_factors(n, div=2):
    if n<= 1:
        return []
    if n % div == 0:
        return [div] + prime_factors(n//div,div)
    else:
        return prime_factors(n, div+1)

n = int(input("Enter a positive integer: "))
fac = prime_factors(n)
print("Prime factors of",n,"are:",fac)