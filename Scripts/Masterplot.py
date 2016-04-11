import random

class Masterplot:
    Clause_A = ["A Person in Love,", "A Married Person,", "A Lawless Person,",
                "An Erring Person,", "A Benevolent Person,", "A Protecting Person,",
                "A Person of Ideals,", "A Person Subjected to Adverse Conditions,",
                "A Resentful Person,", "A Person Swayed by Pretense,",
                "A Subtle Person,", "A Person Influenced by the Occult and the Mysterious,",
                "A Normal Person,", "Any Person,"]

    Clause_B = {
            0: ["Engaging in a difficult enterprise when promised a reward for high achievement,",
                "Falling in love at a time when certain obligations forbid love,",
                "Seeking to demonstrate the power of love by a test of courage,",
                "Being impelled by inordinate fancy to exercise mistaken judgment in a love affair,",
                "Becoming involved in a hopeless love affair, and seeking to make the best of a disheartening situation,",
                "Challenging, in a quest of love, the relentless truth that \"East is East, and West is West, and never the twain shall meet,\"",
                "Becoming involved in a love affair that encounters unforeseen obstacles,",
                "Confronting a situation in which wealth is made conditional upon a certain course of action in a love affair,",
                "Being put to a test in which love will be lost if more material fortunes are advanced,"],
            1: ["Suffering an estrangement due to mistaken judgement,",
                "Confronting a situation in which courage and devotion alone can save the fortunes of one beloved,",
                "Falling into misfortune through disloyalty in love,"],
            2: ["Seeking by craftiness to escape misfortune,",
                "Falling into misfortune through the wiles of a crafty schemer,",
                "Finding a sustaining power in misfortune,",
                "Being delivered from misfortune by one who, in confidence, confesses a secret of transgression,",
                "Bearing patiently with misfortunes and seeking to attain cherished aims honorably,",
                "Rebelling against a power that controls personal abilities and holds them in subjection,",
                "Meeting with misfortune and being cast away in a primitive, isolated and savage environment,",
                "Becoming involved with conditions in which misfortune is indicated,"],
            3: ["Falling into misfortune through mistaken judgment,",
                "Following a wrong course through mistaken judgment,",
                "Becoming involved in a complication that has to do with mistaken judgment and suspicion,",
                "Becoming the victim of mistaken judgment in carrying out an enterprise,"],
            4: ["Seeking to save a person who is accused of transgression,",
                "Seeking secretly to preserve another from danger,",
                "Refusing to betray another's secret and calmly facing persecution because of the refusal,"],
            5: ["Facing a situation in which the misfortunes of one greatly esteemed call for courage and sagacious enterprise,",
                "Aiding another to hide from the world a fateful secret,",
                "Enlisting whole-heartedly in the service of a needy unfortunate and conferring aid of the utmost value,"],
            6: ["Living a lonely, cheerless life and seeking companionship,",
                "Seeking to conceal identity because of a lofty idealism,",
                "Resisting secretly and from an honorable motive a mandate considered discreditable,",
                "Embarking upon an enterprise of insurrection in the hope of ameliorating certain evil conditions,",
                "Becoming involved in a complication that challenges the value of cherished ideals,",
                "Undergoing an experience that results in a remarkable character change,",
                "Seeking against difficulties to realize a cherished ideal,"],
            7: ["Committing a grievous mistake and seeking in secret to live down its evil results,",
                "Forsaking cherished ambitions to carry out an obligation,",
                "Embarking upon an enterprise in which one obligation is opposed by another obligation,",
                "Finding an obligation at variance with ambition, inclination or necessity,",
                "Falling into misiortune while seeking honorably to discharge an obligation,"],
            8: ["Seeking to overcome personal limitations in carrying out an enterprise,",
                "Seeking by unusual methods to conquer personal limitations,",
                "Seeking to forward an enterprise and encountering family sentiment as an obstacle,"],
            9:["Seeking retaliation for a grievous wrong that is either real or fancied,"],
            10:["Finding (apparently) an object greatly coveted, and obtaining (apparently) the object,",
                "Assuming the character of a criminal in a perfectly honest enterprise,",
                "Assuming a fictitious character when embarking upon a certain enterprise,"],
            11:["Being impelled by an unusual motive to engage in crafty enterprise,",
                "Devising a clever and plausible delusion in order to forward certain ambitious plans,",
                "Encountering a would-be transgressor and seeking to prevent a transgression,",
                "Opposing the plans of a crafty schemer,"],
            12:["Becoming involved in a puzzling complication that has to do with an object possessing mysterious powers,",
                "Becoming involved in a mysterious complication and seeking to make the utmost of a bizarre experience,",
                "Seeking to test the value of a mysterious communication and becoming involved in weird complexities,",
                "Seeking to unravel a puzzling complication,",
                "Engaging in an enterprise and then mysteriously disappearing,",
                "Engaging in an enterprise and becoming involved with the occult and the fantastic,",
                "Becoming involved, through curiosity aroused by mystery, in a strange enterprise,"],
            13:["Becoming aware of an important secret that calls for decisive action,"],
            14:["Becoming involved in any sort of complication,"]
            }

    Clause_C = ["Pays a grim penalty in an unfortunate undertaking.",
                "Emerges happily from a serious entanglement.",
                "Foils a guilty plotter and defeats a subtle plot.",
                "Undertakes a role that leads straight to catastrophe.",
                "Emerges from a trying ordeal with sorely garnered wisdom.",
                "Makes the supreme sacrifice in carrying out an undertaking.",
                "Reverses certain opinions when their fallacy is revealed.",
                "Achieves a spiritual victory.",
                "Achieves success and happiness in a hard undertaking.",
                "Meets with an experience whereby an error is corrected.",
                "Discovers the folly of trying to appear otherwise than as one is in reality.",
                "Rescues integrity from a serious entanglement.",
                "Comes finally to the blank wall of enigma.",
                "Achieves a complete and permanent character transformation.",
                "Meets any fate, good or evil."]
    
    def __init__(self):
        self.plot = ""

    def setPlot(self):
        i = random.randrange(1, 15)
        j = random.randrange(len(self.Clause_B[i]))
        
        character = self.Clause_A[i]
        advancement = self.Clause_B[i][j]
        end = self.Clause_C[i]
        plot = character + " " + advancement + " " + end
        self.plot = plot

    def wildCombination(self):
        a = random.randrange(len(self.Clause_A))
        i = random.randrange(len(self.Clause_A))
        b = random.randrange(len(self.Clause_B[i]))
        c = random.randrange(len(self.Clause_C))
       
        character = self.Clause_A[a]
        advancement = self.Clause_B[i][b]
        end = self.Clause_C[c]
        plot = character + " " + advancement + " " + end
        self.plot = plot

    def getPlot(self):
        return self.plot

    def display(self):
        print("The plot: \n")
        print(self.plot)
