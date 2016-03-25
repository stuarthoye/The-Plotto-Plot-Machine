from Conflicts import Conflicts
from Characters import Characters
from Masterplot import Masterplot

class Plotto:
    
    def __init__(self):
        self.conflicts = Conflicts()
        self.characters = Characters()
        self.masterplot = Masterplot()
        
    def generate(self):
        self.conflicts.setConflict()
        self.characters.wildCombination()
        self.masterplot.wildCombination()
        
    def display(self):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("==============================================================================")
        print("PLOTTO:\n")
        print("==============================================================================")
        self.conflicts.display()
        self.masterplot.display()
        self.characters.display()