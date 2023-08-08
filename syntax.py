# Analizador sintactico

import ply.yacc as yacc

# Importe de analizador lexico
from lexer import tokens

# Class Node
# Nodo de un grafo dirigido
class Node:
    _id_counter_ = 0
    
    def __init__(self, label):
        self.id = Node._id_counter_
        Node._id_counter_ += 1
        self.label = label
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
    def _str_helper(self, depth):
        ret = '\t' * depth + self.label + '\n'
        for child in self.children:
            ret += child._str_helper(depth + 1)
        return ret
    
    def __str__(self):
        return self._str_helper(0)

# Reglas de precedencia
precedence = (
    ('left', 'CONJUNCTION', 'DISJUNCTION'),
    ('left', 'IMPLICATION', 'BICONDITIONAL'),
    ('right', 'NEGATION')
)

# Expresion: Variable
def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = Node(p[1])
    
    
# Expresion: Constante
def p_expression_constant(p):
    'expression : CONSTANT'
    p[0] = Node(p[1])
    
# Expresion: Parentesis
def p_expression_parenthesis(p):
    'expression : PARENIZQ expression PARENDER'
    p[0] = p[2]
    
# Expresiones
def p_expression_binop(p):
    '''expression : expression CONJUNCTION expression
                  | expression DISJUNCTION expression
                  | expression IMPLICATION expression
                  | expression BICONDITIONAL expression'''
    node = Node(p[2])
    node.add_child(p[3])
    node.add_child(p[1])
    p[0] = node

# Negacion
def p_expression_negation(p):
    'expression : NEGATION expression %prec NEGATION'
    node = Node(p[1])
    node.add_child(p[2])
    p[0] = node

# Error
def p_error(p):
    print(f'Error de sintaxis en {p.value}')

# Construir el parser
parser = yacc.yacc()
