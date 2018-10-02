#
#Below is just the function defination.
#

def angryProfessor(k, a):
    present=0;
    for l in a:
        if l<=0:
            present+=1;
    if(present<k):
        return "YES";
    else:
        return "NO";
        
#
#If you want to check whether code works you can use following function calls
#

a=angryProfessor(3,[-1,-3,4,2])
print(a)
