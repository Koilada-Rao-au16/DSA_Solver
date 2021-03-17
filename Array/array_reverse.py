# Iterative python program to reverse an array


def reverseList(self):
    print(self[::-1])

self = [1,2,3,4,5]
print(self)
print("reverse list is ")
reverseList(self)

# method 2

def reverseList(A,start,end):
    if start >= end:
        return

    A[start],A[end] = A[end],A[start]
    reverseList(A, start+1 , end-1)
A = [1,2,3,4,5]
print(A)
reverseList(A, 0, 4)
print("reversed list is")
print(A)

# time complexity O(n)



