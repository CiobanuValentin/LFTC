from model.Fa import Fa


if __name__ == '__main__':
    finiteAutomata = Fa.fromFile('fa1.txt')
    print(finiteAutomata)
    finiteAutomata.verifySeq('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab')