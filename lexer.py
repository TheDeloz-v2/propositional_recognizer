# Analizador lexico 

import ply.lex as lex

# Tokens
tokens = (
    'VARIABLE', 
    'CONJUNCTION',
    'DISJUNCTION',
    'NEGATION',
    'IMPLICATION',
    'BICONDITIONAL', 
    'CONSTANT', 
    'PARENDER', 
    'PARENIZQ'
)

t_VARIABLE = r'[p-z]'
t_CONJUNCTION = r'\^'
t_DISJUNCTION = r'o'
t_NEGATION = r'\~'
t_IMPLICATION = r'=>'
t_BICONDITIONAL = r'<=>'
t_CONSTANT = r'0|1'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'

# Caracteres ignorados
t_ignore = ' \t'

# Funcion para captar errores lexicos
def t_error(t):
    print(f'Caracter inaceptable: {t.value[0]}')
    t.lexer.skip(1)

# Funcion para captar nueva linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Construir el lexer
lexer = lex.lex()