/*

Help me write a g4 file for the following language, Spock, which is designed to be spoken aloud. It has no punctuation, only words. it is case insensitive, and whitespace insensitive:

program : statement+
statement : declaration | assignment | PRINT expression | block ; // Is a declaration a type of assignment? I don't know
block: BEGIN statement+ END
declaration : DECLARE ID ;
type : FUN, INT, STR ;
assignment : ID EQUALS expression ;
expression : ID | STRING | NUMBER | lambda ;
lambda : LAMBDA TAKES list AND DOES block
list : BEGIN ID+ END


// Lexer rules -- these are regexes, meaning the words are just equivalent to themselves
DECLARE : declare ;
ID : [a-zA-Z]+ ;
FUN : function ;
INT : integer ;
STR : string ;
EQUALS : equals ;
STRING : quote \w+ unquote ;
NUMBER : \d+ ;
LAMBDA : lambda
TAKES : takes ;
AND : and ;
DOES : does ;
BEGIN : begin ;
END : end ;

*/

grammar Spock;

options { caseInsensitive=true; }

// Parser Rules
program : statement+ ;

statement : declaration
          | assignment
          | printStatement 
          | whileLoop
          | block ;

printStatement : 'print' expression ;

block : 'begin' statement+ 'end' ;

declaration : 'declare' ID type? ;

type : 'function' | 'integer' | 'string' ;

assignment : ID 'equals' expression ;

whileLoop : 'while' 'left' expression 'right' statement ;

expression : ID
           | STRING
           | NUMBER
           | WORD_NUMBER
           | lambda
           | call ;

lambda : 'lambda' 'takes' arglist 'and' 'does' block ;

call : 'call' ID list ;

arglist : 'begin' ID+ 'end' ;

list : 'left' expression+ 'right' ;

WORD_NUMBER : 'zero' | 'one' | 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine' | 'ten'
            | 'eleven' | 'twelve' | 'thirteen' | 'fourteen' | 'fifteen' | 'sixteen' | 'seventeen' | 'eighteen' | 'nineteen' | 'twenty' ;

// Lexer Rules
ID : [a-zA-Z]+ ;
STRING : 'quote' .*? 'unquote' ;
NUMBER : [0-9]+ ;


// Single-line comment
COMMENT : 'comment' ~[\r\n]* -> skip ;

// Multi-line comment
MULTILINE_COMMENT : 'begin comment' .*? 'end comment' -> skip ;

// Ignore whitespace
WS : [ \t\r\n]+  -> skip ;
FLUSH : 'flush' -> skip ;
