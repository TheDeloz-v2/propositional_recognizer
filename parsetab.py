
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCONJUNCTIONDISJUNCTIONleftIMPLICATIONBICONDITIONALrightNEGATIONBICONDITIONAL CONJUNCTION CONSTANT DISJUNCTION IMPLICATION NEGATION PARENDER PARENIZQ VARIABLEexpression : VARIABLEexpression : CONSTANTexpression : PARENIZQ expression PARENDERexpression : expression CONJUNCTION expression\n                  | expression DISJUNCTION expression\n                  | expression IMPLICATION expression\n                  | expression BICONDITIONAL expressionexpression : NEGATION expression %prec NEGATION'
    
_lr_action_items = {'VARIABLE':([0,4,5,6,7,8,9,],[2,2,2,2,2,2,2,]),'CONSTANT':([0,4,5,6,7,8,9,],[3,3,3,3,3,3,3,]),'PARENIZQ':([0,4,5,6,7,8,9,],[4,4,4,4,4,4,4,]),'NEGATION':([0,4,5,6,7,8,9,],[5,5,5,5,5,5,5,]),'$end':([1,2,3,11,12,13,14,15,16,],[0,-1,-2,-8,-4,-5,-6,-7,-3,]),'CONJUNCTION':([1,2,3,10,11,12,13,14,15,16,],[6,-1,-2,6,-8,-4,-5,-6,-7,-3,]),'DISJUNCTION':([1,2,3,10,11,12,13,14,15,16,],[7,-1,-2,7,-8,-4,-5,-6,-7,-3,]),'IMPLICATION':([1,2,3,10,11,12,13,14,15,16,],[8,-1,-2,8,-8,8,8,-6,-7,-3,]),'BICONDITIONAL':([1,2,3,10,11,12,13,14,15,16,],[9,-1,-2,9,-8,9,9,-6,-7,-3,]),'PARENDER':([2,3,10,11,12,13,14,15,16,],[-1,-2,16,-8,-4,-5,-6,-7,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,5,6,7,8,9,],[1,10,11,12,13,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','syntax.py',39),
  ('expression -> CONSTANT','expression',1,'p_expression_constant','syntax.py',45),
  ('expression -> PARENIZQ expression PARENDER','expression',3,'p_expression_parenthesis','syntax.py',50),
  ('expression -> expression CONJUNCTION expression','expression',3,'p_expression_binop','syntax.py',55),
  ('expression -> expression DISJUNCTION expression','expression',3,'p_expression_binop','syntax.py',56),
  ('expression -> expression IMPLICATION expression','expression',3,'p_expression_binop','syntax.py',57),
  ('expression -> expression BICONDITIONAL expression','expression',3,'p_expression_binop','syntax.py',58),
  ('expression -> NEGATION expression','expression',2,'p_expression_negation','syntax.py',66),
]