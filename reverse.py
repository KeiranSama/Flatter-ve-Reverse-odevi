l = [[1, 2], [3, 4], [5, 6, 7]]
l.reverse()
def reversed(x):
    reversed_list = []
    for i in x :
         if type(i) == list:
            
            reversed_list.append(i[::-1])
            
    return reversed_list
   
         
         
print(reversed(l))