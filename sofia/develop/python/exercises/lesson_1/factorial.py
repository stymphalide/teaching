
def factorial(n):
	result = 1

	for i in range(1,n+1):
		result = result * i
	return result

def factorial_rec(n):
	if n==0:
		return 1
	else :
		return n*factorial_rec(n-1)
def factorial_tail_rec(n, res=1):
	if n == 0:
		return res
	else:
		return factorial_tail_rec(n-1,res*n)


n = input("type n: ")
n = int(n)

result = factorial(n)

res_string = str(result)

print(len(res_string))


