# A simple lexical analyzer for PHP source code using PLY

from ply import lex

# List of PHP keywords
keywords = {
    'PRINT': 'PRINT',
    'ECHO': 'ECHO',
    'IF': 'IF',
    'ELSE': 'ELSE',
    'WHILE': 'WHILE',
    'FOR': 'FOR',
    'FUNCTION': 'FUNCTION',
    'RETURN': 'RETURN',
}

# List of tokens
tokens = list(keywords.values()) + [
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'RCURLY', 'LCURLY', 'LT', 'LE', 'GT', 'GE', 'NE',
    'CONCAT', 'COMMA', 'SEMI', 'NOT', 'MOD','IDENTIFIER', 'NUMBER', 'STRING',
    'NEWLINE', 'COMMENT', 'PHP_OPEN', 'PHP_CLOSE',
]

# Ignore whitespace
t_ignore = ' \t'

# Token definitions
def t_PHP_OPEN(t):
    r'\<\?php'
    return t

def t_PHP_CLOSE(t):
    r'\?\>'
    return t

def t_COMMENT(t):
    r'//.*'
    pass  # Ignore comments

def t_PRINT(t):
    r'PRINT'
    return t

def t_ECHO(t):
    r'ECHO'
    return t

def t_IF(t):
    r'IF'
    return t

def t_ELSE(t):
    r'ELSE'
    return t

def t_WHILE(t):
    r'WHILE'
    return t

def t_FOR(t):
    r'FOR'
    return t

def t_FUNCTION(t):
    r'FUNCTION'
    return t

def t_RETURN(t):
    r'RETURN'
    return t

def t_IDENTIFIER(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'  # Identifiers start with $ followed by letters or numbers
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert to integer
    return t

def t_STRING(t):
    r'"([^"\\]*(\\.[^"\\]*)*)"'
    return t

t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'<>'
t_CONCAT = r'\.'  # Concatenation operator
t_COMMA = r','
t_SEMI = r';'
t_NOT = r'!'
t_MOD = r'%'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lex.lex(debug=0)

# Function to analyze input code
def analyze_code(code):
    lex.input(code)
    while True:
        token = lex.token()  # Get the next token
        if not token:  # If there are no more tokens, break
            break
        print(token)

# Example PHP code snippets to analyze

# Example 1: Simple Print Statements
php_code_1 = '''<?php //php 7.2.24
PRINT "Hello, world! \\n"; ECHO "Welcome"; ?>'''

# Example 2: Simple Arithmetic Expression
php_code_2 = '''<?php
$num1 = 10; $num2 = 20; $num3 = 30;
$sum = $num1 + $num2 + $num3; $avg = $sum / 3;
PRINT "Num1 is " . $num1 . "\\n"; PRINT "Num2 is " . $num2 . "\\n"; ?>'''

# Example 3: Simple Conditional IF with Block
php_code_3 = '''<?php //php 7.2.24
$num1 = 10; $num2 = 20; IF ($num1 > $num2) {
    $bignum = $num1; PRINT "Big Number is " . $bignum;
} ELSE {
    $bignum = $num2; PRINT "Big Number is " . $bignum;
} ?>'''

# Example 4: Simple Looping with Conditional IF Block
php_code_4 = '''<?php //php 7.2.24
PRINT "List of Odd Number 1-100:\\n"; $num = 1; WHILE ($num <= 100) {
    IF (($num % 2) != 0) {
        PRINT "" . $num . " ";
    }
    $num = $num + 1;
} ?>'''

# Analyze each example PHP code
print("Analyzing PHP Code 1:")
analyze_code(php_code_1)
print("\nAnalyzing PHP Code 2:")
analyze_code(php_code_2)
print("\nAnalyzing PHP Code 3:")
analyze_code(php_code_3)
print("\nAnalyzing PHP Code 4:")
analyze_code(php_code_4)