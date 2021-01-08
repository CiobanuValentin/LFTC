
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     IDENTIFIER = 258,
     CONSTANT = 259,
     FCT = 260,
     MAIN = 261,
     IN = 262,
     OUT = 263,
     IF = 264,
     ELSE = 265,
     FOR = 266,
     WHILE = 267,
     BREAK = 268,
     NUMBER = 269,
     CHAR = 270,
     BULA = 271,
     RETURN = 272,
     TRUE = 273,
     FALSE = 274,
     COLON = 275,
     SEMI_COLON = 276,
     COMA = 277,
     DOT = 278,
     PLUS = 279,
     MINUS = 280,
     MULTIPLY = 281,
     DIVISION = 282,
     MOD = 283,
     LEFT_ROUND_PARENTHESIS = 284,
     RIGHT_ROUND_PARENTHESIS = 285,
     LEFT_SQUARE_PARENTHESIS = 286,
     RIGHT_SQUARE_PARENTHESIS = 287,
     LEFT_CURLY_PARENTHESIS = 288,
     RIGHT_CURLY_PARENTHESIS = 289,
     LESS_THAN = 290,
     GREATER_THAN = 291,
     LESS_OR_EQUAL_THAN = 292,
     GREATER_OR_EQUAL_THAN = 293,
     DIFFERENT = 294,
     EQUAL = 295,
     ASSIGNMENT = 296,
     NEGATION = 297,
     OR = 298,
     AND = 299
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


