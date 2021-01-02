# also known as gale shapley algorithm
n=int(input("Enter the number of candidates(N): "))
A_B=[]

print('Enter candidates of group 1:')
var=list(map(str,input().split()))
A_B.append(var)
print('Enter candidates of group 2:')
var=list(map(str,input().split()))
A_B.append(var)



# Matrix A,B are NxN and contain the preferences of group 1,2 (men,women) respectively
print('Enter preferences of group 1:')
A=[]
for _ in range(n):
    print('List of Candidate ',str(_+1))
    var=list(map(str,input().split()))
    A.append(var)

print('Enter preferences of group 2:')
B=[]
for _ in range(n):
    print('List of Candidate ',str(_+1))
    var=list(map(str,input().split()))
    B.append(var)

# queue of remaining idle poeple
unmatched=[]
for i in A_B[0]:
    unmatched.append(i)
# current partners are the pairs matched till date
current_partners=[[],[]]
for i in range(n):
    current_partners[0].append('_')
    current_partners[1].append('_')
# create proposed matrix (Binary)
proposed=[]
for i in range(n):
    for j in range(n):
        var=[]
        var.append(0)
    proposed.append(var)

# Start of Algo #
#               #
#               #
while(len(unmatched)>0):
    current_male=unmatched.pop(0)
    i=A_B.index(current_male)
    for j in range(n):
        if proposed[i][j]==0:   # this male hasnt proposed the female at pos j
            proposed[i][j]=1
            current_female=A[i][j]
            male_index=A_B[0].index(current_male)
            female_index=A_B[1].index(current_female)
            if current_female in current_partners[1]: # the female is already engaged and need to check priority
                defending_male=current_partners[0][current_partners[1].index(current_female)] # rival of proposing male
                defending_male_pos=B[female_index].index(defending_male)
                current_male_pos=B[female_index].index(current_male)
                if current_male_pos < defending_male_pos: # the proposing male has higher priority than defending male in view of the female
                    
                    pass
                
            else:                              # female not engaged engage her to the male
                current_partners[0][male_index]=current_male
                current_partners[1][male_index]=current_female
                break