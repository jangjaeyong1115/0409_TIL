n,k = map(int,input().split())
max_n = 0
for i in range(1,k+1):
	num = n*i
	rev_str = int(str(num)[::-1])
	max_n = max(max_n,rev_str)

print(max_n)