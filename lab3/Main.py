from model.St import SymbolTable
from model.Pif import ProgramInternalForm
from Scanner import *

if __name__ == "__main__":
    fileName = "1.txt"

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
                    raise Exception('Unknown token $' + token + '$ at line ' + str(lineNo))
    symbolTable.inorder()
    print(pif)
    print(codification)
