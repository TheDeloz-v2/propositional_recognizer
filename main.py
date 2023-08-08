from lexer import lexer
from syntax import parser

# Lista de expresiones a evaluar
expressions = [
    '(p=>q)^p',
    'p',
    '~~~q',
    '(p^q)',
    '(0=>(ros))',
    '~(p^q)',
    '(p<=>~p)',
    '((p=>q)^p)',
    '(~(p^(qor))os)'
]

# Lista de resultado
results = []

# Evaluar cada expresion
for expression in expressions:
    lexer.input(expression)
    result = parser.parse(expression, lexer=lexer)
    results.append(result)
    
# Imprimir resultados
for i in range(len(expressions)):
    print(f'{expressions[i]} = {results[i]}')
    print()
    
# Resultados esperados
# (p=>q)^p = ('^', ('=>', 'p', 'q'), 'p')
# p = 'p'
# ~~~q = ('~', ('~', ('~', 'q')))
# (p^q) = ('^', 'p', 'q')
# (0=>(ros)) = ('=>', '0', 'ros')
# ~(p^q) = ('~', ('^', 'p', 'q'))
# (p<=>~p) = ('<=>', 'p', ('~', 'p'))
# ((p=>q)^p) = ('^', ('=>', 'p', 'q'), 'p')
# (~(p^(qor))os) = ('~', ('^', 'p', ('^', 'q', 'or')), 'os')