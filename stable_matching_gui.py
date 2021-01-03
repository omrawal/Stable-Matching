import tkinter as tk
# def getInputs(n,grp1,grp2,pref1,pref2):
#     print('n=',n)
#     print('grp1',grp1)
#     print('grp2',grp2)
#     print('pref1',pref1)
#     print('pref2',pref2)
#     pass

def getInputs(n,gp1,gp2,p1,p2):
    print('n=',n)
    print('grp1',gp1)
    print('grp2',gp2)
    print('pref1',p1)
    print('pref2',p2)









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

log=tk.Button(root,font=("times", 16),text="Match",command=lambda:getInputs(countEntry.get(),grp1Entry.get(),grp2Entry.get(),pref1text.get("1.0",'end-1c'),pref2text.get("1.0",'end-1c')))
log.place(x = 200, y = 440 )

root.mainloop()