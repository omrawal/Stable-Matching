import tkinter as tk
from tkinter import messagebox
from stable_matching import StableMatch


def validate_input(n,grp1,grp2,pref1,pref2):
    if(len(grp1)!=n):
        return([False,'Length of group1 not Equal to n !!!'])
    elif(len(grp2)!=n):
        return([False,'Length of group2 not Equal to n !!!'])
    elif(len(grp1)!=len(grp2)):
        return([False,'Lengths of groups are unequal !!!'])
    elif(len(pref1[0])!=len(pref1)):
        return([False,'Invalid Preference 1 matrix !!!'])
    elif(len(pref2[0])!=len(pref2)):
        return([False,'Invalid Preference 2 matrix !!!'])
    else:
        return([True,''])

def getInputs(n,gp1,gp2,p1,p2,root):
    n=int(n)
    group1=gp1.split(',')
    group2=gp2.split(',')
    # print(n)
    # print(group1)
    # print(group2)
    pref1=[]
    a=p1.split('\n')
    for i in a:
        k=i.split(',')
        pref1.append(k)
    # print(a)
    # print(pref1)
    pref2=[]
    a=p2.split('\n')
    for i in a:
        k=i.split(',')
        pref2.append(k)
    bool_result=validate_input(n,group1,group2,pref1,pref2)
    if(bool_result[0]==False):
        messagebox.showerror("Error",bool_result[1])
    else:
        sm=StableMatch(n)
        sm.get_grps(group1,group2)
        sm.get_preference_grp1(pref1)
        sm.get_preference_grp2(pref2)
        sm.select_proposing_group(1)
        sm.create_unmatched_list()
        sm.create_current_partner_matrix()
        sm.create_proposed_matrix()
        result_list=sm.calculate_stable_match()
        result_str=''
        for i in range(len(result_list[0])):
            if(i==len(result_list[0])-1):
                result_str+=result_list[0][i]+' <-> '+result_list[1][i]
            else:
                result_str+=result_list[0][i]+' <-> '+result_list[1][i]+'\n'
        messagebox.showinfo('Stable Match',result_str)
        
    


    









root = tk.Tk()
root.title("Stable Matching Algorithm")
root.geometry("500x700") #300x200
lbs = tk.Label(root, text = "Stable Matching", font=20)
lbs.place(x=180, y=5)


countlabel = tk.Label(root, text = "Count ")
countEntry = tk.Entry(root)
countlabel.place(x=110, y=60)
countEntry.place(x=210, y=60)

grp1label = tk.Label(root, text = "Group 1 ")
grp1Entry = tk.Entry(root)
grp1label.place(x=110, y=100)
grp1Entry.place(x=210, y=100,width=250)

grp2label = tk.Label(root, text = "Group 2 ")
grp2Entry = tk.Entry(root)
grp2label.place(x=110, y=140)
grp2Entry.place(x=210, y=140,width=250)

pref1label = tk.Label(root, text = "Pref. of Grp1 ")
pref1text=tk.Text(root)
pref1label.place(x=110, y=180)
pref1text.place(x=210, y=180,height=100, width=250)

pref2label = tk.Label(root, text = "Pref. of Grp2 ")
pref2text=tk.Text(root)
pref2label.place(x=110, y=310)
pref2text.place(x=210, y=310,height=100, width=250)

log=tk.Button(root,font=("times", 16),text="Match",command=lambda:getInputs(countEntry.get(),grp1Entry.get(),grp2Entry.get(),pref1text.get("1.0",'end-1c'),pref2text.get("1.0",'end-1c'),root))
log.place(x = 200, y = 440 )

inst_text='Note:-\n\tn = Integer\n\tGroups = comma separated\n\tPreferences = Comma Separated matrix'
inst = tk.Label(root, text = inst_text, font=2)
inst.place(x=0, y=500)

root.mainloop()



#  TESTING INPUTS SET 1

# 5

# A,B,C,D,E

# L,M,N,O,P

# O,M,N,L,P
# P,N,M,L,O
# M,P,L,O,N
# P,M,O,N,L
# O,L,M,N,P

# D,B,E,C,A
# B,A,D,C,E
# A,C,E,D,B
# D,A,C,B,E
# B,E,A,C,D

#  TESTING INPUTS SET 2

# 4

# RYAN,JOSH,BLAKE,CONNOR

# LIZZY,SARAH,ZOEY,DANIELA

# LIZZY,SARAH,ZOEY,DANIELA
# SARAH,LIZZY,DANIELA,ZOEY
# SARAH,DANIELA,ZOEY,LIZZY
# LIZZY,SARAH,ZOEY,DANIELA

# RYAN,BLAKE,JOSH,CONNOR
# RYAN,BLAKE,CONNOR,JOSH
# CONNOR,JOSH,RYAN,BLAKE
# RYAN,JOSH,CONNOR,BLAKE