%{
#include <math.h>
#include <stdio.h>
#include "parser.tab.h"
int lines = 0;
%}
%option noyywrap

DIGIT 		[0-9]
STRING		["]([a-zA-Z ])*["]
NUMBER		[1-9][0-9]*|0|"-"[1-9][0-9]*
BULA "true"|"false"
CST		{STRING}|{NUMBER}
ID 		[a-zA-Z][a-zA-Z0-9]*

%%

"fct"	{printf( "Reserved word: %s\n", yytext ); return FCT; }
"Main"	{printf( "Reserved word: %s\n", yytext ); return MAIN; }
"in>>"	{printf( "Reserved word: %s\n", yytext ); return IN; }
"out<<"	{printf( "Reserved word: %s\n", yytext ); return OUT; }
"if"	{printf( "Reserved word: %s\n", yytext ); return IF; }
"else"	{printf( "Reserved word: %s\n", yytext ); return ELSE; }
"for"	{printf( "Reserved word: %s\n", yytext ); return FOR; }
"break"	{printf( "Reserved word: %s\n", yytext ); return BREAK; }
"Number"	{printf( "Reserved word: %s\n", yytext ); return NUMBER; }
"char"	{printf( "Reserved word: %s\n", yytext ); return CHAR; }
"bula"	{printf( "Reserved word: %s\n", yytext ); return BULA; }
"return"	{printf( "Reserved word: %s\n", yytext ); return RETURN; }

{ID}	{printf( "Identifier: %s\n", yytext ); return IDENTIFIER; }

{CST}	{printf( "Constant: %s\n", yytext ); return CONSTANT; }

":"	{printf( "Separator: %s\n", yytext );return COLON; }
";"	{printf( "Separator: %s\n", yytext ); return SEMI_COLON;}
","	{printf( "Separator: %s\n", yytext );return COMA; }
"."	{printf( "Separator: %s\n", yytext ); return DOT;}
"+"	{printf( "Operator: %s\n", yytext ); return PLUS;}
"-"	{printf( "Operator: %s\n", yytext ); return MINUS;}
"*"	{printf( "Operator: %s\n", yytext ); return MULTIPLY;}
"/"	{printf( "Operator: %s\n", yytext ); return DIVISION;}
"%"	{printf( "Operator: %s\n", yytext ); return MOD;}
"("	{printf( "Separator: %s\n", yytext ); return LEFT_ROUND_PARENTHESIS;}
")"	{printf( "Separator: %s\n", yytext );return RIGHT_ROUND_PARENTHESIS; }
"{"	{printf( "Separator: %s\n", yytext );return LEFT_CURLY_PARENTHESIS; }
"}"	{printf( "Separator: %s\n", yytext );return RIGHT_CURLY_PARENTHESIS; }
"["	{printf( "Separator: %s\n", yytext ); return LEFT_SQUARE_PARENTHESIS;}
"]"	{printf( "Separator: %s\n", yytext ); return RIGHT_SQUARE_PARENTHESIS;}
"<"	{printf( "Operator: %s\n", yytext );return LESS_THAN; }
">"	{printf( "Operator: %s\n", yytext ); return GREATER_THAN;}
"<=" {printf( "Operator: %s\n", yytext ); return LESS_OR_EQUAL_THAN;}
">=" {printf( "Operator: %s\n", yytext ); return GREATER_OR_EQUAL_THAN;}
"!=" {printf( "Operator: %s\n", yytext ); return DIFFERENT;}
"==" {printf( "Operator: %s\n", yytext );return EQUAL; }
"="	{printf( "Operator: %s\n", yytext ); return ASSIGNMENT;}
"!"	{printf( "Operator: %s\n", yytext ); return NEGATION; }

[ \t]+	/* elimina spatii */  	{}

[\n]+	{++lines;}

[0-9][a-zA-Z0-9]*	{printf("Illegal identifier at line %d\n", lines); return -1;}

.	{printf("Illegal symbol at line %d\n",lines); return -1;}
%%
/*
void main(int argc,char** argv)
{
if (argc > 1)
{
    FILE *file;
    file = fopen(argv[1], "r");
    if (!file)
    {
        fprintf(stderr, "Could not open %s\n", argv[1]);
        exit(1);
    }
    yyin = file;
}

yylex();
} */
