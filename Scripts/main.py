from Plotto import Plotto

def main():
    plotto = Plotto()
    while (plotto.isPlotting()):
        plotto.menu()
        plotto.display()
    plotto.generate()
    plotto.display()

main()