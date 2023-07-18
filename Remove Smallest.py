t=int(input())
for _ in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	a=sorted(a)
	s="YES"
	for i in range(n-1,0,-1):
		if a[i]-1>a[i-1]:
			s="NO"
			break
	print(s)
