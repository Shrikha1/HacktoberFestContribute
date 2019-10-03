# A is array to be sort
# n is length of arr
def selection_sort(A,n):
    for i in range(n): 
        	mi= i 
        	for j in range(i+1, len(A)): 
        		if A[mi] > A[j]: 
        			mi = j 	 
        	A[i], A[mi] = A[mi], A[i] 

# call function by
# selection_sort(A,n)


