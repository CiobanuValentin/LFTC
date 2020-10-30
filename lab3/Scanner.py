import re

separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ':', ',']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '==', '&&', '||', '!', '!=', '++', '--', ',']
reservedWords = ['fct', 'in>>', 'out<<', 'if', 'else',
                 'for', 'break', 'while',
                 'number', 'char', 'bula', 'return', 'Main']
temp = separators
temp.remove(' ')
everything = temp + operators + reservedWords

codification = {'identifier': 0, 'constant': 1}
for i in range(len(everything)):
    codification[everything[i]] = i + 2


def isIdentifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,}$', token) is not None


def isConstant(token):
    return re.match('^(0|[+\-]?[1-9][0-9]*)$|^\"[a-zA-Z0-9]*\"$|true|false', token) is not None
    # return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None


def getTokensOld(line):
    return re.split("([ (){}\[\];,])", line)


def getTokensByOperators(line):
    return re.split("(<=|>=|\+\+|--|!=|==|\+|-|\*|/|%|<|>|&&|\|\||!|)", line)


def getTokens(line):
    x = re.split("([ (){}\[\];,])", line)
    y = []
    for i in range(len(x)):
        if x[i] not in separators + operators + reservedWords and not isIdentifier(x[i]) and not isConstant(x[i]):
            if any(operator in x[i] for operator in operators):
                y.extend(getTokensByOperators(x[i]))
                y = list(filter(lambda a: a != '' and a != '\n', y))
            else:
                y.append(x[i])
        else:
            y.append(x[i])
    y = list(filter(lambda a: a != '' and a != '\n', y))
    return y
