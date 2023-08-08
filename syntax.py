# Analizador sintactico

import ply.yacc as yacc

# Importe de analizador lexico
from lexer import tokens

# Expresion: Variable
def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = p[1]
    
# Expresion: Constante
def p_expression_constant(p):
    'expression : CONSTANT'
    p[0] = p[1]
    
# Expresion: Parentesis
def p_expression_parenthesis(p):
    'expression : PARENIZQ expression PARENDER'
    p[0] = p[2]

# Expresion: Negacion
def p_expression_negation(p):
    'expression : NEGATION expression'
    p[0] = ('~', p[2])

# Expresiones
def p_expression_conjunction(p):
    'expression : expression CONJUCTION expression'
    p[0] = ('^', p[1], p[3])
    
def p_expression_disjunction(p):
    'expression : expression DISJUNCTION expression'
    p[0] = ('o', p[1], p[3])

def p_expression_implication(p):
    'expression : expression IMPLICATION expression'
    p[0] = ('=>', p[1], p[3])

def p_expression_biconditional(p):
    'expression : expression BICONDITIONAL expression'
    p[0] = ('<=>', p[1], p[3])

# Error
def p_error(p):
    print(f'Error de sintaxis en {p.value}')

# Construir el parser
parser = yacc.yacc()
