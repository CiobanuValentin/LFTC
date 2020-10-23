import re

separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ':', ',']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '==', '&&', '||', '!', '!=', '++', '--', ',']
reservedWords = ['fct', 'in>>', 'out<<', 'if', 'else',
                 'for', 'break', 'while',
                 'number', 'char', 'bula', 'return', 'Main']

everything = separators + operators + reservedWords

codification = {'identifier': 0, 'constant': 1}
for i in range(len(everything)):
    codification[everything[i]] = i + 2


def isIdentifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,}$', token) is not None


def isConstant(token):
    return re.match('^(0|[+\-]?[1-9][0-9]*)$|^\"[a-zA-Z0-9]*\"$|true|false', token) is not None
    # return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None


def getTokens(line):
    return re.split("([ (){}\[\];,])", line)
    # return re.split("( |\(|\)|\{|\}|\[|\]|\;|,)", line)
def getTokensByOperators(line):
    return re.split("(<=|>=|\+\+|--|!=|==|\+|-|\*|/|%|<|>|&&|\|\||!|)", line)

