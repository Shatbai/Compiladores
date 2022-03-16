grammar marzo;

program : expression+ |declarar+;
expression: 
    expression '+' expression #suma
    | Numero                  #primaria
    | Variable                #variable
    ;
comparar:
expression '<'expression #comp
|Boolean #boleano
;

declarar:
'var' Variable #declaracion; 

asignar:
Variable '=' expression #asig;

sentencias:
'si' expression 'entonces' sentencias #ifnoelse 
|'si' expression 'entonces' sentencias 'si no' sentencias#ifelse;



// A continuación los tokens (comienzan con mayúscula)
Numero : [0-9]+;
Boolean: [0-1]+;
Variable: [A-z]+;
WS : [ \t\n\r]+ -> skip ;


