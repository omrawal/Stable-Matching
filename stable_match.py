# also known as gale shapley algorithm
# n=int(input("Enter the number of candidates(N): "))
n=5 #test
# n=4 #test
A_B=[]

# print('Enter candidates of group 1:')
# var=list(map(str,input().split()))
# A_B.append(var)
# print('Enter candidates of group 2:')
# var=list(map(str,input().split()))
# A_B.append(var)

A_B=[['A','B','C','D','E'],['L','M','N','O','P']] #test
# A_B=[['r','j','b','c'],['l','s','z','d']] #test


# Matrix A,B are NxN and contain the preferences of group 1,2 (men,women) respectively
# print('Enter preferences of group 1:')
# A=[]
# for _ in range(n):
#     print('List of Candidate ',str(_+1))
#     var=list(map(str,input().split()))
#     A.append(var)

# print('Enter preferences of group 2:')
# B=[]
# for _ in range(n):
#     print('List of Candidate ',str(_+1))
#     var=list(map(str,input().split()))
#     B.append(var)

A=[['O','M','N','L','P'],['P','N','M','L','O'],['M','P','L','O','N'],['P','M','O','N','L'],['O','L','M','N','P']] #test
B=[['D','B','E','C','A'],['B','A','D','C','E'],['A','C','E','D','B'],['D','A','C','B','E'],['B','E','A','C','D']] #test
# A=[['l','s','z','d'],['s','l','d','z'],['s','d','z','l'],['l','s','z','d']] #test
# B=[['r','b','j','c'],['r','b','c','j'],['c','j','r','b'],['r','j','c','b']] #test

# queue of remaining idle poeple(males)
unmatched=[]
for i in A_B[0]:
    unmatched.append(i)
# print(unmatched)
# current partners are the pairs matched till date
current_partners=[[],[]]
for i in range(n):
    current_partners[0].append('_')
    current_partners[1].append('_')
# create proposed matrix (Binary)
proposed=[]
for i in range(n):
    var=[]
    for j in range(n):
        # var=[]
        var.append(0)
    proposed.append(var)
# print(proposed)
# Start of Algo #
#               #
#               #
while(len(unmatched)>0):
    current_male=unmatched.pop(0)
    i=A_B[0].index(current_male)
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
                    current_partners[0][A_B[0].index(defending_male)]='_'
                    current_partners[1][A_B[0].index(defending_male)]='_'
                    current_partners[0][A_B[0].index(current_male)]=current_male
                    current_partners[1][A_B[0].index(current_male)]=current_female
                    unmatched.insert(0,defending_male)
                    break           
            else:                              # female not engaged engage her to the male
                current_partners[0][male_index]=current_male
                current_partners[1][male_index]=current_female
                break
print(current_partners)