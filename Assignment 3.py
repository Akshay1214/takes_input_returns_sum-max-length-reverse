lst = []                                              # Creating an empty list
n = int(input("Enter number of elements : "))         # Number of elements as input
for i in range(0, n):                                 # Iterating till the range
	ele = int(input())
	lst.append(ele)                                    # Adding the element	
print(lst)                                            # Printing input list
print(("=")*80)

print("This function returns reverse list of given input list.") 

def rev(lst):
   r = []                                           # Assignined an empty list
   for i in lst:
      r.insert(0, i)                                # Inserting at zeroth index to get the reverse list 
   return r                                         # Returning reverse list
print("The reverse of list is:- ", rev(lst))

print(("=")*80)
print("This function returns length of numbers in list.") 

def count_list(lst):
   n = 0                                            # Assigned value to 0   
   for i in lst:
      n = n+1                                       # Adding list items to get the length
   return n                                         # Returning length of list
print("The length of list is:- ", count_list(lst))

print(("=")*80)
print("This function returns largest number in list.") 

def myMax(lst):    
   max = lst[0]                                     # Let's say the first element in list is largest element
   for x in lst:                                    # Looping through list and comparing each number to get the largest value
      if x > max :
         max = x
   return max                                       # Returning largest value
print("The largest element in list is:- ", myMax(lst))

print(("=")*80)
print("This function returns sum of numbers in list.") 

def sum_of_list(l):    
   total = 0                                       # Assigned value 0 to total
   for val in l:
      total = total + val                          # Using for loop and adding each value to the variable total 
   return total                                    # Returning sum of elements 

print("The sum of list is:- ", sum_of_list(lst))   # Printing the output
print(("=")*80)