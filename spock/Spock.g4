grammar Spock;

options { caseInsensitive=true; }

// Parser Rules
program : statement* ;

statement : declaration
          | definition
          | assignment
          | printStatement 
          | whileLoop
          | returnStatement
          | ifStatement
          | block ;

printStatement : PRINT expression ;

returnStatement : RETURN expression ;

block : BEGIN statement+ FINISH ;

id : ID_PART+ ;

declaration : DECLARE id ;

// type : 'function' | 'integer' | 'string' ;

assignment : id EQUALS expression | SET id AS expression;

definition : DEFINE id AS expression ;

whileLoop : WHILE expression statement ;

ifStatement : IF expression statement ;

expression : id
           | STRING
           | NUMBER
           | WORD_NUMBER
           | lambda
           | call ;

lambda : LAMBDA (TAKES arglist)? DOES block ;

call : CALL expression WITH list | CALL expression LEFT list RIGHT ;

arglist : id (AND id)* ;

// list : 'left' expression+ 'right' ;
// list : expression | expression+ 'and' expression ;

list : expression (AND expression)* ;

// Lexer Rules
PRINT : 'print' ;
RETURN : 'return' ;
BEGIN : 'begin';
FINISH : 'finish';
DECLARE : 'declare';
DEFINE : 'define' ;
EQUALS : 'equals';
WHILE : 'while';
IF : 'if';
LAMBDA : 'lambda';
TAKES : 'takes';
DOES : 'does';
CALL : 'call' | 'col';
AND : 'and';
SET : 'set';
AS : 'as';
WITH : 'with';
LEFT : 'left';
RIGHT : 'right';


WORD_NUMBER : 'zero' | 'one' | 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine' | 'ten'
            | 'eleven' | 'twelve' | 'thirteen' | 'fourteen' | 'fifteen' | 'sixteen' | 'seventeen' | 'eighteen' | 'nineteen' | 'twenty' ;

STRING : 'quote' .*? 'unquote' ;
NUMBER : [0-9]+ ;
ID_PART : [a-z]+ ;


// Single-line comment
COMMENT : 'comment' ~[\r\n]* -> skip ;

// Multi-line comment
MULTILINE_COMMENT : 'escape' .*? 'unescape' -> skip ;

// Ignore whitespace
WS : [ \t\r\n]+  -> skip ;
FLUSH : 'flush' -> skip ;
