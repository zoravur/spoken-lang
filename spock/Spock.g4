grammar Spock;

options { caseInsensitive=true; }

// Parser Rules
program : statement+ ;

statement : declaration
          | definition
          | assignment
          | printStatement 
          | whileLoop
          | returnStatement
          | ifStatement
          | block ;

printStatement : 'print' expression ;

returnStatement : 'return' expression ;

block : 'begin' statement+ 'end' ;

declaration : 'declare' ID ;

type : 'function' | 'integer' | 'string' ;

assignment : ID 'equals' expression ;

definition : 'define' ID 'equals' expression ;

whileLoop : 'while' 'left' expression 'right' statement ;

ifStatement : 'if' 'left' expression 'right' statement ;

expression : ID
           | STRING
           | NUMBER
           | WORD_NUMBER
           | lambda
           | call ;

lambda : 'lambda' 'takes' arglist 'and' 'does' block ;

call : 'call' ID list ;

arglist : 'left' ID+ 'right' ;

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
