import random
import names

class Character:
    def __init__(self, role, protagonists = []):
        self.role = role

        print self.role
        print len(protagonists)

        if len(protagonists) > 0:
            self.role = self.role.replace('of A', 'of ' + protagonists[0].name)
            self.role = self.role.replace('of B', 'of ' + protagonists[1].name)

        self.gender = 'male'
        gender_swap = ('female', 'mother', 'sister', 'daughter', 'aunt', 'neice')    
        if any(s in self.role for s in gender_swap):
            self.gender = 'female'
        self.name = self.getName(self.gender)

    def getName(self,sex):
        return names.get_full_name(gender = sex)

class Characters:
    def __init__(self):
        
        # this list should come from the text file of characters

        self.characters = {}
        with open("../Texts/clean/characters-clean.txt") as f:
            for line in f:
                (key, val) = line.split(', ',2)
                self.characters[key] = val.rstrip()
        self.cast = []
        
    def wildCombination(self):
        # Create the male protagonist
        male_pro = Character(self.characters['A'])
        self.cast.append(male_pro)

        # Create the female protagonist
        female_pro = Character(self.characters['B'])
        self.cast.append(female_pro)
        
        # get some collection of supporting characters
        min_chars = 1
        max_chars = 5
        count = random.randrange(min_chars, max_chars)
        for i in range(count):
            # pull a random character
            new_char = Character(self.characters[random.choice(self.characters.keys())],[male_pro,female_pro])
            # add the character to the character list 
            self.cast.append(new_char)

    def getCharacters(self):
        return self.cast

    def display(self):
        print("Cast of characters: \n")
        for member in self.cast:
            print(str(member) + "\n")
