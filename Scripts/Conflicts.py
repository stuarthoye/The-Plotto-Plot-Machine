import random

class Conflicts:
    def __init__(self):
        self.grandScope = ["Love & Courtship", "Married Life", "Enterprise"]
        self.Conflicts = { "Love & Courtship": [   "Love's beginnings", 
                                                   "Love's misadventures",
                                                   "The Marriage Proposal",
                                                   "Love's rejection",
                                                   "Marriage"],
                           "Married Life"    : [   "Divorce",
                                                   "Affair"],
                           "Enterprise"      : [   "Misfortune",
                                                   "Mistaken Judgement",
                                                   "Helpfulness",
                                                   "Deliverance",
                                                   "Idealism",
                                                   "Obligation",
                                                   "Necessity",
                                                   "Chance",
                                                   "Personal Limitations",
                                                   "Simulation",
                                                   "Craftiness",
                                                   "Transgression",
                                                   "Revenge"]
                         }
    
    def setConflict(self):
        i = random.randrange(len(self.grandScope))
        gs = self.grandScope[i]
        j = random.randrange(len(self.Conflicts[gs]))
        self.conflict = gs + "; " + self.Conflicts[gs][j]
    
    def getConflict(self):
        return self.conflict

    def display(self):
        print(self.conflict + ".\n")
