from Conflicts import Conflicts
from Characters import Characters
from Masterplot import Masterplot

class Plotto:
    
    def __init__(self):
        self.plotting = True;
        self.conflicts = Conflicts()
        self.characters = Characters()
        self.masterplot = Masterplot()
        self.options = ["Create a Conflict", "Create a Masterplot", 
                        "Create some Characters", "Terminate"]
        
    def generate(self):
        self.conflicts.wildCombination()
        self.characters.wildCombination()
        self.masterplot.wildCombination()
<<<<<<< HEAD

    def selectFrom(self, selections):
        selection = ""
        print("Please select an option:")
        for i in range(len(selections)):
            print("[" + str(i+1) + "]: " + selections[i])
        while (selection == ""):
            try:
                selection = input("Please select the number representing your choice: ")
                assert(int(selection) in range(1, len(selections) + 1))
            except AssertionError:
                print("Your selection was not in the valid range.")
        return int(selection) - 1

    def terminate(self):
        self.plotting = False;

    def menu(self):
        self.clearScreen()
=======
        
    def display(self):
>>>>>>> 4718701b07f2fa7ead9ed679b9593417cbf5fd38
        print("==============================================================================")
        print("PLOTTO:")
        print("==============================================================================")
        selection = self.selectFrom(self.options)
        if (selection == 0):
            self.menuConflict()
        elif (selection == 1):
            self.menuMasterplot()
        elif (selection == 2):
            self.menuCharacters()
        elif (selection == 3):
            self.terminate()

    def menuConflict(self):
        grandScopes = self.conflicts.getGrandScopes()
        self.clearScreen()
        print("==============================================================================")
        print("PLOTTO Conflicts:\n")
        print("==============================================================================")
        print("Please select a Grand Scope for your narrative:")
        selection = self.selectFrom(grandScopes)
        self.conflicts.selectGrandScope(selection)

        conflicts = self.conflicts.getConflicts(self.conflicts.getGrandScope())
        self.clearScreen()
        print("==============================================================================")
        print("Please select a Conflict for your narrative:")
        selection = self.selectFrom(conflicts)
        self.conflicts.selectConflict(selection)

    def menuMasterplot(self):
        self.clearScreen()
        print("==============================================================================")
        print("PLOTTO Masterplots:\n")
        print("==============================================================================")
        
    def menuCharacters(self):
        self.clearScreen()
        print("==============================================================================")
        print("PLOTTO Characters:\n")
        print("==============================================================================")
    
    def isPlotting(self):
        return self.plotting

    def clearScreen(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def display(self):
        self.conflicts.display()
        self.masterplot.display()
        self.characters.display()