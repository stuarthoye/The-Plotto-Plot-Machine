import random

class Conflicts:
    def __init__(self):
        self.conflict = "";
        self.grandScope = "";
        self.grandScopes = ["Love & Courtship", "Married Life", "Enterprise"]
        self.conflicts = { "Love & Courtship": [   "Love's beginnings", 
                                                   "Love's misadventures",
                                                   "The Marriage Proposal",
                                                   "Love's rejection",
                                                   "Marriage"],
                           "Married Life"    : [   ""],
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
    
    def wildCombination(self):
        i = random.randrange(len(self.grandScopes))
        gs = self.grandScopes[i]
        j = random.randrange(len(self.conflicts[gs]))
        self.grandScope = gs
        self.conflict = self.conflicts[gs][j]
    
    def selectGrandScope(self, selection):
        assert(selection in range(len(self.grandScopes)))
        assert(self.conflict == "")
        self.grandScope += self.grandScopes[selection]
    
    def selectConflict(self, selection):
        assert(self.grandScope in self.conflicts)
        assert(selection in range(len(self.conflicts[self.grandScope])))
        self.conflict = self.conflicts[self.grandScope][selection]
    
    def getGrandScopes(self):
        return self.grandScopes

    def getGrandScope(self):
        return self.grandScope

    def getConflicts(self):
        return self.conflicts

    def getConflicts(self, grandScope):
        assert(grandScope in self.conflicts)
        return self.conflicts[grandScope]

    def getConflict(self):
        return self.conflict

    def display(self):
        print(self.grandScope + "; " + self.conflict + ".\n")
