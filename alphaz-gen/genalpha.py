def getA0(i,j,k,N):
	if k==10:
		return ("0, N-1", 0)
	if k==11:
		return ("N-1, 0", 1)
	if i==0 and j==0:
		return ("i, 1", k)
	elif j==0:
		return ("i-1, j", k)
	elif i==0:
		if k%2==0:
			return ("N-1-j, N-1", (k+2)%10)
		else:
			return ("N-1, j", (k+1)%10)
	else:
		return ("i-1, j", k)

def getA1(i,j,k,N):
	if k==10:
		return ("0, N-1", 2)
	if k==11:
		return ("N-1, 0", 3)
	if i==0 and j==0:
		if k%2==0:
			return ("N-1, N-1", (k+2)%10)
		else:
			return ("N-1, 0", (k+1)%10)
	elif j==0:
		if k%2==0:
			return ("i-1, N-1", (k+1)%10)
		else:
			return ("N-1, N-i", (k+2)%10)
	elif i==0:
		if k%2==0:
			return ("N-j, N-1", (k+2)%10)
		else:
			return ("N-1, j-1", (k+1)%10)
	else:
		return ("i-1, j-1", k)
	
def getA2(i,j,k,N):
	if k==10:
		return ("0, N-1", 4)
	if k==11:
		return ("N-1, 0", 5)
	if i==0 and j==0:
		if k%2==0:
			return ("0, N-1", (k+1)%10)
		else:
			return ("N-1, N-1", (k+2)%10)
	elif i==0:
		return ("i, j-1", k)
	elif j==0:
		if k%2==0:
			return ("i, N-1", (k+1)%10)		
		else:
			return ("N-1, N-1-i", (k+2)%10)
	else:
		return ("i, j-1", k)


def getA3(i,j,k,N):
	if k==10:
		return ("0, N-1", 6)
	if k==11:
		return ("N-1, 0", 7)
	if i==N-1 and j==N-1:
		if k%2==0:
			return ("0, N-1", (k-1)%10)
		else:
			return ("1, 0", (k-2)%10)
	elif i==N-1:
		if k%2==0:
			return("0, j", (k-1)%10)
		else:
			if j==0:
				return ("0,0",11)
			else:
				return ("N-j,0", (k-2)%10)
	elif j==N-1:
		return ("i+1, j",k)
	else:
		return ("i+1, j",k)

def getA4(i,j,k,N):
	if k==10:
		return ("0, N-1", 8)
	if k==11:
		return ("N-1, 0", 9)
	if i==N-1 and j==N-1:
		return ("0,0",(k-2)%10)
	elif i==N-1:
		if k%2==0:
			return ("0,j+1", (k-1)%10)
		else:
			return ("N-j-1, 0", (k-2)%10)
	elif j==N-1:
		if k%2==0:
			return ("0, N-1-i", (k-2)%10)
		else:
			return ("i+1, 0", (k-1)%10)
	else:
		return ("i+1, j+1", k)

def getA5(i,j,k,N):
	if k==10 or k==11: 
		return ("-1, -1", -1)
	if i==0 and j==0:
		return ("-1,-1",-1)
	elif i==N-1 and j==N-1:
		if k%2==0:
			return ("0, 1", (k-2)%10)
		else:
			return ("N-1, 0", (k-1)%10)
	elif i==N-1:
		return ("i, j+1", k)
	elif j==N-1:
		if k%2==0:
			if i==0:
				return ("0,0",10)
			else:
				return ("0, N-i", (k-2)%10)
		else:
			return ("i, 0", (k-1)%10)
	else:
		return ("i, j+1", k)


def getAx(i,j,k,N,x):
	funcs = [getA0, getA1, getA2, getA3, getA4, getA5]
	return funcs[x](i,j,k,N)

def getL(p,channel):
	seg = "ABCDEFGHIJKL"
	f=p[0]
	k=p[1]
	return channel+"_"+seg[k]+"["+f.replace(" ","")+",t-1]"
'''
for k in range(0,12):
	i=0
	j=0
	print seg[k]+'[i,j,t]='
	print '\tcase'
	print '\t\t{|t==0} : 0;' 
	print '\t\t{|i==0 && j==0} : '+getL(getA0(i,j,k,N))+' + '+getL(getA1(i,j,k,N))+' + '+getL(getA2(i,j,k,N))+' + '+getL(getA3(i,j,k,N))+' + '+getL(getA4(i,j,k,N))+';'
	if k!=10 and k!=11:
		i=N-1
		j=N-1
		print '\t\t{|i==N-1 && j==N-1} : '+getL(getA0(i,j,k,N))+' + '+getL(getA1(i,j,k,N))+' + '+getL(getA2(i,j,k,N))+' + '+getL(getA3(i,j,k,N))+' + '+getL(getA4(i,j,k,N))+' + '+getL(getA5(i,j,k,N))+';'
		i=0
		j=N-1
		print '\t\t{|i==0 && j==N-1} : '+getL(getA0(i,j,k,N))+' + '+getL(getA1(i,j,k,N))+' + '+getL(getA2(i,j,k,N))+' + '+getL(getA3(i,j,k,N))+' + '+getL(getA4(i,j,k,N))+' + '+getL(getA5(i,j,k,N))+';'
		i=N-1
		j=0
		print '\t\t{|i==N-1 && j==0} : '+getL(getA0(i,j,k,N))+' + '+getL(getA1(i,j,k,N))+' + '+getL(getA2(i,j,k,N))+' + '+getL(getA3(i,j,k,N))+' + '+getL(getA4(i,j,k,N))+' + '+getL(getA5(i,j,k,N))+';'
		i=0
		j=1
		print '\t\t{|i==0} : '+getL(getA0(i,j,k,N))+' + '+getL(getA1(i,j,k,N))+' + '+getL(getA2(i,j,k,N))+' + '+getL(getA3(i,j,k,N))+' + '+getL(getA4(i,j,k,N))+' + '+getL(getA5(i,j,k,N))+';'
		i=N-1
		j=1
		print '\t\t{|i==N-1} : '+getL(getA0(i,j,k,N))+' + '+getL(getA1(i,j,k,N))+' + '+getL(getA2(i,j,k,N))+' + '+getL(getA3(i,j,k,N))+' + '+getL(getA4(i,j,k,N))+' + '+getL(getA5(i,j,k,N))+';'
		j=0
		i=1
		print '\t\t{|j==0} : '+getL(getA0(i,j,k,N))+' + '+getL(getA1(i,j,k,N))+' + '+getL(getA2(i,j,k,N))+' + '+getL(getA3(i,j,k,N))+' + '+getL(getA4(i,j,k,N))+' + '+getL(getA5(i,j,k,N))+';'
		j=N-1
		i=1
		print '\t\t{|j==N-1} : '+getL(getA0(i,j,k,N))+' + '+getL(getA1(i,j,k,N))+' + '+getL(getA2(i,j,k,N))+' + '+getL(getA3(i,j,k,N))+' + '+getL(getA4(i,j,k,N))+' + '+getL(getA5(i,j,k,N))+';'
		i=1
		j=1
		print '\t\t{|} : '+getL(getA0(i,j,k,N))+' + '+getL(getA1(i,j,k,N))+' + '+getL(getA2(i,j,k,N))+' + '+getL(getA3(i,j,k,N))+' + '+getL(getA4(i,j,k,N))+' + '+getL(getA5(i,j,k,N))+';'
	else:
		print '\t\t{|} : 0;'
	print '\tesac;'
'''






