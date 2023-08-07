import ply.lex as lex

tokens = (
    'VARIABLE', 
    'OPERATOR', 
    'CONSTANT', 
    'LPAREN', 
    'RPAREN'
)

# Tokens
t_VARIABLE = r'[p-z]'
t_OPERATOR = r'~|\^|o|=>|<=>'
t_CONSTANT = r'0|1'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'

# Caracteres ignorados
t_ignore = ' \t'

# Funcion para captar errores lexicos
def t_error(t):
    print(f'Caracter inaceptable: {t.value[0]}')
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()