import random

class Character:
    def __init__(self, relation):
        self.name = ""
        self.sex = ""
        self.role = ""
        self.roleToward = ""
        
        if (relation == "A" or relation == "B"):
            self.makeProtagonist(relation)
        elif "-" in relation:
            primary, secondary = relation.split("-")
            if primary in ["A", "B"]:
                self.makeSocial(primary, secondary)
            else:
                self.makeFamily(primary, secondary)
        else:
            self.makeOther(relation)

        if "A" in relation:
            self.protagonist = "A"
        else:
            self.protagonist = "B"
            
        self.name = self.getName(self.sex)
    
    def makeProtagonist(self, relation):
        if relation == "A":
            self.sex = "male"
        else:
            self.sex = "female"
        self.role = "protagonist"
        self.name = self.getName(self.sex)
        
    def makeSocial(self, primary, sec):
        if primary == "A":
            self.sex = "male"
        else:
            self.sex = "female"
        if sec == "2":
            self.role = "friend"
        elif sec == "3":
            self.role = "rival or enemy"
        elif sec == "4":
            self.role = "stranger"
        elif sec == "5":
            self.role = "criminal"
        elif sec == "6":
            self.role = "officer of the law"
        elif sec == "7":
            self.role = "inferior or employee"
        elif sec == "8":
            self.role = "utility symbol"
        elif sec == "9":
            self.role = "superior, employer, or one in authority"
        
    def makeFamily(self, primary, sec):
        if primary in ["F", "BR", "SN", "U", "CN", "NW", "GF", "SF"]:
            self.sex = "male"
        elif primary in ["M", "SR", "D", "AU", "NC", "GM", "SM"]:
            self.sex = "female"
        else:
            # children & grandchildren of indeterminate sex, eg
            self.sex = "undecided" 
        
        if primary == "F":
            self.role = "father"
        elif primary == "M":
            self.role = "mother"
        elif primary == "BR":
            self.role = "brother"
        elif primary == "SR":
            self.role = "sister"
        elif  primary == "SN":
            self.role = "son"
        elif primary == "D":
            self.role = "daughter"
        elif primary == "U":
            self.role = "uncle"
        elif primary == "AU":
            self.role = "aunt"
        elif primary == "CN":
            self.role = "cousin"
        elif primary == "NW":
            self.role = "nephew"
        elif primary == "NC":
            self.role = "neice"
        elif primary == "GF":
            self.role = "grandfather"
        elif primary == "GM":
            self.role = "grandmother"
        elif primary == "SF":
            self.role = "stepfather"
        elif primary == "SM":
            self.role = "stepmother"
        elif primary == "GCH":
            self.role = "grandchild"
        elif primary == "CH":
            self.role = "child"

    def makeOther(self, primary):
        if primary == "X":
            self.sex = "neuter"
            self.role = "an inanimate object, and object of mystery, and uncertain quantity"
        else:
            if primary[0] == "A":
                self.sex = "male"
            else:
                self.sex = "female"
            self.role = "mysterious person, or one of unusual character"

    def getName(self, sex):
        return "Name Placeholder"

    def __str__(self):
        return self.name + ":\n" + "A " + self.sex + " " + self.role + "\n" +\
               "in relation to " + self.protagonist + "."

class Characters:
    def __init__(self):
        self.characters = ["A", "B", "A-2", "B-2", "A-3", "B-3", "A-4", "B-4",
                           "A-5", "B-5", "A-6", "B-6", "A-7", "B-7", "A-8", "B-8",
                           "A-9",  "B-9", "F-A", "F-B", "M-A", "M-B", "BR-A",
                           "BR-B", "SR-A", "SR-B", "SN-A", "SN-B", "D-A", "D-B",
                           "U-A", "U-B", "AU-A", "AU-B", "CN-A", "CN-B", "NW-A",
                           "NW-B", "NC-A", "NC-B", "GF-A", "GF-B", "GM-A", "GM-B",
                           "SF-A", "SF-B", "SM-A", "SM-B", "GCH-A", "GCH-B",
                           "CH", "AX", "BX", "X"]
        self.cast = []
        
    def wildCombination(self):
        count = random.randrange(3, 7)
        for i in range(count):
            j = random.randrange(len(self.characters))
            self.cast.append(Character(self.characters[j]))

    def getCharacters(self):
        return self.cast

    def display(self):
        print("Cast of characters: \n")
        for member in self.cast:
            print(str(member) + "\n")
