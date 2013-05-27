#! /usr/bin/env python3.3

n = 600851475143
i = 2

while i * i < n:
	while n % i == 0:
		n = n / i 
		print("\ti:\t",i)
		print("\tn:\t",n)
		print()

	i = i + 1

print("\ti:\t",i)
print("\tn:\t",n)
print()
