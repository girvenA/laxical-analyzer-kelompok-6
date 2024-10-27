import ply.lex as lex

# list of token names
okens = [
    'PRINT', 'ECHO',
    'IF', 'ELSE', 'WHILE',
    'ID', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'MODULO', 'DIVIDE',
    'ASSIGN', 'SEMICOLON',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'NEWLINE', 'COMMENT'
]

# regular expression rules for simple tokens
t_PRINT = r'PRINT'
t_ECHO = r'ECHO'
t_IF = r'IF'
t_ELSE = r'ELSE'
t_WHILE = r'WHILE'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MODULO = r'%'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMENT = r'//.*|/\*.*?\*/'

# a regular expression rule
def t_ID(t):
    r'\$[a-zA-Z_][a-zA-z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]*(\\.[^"\\]*)*)"'
    t.value = t.value[1:-1]
    return t

# define a rule
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# gnored white
t_ignore = ' \t'

#error handler
def t_error(t):
    print("Illegal Character '{%t.value[0]}'")
    t.lexer.skip(1)

# create lexer
lexer = lex.lex()
