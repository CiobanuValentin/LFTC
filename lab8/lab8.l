%{
#include <math.h>
#include <stdio.h>
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

"fct"	{printf( "Reserved word: %s\n", yytext );  }
"Main"	{printf( "Reserved word: %s\n", yytext );  }
"in>>"	{printf( "Reserved word: %s\n", yytext );  }
"out<<"	{printf( "Reserved word: %s\n", yytext );  }
"if"	{printf( "Reserved word: %s\n", yytext );  }
"else"	{printf( "Reserved word: %s\n", yytext );  }
"for"	{printf( "Reserved word: %s\n", yytext );  }
"break"	{printf( "Reserved word: %s\n", yytext );  }
"Number"	{printf( "Reserved word: %s\n", yytext );  }
"char"	{printf( "Reserved word: %s\n", yytext );  }
"bula"	{printf( "Reserved word: %s\n", yytext );  }
"return"	{printf( "Reserved word: %s\n", yytext );  }

{ID}	{printf( "Identifier: %s\n", yytext ); }

{CST}	{printf( "Constant: %s\n", yytext ); }

":"	{printf( "Separator: %s\n", yytext ); }
";"	{printf( "Separator: %s\n", yytext ); }
","	{printf( "Separator: %s\n", yytext ); }
"."	{printf( "Separator: %s\n", yytext ); }
"+"	{printf( "Operator: %s\n", yytext ); }
"-"	{printf( "Operator: %s\n", yytext ); }
"*"	{printf( "Operator: %s\n", yytext ); }
"/"	{printf( "Operator: %s\n", yytext ); }
"%"	{printf( "Operator: %s\n", yytext ); }
"("	{printf( "Separator: %s\n", yytext ); }
")"	{printf( "Separator: %s\n", yytext ); }
"{"	{printf( "Separator: %s\n", yytext ); }
"}"	{printf( "Separator: %s\n", yytext ); }
"["	{printf( "Separator: %s\n", yytext ); }
"]"	{printf( "Separator: %s\n", yytext ); }
"<"	{printf( "Operator: %s\n", yytext ); }
">"	{printf( "Operator: %s\n", yytext ); }
"<=" {printf( "Operator: %s\n", yytext ); }
">=" {printf( "Operator: %s\n", yytext ); }
"!=" {printf( "Operator: %s\n", yytext ); }
"==" {printf( "Operator: %s\n", yytext ); }
"="	{printf( "Operator: %s\n", yytext ); }
"!"	{printf( "Operator: %s\n", yytext ); }
"||"	{printf( "Operator: %s\n", yytext ); }
"&&"	{printf( "Operator: %s\n", yytext ); }

[ \t]+	/* elimina spatii */  	{}

[\n]+	{++lines;}

[0-9][a-zA-Z0-9]*	{printf("Illegal identifier at line %d\n", lines); return -1;}

.	{printf("Illegal symbol at line %d\n",lines); return -1;}
%%
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
}
