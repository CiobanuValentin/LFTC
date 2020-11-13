
class Fa:
    @staticmethod
    def parseLine(line):
        x = line.strip().split('=')[1].strip()[1:-1].strip()
        x = x.replace('\n','')
        x = x.replace('\t', '')
        return [value.strip() for value in x.split(',')]

    @staticmethod
    def fromFile(fileName):
        with open(fileName) as file:
            Q = Fa.parseLine(file.readline())
            E = Fa.parseLine(file.readline())
            q0 = file.readline().split('=')[1].strip()
            F = Fa.parseLine(file.readline())
            S = Fa.parseTransitions(Fa.parseLine(''.join([line for line in file])))
            return Fa(Q, E, S, q0, F)

    @staticmethod
    def parseTransitions(parts):
        result = []
        transitions = []
        index = 0

        while index < len(parts):
            transitions.append(parts[index] + ',' + parts[index + 1])
            index += 2

        for transition in transitions:
            lhs, rhs = transition.split('->')
            state2 = rhs.strip()
            state1, route = [value.strip() for value in lhs.strip()[1:-1].split(',')]

            result.append(((state1, route), state2))

        return result

    def __init__(self, Q, E, S, q0, F):
        self.Q = Q
        self.E = E
        self.S = S
        self.q0 = q0
        self.F = F
        self.isDfa = self.isDFA()

    def isDFA(self):
        for i in range(len(self.S)):
            for j in range(len(self.S)):
                if self.S[i][0] == self.S[j][0]:
                    if i!=j:
                        return False
        return True


    def verifySeq(self, sequence):
        if self.isDfa:
            x = self.q0
            ok = False
            for i in sequence:
                ok = False
                for s in self.S:
                    if s[0] == (x, i):
                        x = s[1]
                        ok = True
                        break
                if not ok:
                    break
            if ok and x in self.F:
                print('seq is good')
            else:
                print('seq is not good')
        else:
            print('is not dfa')

    def __str__(self):
        return 'Q = { ' + ', '.join(self.Q) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'F = { ' + ', '.join(self.F) + ' }\n' \
               + 'S = { ' + ', '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n' \
               + 'q0 = ' + str(self.q0) + '\n'


