from Plotto import Plotto
import grammar_check
import re

import re

def capitalize(str_in):
	return re.sub(r"(\A\w)|"+             # start of string
             "(?<!\.\w)([\.?!] )\w|"+     # after a ?/!/. and a space, but not after an acronym
             "\w(?:\.\w)|"+               # start/middle of acronym
             "(?<=\w\.)\w",               # end of acronym
             lambda x: x.group().upper(), 
             str_in)

def main():
    plotto = Plotto()
    plotto.generate()
    
    tool = grammar_check.LanguageTool('en-US')

    masterplot = plotto.masterplot.getPlot()
    plot_checked = grammar_check.correct(masterplot, tool.check(masterplot))
    print capitalize(plot_checked.lower())

    conflict = plotto.conflicts.getConflict()
    characters = plotto.characters.getCharacters()

    print conflict, characters[0]
    # plotto.display()

main()