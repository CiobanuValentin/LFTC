%{
#include <stdio.h>
#include <stdlib.h>


#define YYDEBUG 1
%}

%token IDENTIFIER
%token CONSTANT
%token FCT
%token MAIN
%token IN
%token OUT
%token IF
%token ELSE
%token FOR
%token WHILE
%token BREAK
%token NUMBER
%token CHAR
%token BULA
%token RETURN
%token TRUE
%token FALSE
%token COLON
%token SEMI_COLON
%token COMA
%token DOT
%token PLUS
%token MINUS
%token MULTIPLY
%token DIVISION
%token MOD
%token LEFT_ROUND_PARENTHESIS
%token RIGHT_ROUND_PARENTHESIS
%token LEFT_SQUARE_PARENTHESIS
%token RIGHT_SQUARE_PARENTHESIS
%token LEFT_CURLY_PARENTHESIS
%token RIGHT_CURLY_PARENTHESIS
%token LESS_THAN
%token GREATER_THAN
%token LESS_OR_EQUAL_THAN
%token GREATER_OR_EQUAL_THAN
%token DIFFERENT
%token EQUAL
%token ASSIGNMENT
%token NEGATION
%token OR
%token AND

%start program

%%

program : FCT MAIN LEFT_ROUND_PARENTHESIS RIGHT_ROUND_PARENTHESIS cmpstmt ;
cmpstmt : LEFT_CURLY_PARENTHESIS stmtlist RIGHT_CURLY_PARENTHESIS ;
stmtlist : stmt SEMI_COLON | stmt SEMI_COLON stmtlist ;
stmt : decl | assignment | iostmt | ifstmt | whilestmt | forstmt | cmpstmt ;
decl : type IDENTIFIER ;
assignment : IDENTIFIER ASSIGNMENT expression ;
iostmt : OUT term | IN term ;
ifstmt : IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS cmpstmt | IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS cmpstmt ELSE cmpstmt ;
whilestmt : WHILE LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS cmpstmt ;
forstmt : FOR LEFT_ROUND_PARENTHESIS assignment SEMI_COLON condition SEMI_COLON assignment RIGHT_ROUND_PARENTHESIS cmpstmt ;
relation : LESS_THAN | GREATER_THAN | LESS_OR_EQUAL_THAN | GREATER_OR_EQUAL_THAN | DIFFERENT | EQUAL ;
expression : term | term PLUS expression | term MINUS expression | term MULTIPLY expression | term DIVISION expression | term MOD expression | LEFT_ROUND_PARENTHESIS expression RIGHT_SQUARE_PARENTHESIS ;
term : IDENTIFIER | CONSTANT | IDENTIFIER LEFT_SQUARE_PARENTHESIS term RIGHT_SQUARE_PARENTHESIS  ;
type : primitiveType | arrayDeclaration ;
primitiveType : CHAR | NUMBER | BULA ;
arrayDeclaration : primitiveType LEFT_SQUARE_PARENTHESIS CONSTANT RIGHT_SQUARE_PARENTHESIS  ;
condition : expression relation expression ;


%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1)
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) )
    yydebug = 1;
  if ( !yyparse() )
    fprintf(stderr,"\t U GOOOOOD !!!\n");
}
