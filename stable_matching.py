class StableMatch:
    def __init__(self,count) -> None: # count=set count; 
        self.n=count
    def get_grps(self,group1,group2): # grp1=elements in group 1; grp2=elements in group 2;
        self.A_B=[group1,group2]
    def get_preference_grp1(self,grp1): # list of lists
        self.A=grp1
    def get_preference_grp2(self,grp2): # list of lists
        self.B=grp2
    
    def select_proposing_group(self,value):  # group value is ~requires 1/2~  0=first 1=second 
        if(value==1):
            self.proposing_group=0
            self.proposed_group=1
    def create_unmatched_list(self): # list of unmatched items from proposing group
        self.unmatched=[]
        for i in self.A_B[self.proposing_group]:
            self.unmatched.append(i)
    def create_current_partner_matrix(self): # pairs of matched partners
        self.current_partners=[[],[]]
        for i in range(self.n):
            self.current_partners[0].append('_')
            self.current_partners[1].append('_')
    def create_proposed_matrix(self): # matrix to mark the proposed items
        self.proposed=[]
        for i in range(self.n):
            var=[]
            for j in range(self.n):
                # var=[]
                var.append(0)
            self.proposed.append(var)
    

    def calculate_stable_match(self): # here male refers to proposer and female to proposee
        while(len(self.unmatched)>0):
            current_male=self.unmatched.pop(0)
            i=self.A_B[self.proposing_group].index(current_male)
            for j in range(self.n):
                if self.proposed[i][j]==0:   # this male hasnt proposed the female at pos j
                    self.proposed[i][j]=1
                    current_female=self.A[i][j]
                    male_index=self.A_B[self.proposing_group].index(current_male)
                    female_index=self.A_B[self.proposed_group].index(current_female)
                    if current_female in self.current_partners[self.proposed_group]: # the female is already engaged and need to check priority
                        defending_male=self.current_partners[self.proposing_group][self.current_partners[self.proposed_group].index(current_female)] # rival of proposing male
                        defending_male_pos=self.B[female_index].index(defending_male)
                        current_male_pos=self.B[female_index].index(current_male)
                        if current_male_pos < defending_male_pos: # the proposing male has higher priority than defending male in view of the female
                            self.current_partners[self.proposing_group][self.A_B[self.proposing_group].index(defending_male)]='_'
                            self.current_partners[self.proposed_group][self.A_B[self.proposing_group].index(defending_male)]='_'
                            self.current_partners[self.proposing_group][self.A_B[self.proposing_group].index(current_male)]=current_male
                            self.current_partners[self.proposed_group][self.A_B[self.proposing_group].index(current_male)]=current_female
                            self.unmatched.insert(self.proposing_group,defending_male)
                            break           
                    else:                              # female not engaged engage her to the male
                        self.current_partners[self.proposing_group][male_index]=current_male
                        self.current_partners[self.proposed_group][male_index]=current_female
                        break
        return self.current_partners                