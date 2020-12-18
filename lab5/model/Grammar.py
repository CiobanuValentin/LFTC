class Grammar:
    @staticmethod
    def parseLine(line):
        return line.strip().split(' ')[2:]

    @staticmethod
    def read(file_name):
        with open(file_name) as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = Grammar.parseLine(file.readline())[0]

            file.readline()

            P = []
            for line in file:
                [lhs, rhs] = line.strip().split('->')
                lhs.strip()
                for token in rhs.strip().split('|'):
                    P.append((lhs.strip(), token.strip()))
            print(P)
            return Grammar(N, E, S, P)


    def __init__(self, N, E, P, S):
        self.N = N
        self.E = E
        self.P = P
        self.S = S

    def isNonTerminal(self, value):
        return value in self.N

    def isTerminal(self, value):
        return value in self.E

    def getProductionsFor(self, nonTerminal):
        if not self.isNonTerminal(nonTerminal):
            raise Exception('Can only show productions for non-terminals')

        return [prod for prod in self.P if prod[0] == nonTerminal]

    def showProductionsFor(self, nonTerminal):
        productions = self.getProductionsFor(nonTerminal)

        print(', '.join([' -> '.join(prod) for prod in productions]))

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'P = { ' + ', '.join([' -> '.join(prod) for prod in self.P]) + ' }\n' \
               + 'S = ' + str(self.S) + '\n'
