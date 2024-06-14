def half_pyramid(n):
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			if i+j<=n:
			    print(" " )
			else:
			    print("* ",end="")
print("\r")

# Example: Print a half pyramid with 5 rows
n = 5
half_pyramid(n)
