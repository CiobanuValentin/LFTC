from model.St import SymbolTable
from model.Pif import ProgramInternalForm
from Scanner import *

if __name__ == "__main__":
    fileName = "err.txt"

    file = open(fileName, 'r')
    for line in file:
        print(line)

    with open(fileName, 'r') as file:
       for line in file:
            print([token for token in getTokens(line)])

    symbolTable = SymbolTable()
    pif = ProgramInternalForm()
    with open(fileName, 'r') as file:
        lineNo = 0
        for line in file:
            lineNo += 1
            line=line.replace('\n','')
            for token in getTokens(line):
                if token == '' or token == '\n' or token == ' ':
                    pass
                elif token in separators + operators + reservedWords:
                    pif.add(codification[token], -1)
                elif isConstant(token):
                    id = symbolTable.add(token)
                    pif.add(codification['constant'], id)
                elif isIdentifier(token):
                    id = symbolTable.add(token)
                    pif.add(codification['identifier'], id)
                else:
                    raise Exception('Unknown token $' + token + '$ at line ' + str(lineNo))

    """""
    with open(fileName, 'r') as file:
        lineNo = 0
        for line in file:
            lineNo += 1
            line=line.replace('\n','')
            for token in getTokens(line):
                if token == '' or token == '\n':
                    pass
                elif token in separators + operators + reservedWords:
                    pif.add(codification[token], -1)
                elif isConstant(token):
                    id = symbolTable.add(token)
                    pif.add(codification['constant'], id)
                elif isIdentifier(token):
                    id = symbolTable.add(token)
                    pif.add(codification['identifier'], id)
                else:
                    for token2 in getTokensByOperators(token):
                        #
                        if token2 == '' or token2 == '\n':
                            pass
                        elif token2 in separators + operators + reservedWords:
                            pif.add(codification[token2], -1)
                        elif isConstant(token2):
                            id = symbolTable.add(token2)
                            pif.add(codification['constant'], id)
                        elif isIdentifier(token2):
                            id = symbolTable.add(token2)
                            pif.add(codification['identifier'], id)
                        else:
                            raise Exception('Unknown token $' + token + '$ at line ' + str(lineNo))
                        #
                    #raise Exception('Unknown token $' + token + '$ at line ' + str(lineNo))
    """""
    outPif = open("pif.txt", "w")
    outSt = open("St.txt", "w")
    outCodification = open("codification.txt", "w")
    outSt.write(str(symbolTable.inorder()))
    outPif.write(str(pif))
    s=""
    for x,y in codification.items():
        s+=(str(x)+" "+str(y)+'\n')
    outCodification.write(s)
