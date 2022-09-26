%Materias|codigo | nombre | cuatrimestre | año | aprobada
materias(6111,'Introducción a la Programación 1',1,1,1).
materias(6112,'Análisis Matemático 1',1,1,1).
materias(6113, "Algebra I.", 1, 1, 1).
materias(6114, "Quimica.", 1, 1, 1).
materias(6121, "Ciencias de la Computacion I.", 2, 1, 1).
materias(6122, "Introduccion a la Programacion II.", 2, 1. 1).
materias(6123, "Algebra Lineal.", 2, 1, 1).
materias(6124, "Fisica General.", 2, 1, 1).
materias(6125, "Matematica Discreta.", 2, 1, 1).
materias(6211, "Ciencias de la Computacion II.", 1, 2, 1).
materias(6212, "Analisis y Diseño de Algoritmos I.", 1, 2, 1).
materias(6213, "Introduccion a la Arquitectura de Sistemas.", 1, 2, 1).
materias(6214, "Analisis Matematico II.", 1, 2, 1).
materias(6215, "Electricidad y Magnetismo.", 1, 2, 1).
materias(6221, "Analisis y Diseño de Algoritmos II.", 2, 2, 1).
materias(6222, "Comunicacion de Datos I.", 2, 2, 1).
materias(6223, "Probabilidades y Estadistica.", 2, 2, 1).
materias(6224, "Electronica Digital.", 2, 2, 1).
materias(6225, "Ingles.", 2, 2, 1).
materias(6311, "Programacion Orientada a Objetos.", 1, 3, 1).
materias(6312, "Estructuras de Almacenamiento de Datos.", 1, 3, 1).
materias(6313, "Metodologias de Desarrollo de Software I.", 1, 3, 1).
materias(6314, "Arquitectura de Computadoras I.", 1, 3, 1).
materias(6321, "Programacion Exploratoria.", 2, 3, 0).
materias(6322, "Base de Datos I.", 2, 3, 0).
materias(6323, "Lenguajes de Programacion I.", 2, 3, 0).
materias(6324, "Sistemas Operativos I.", 2, 3, 0).
materias(6325, "Investigacion Operativa I.", 2, 3, 0).
materias(6411, "Arquitectura de Computadoras y Tecnicas Digitales.", 1, 4, 0).
materias(6412, "Teoria de la Informacion.", 1, 4, 0).
materias(6413, "Comunicacion de Datos II.", 1, 4, 0).
materias(6414, "Introduccion al Calculo Diferencial e Integral.", 1, 4, 1).
materias(6421, "Diseño de Sistemas de Software.", 2, 4, 0).
materias(6422, "Diseño de Compiladores. I", 2, 4, 0).
materias(6511, "Ingenieria de Software.", 1, 5, 0).

%correlativas codigo | lista de correlativas
correlativa(6111,[]).
correlativa(6112,[]).
correlativa(6113,[]).
correlativa(6114,[]).
correlativa(6121,[]).
correlativa(6122, [6111]).
correlativa(6123, [6113]).
correlativa(6124, [6112]).
correlativa(6125, [6113]).
correlativa(6211, [6121,6122,6125]).
correlativa(6212, [6121, 6122, 6125]).
correlativa(6213, [6122]).
correlativa(6214, [6112]).
correlativa(6215, [6124]).
correlativa(6221, [6211, 6212]).
correlativa(6222, [6213]).
correlativa(6223, [6214, 6123, 6125]).
correlativa(6224, [6215]).
correlativa(6311, [6221]).
correlativa(6312, [6221, 6223]).
correlativa(6313, [6221]).
correlativa(6314, [6213, 6224]).
correlativa(6321, [6221]).
correlativa(6322, [6312, 6313]).
correlativa(6323, [6311]).
correlativa(6324, [6312, 6314]).
correlativa(6325, [6214, 6223]).
correlativa(6411, [6314]).
correlativa(6412, [6212, 6222, 6223]).
correlativa(6413, [6222, 6324]).
correlativa(6414, [6214]).
correlativa(6421, [6311, 6322, 6324]).
correlativa(6422, [6323]).
correlativa(6511, [6421]).

%info personal
soy("juan").

le_gusta(juan, programar).
le_gusta(juan, ia).
le_gusta(juan, machine learning).
le_gusta(juan, matematica).
le_gusta(juan, socializar).
le_gusta(juan, hablar).
le_gusta(juan, dirigir).

%Reglas de materias

%imprime en pantalla una a una las materias
materias_de(X):- 
    write("Materias del curso: "),
    writeln(X),
    materias(_,Nombre,_,X,_),
    writeln(Nombre),
    fail.

materias_de(X).

%devuelve una lista de todas las materias de la carrera
materias_totales_fa(Result) :-
    findall(Nombre, materias(_,Nombre,_,_,_), Result).

%devuelve una lista de las materias de un año
materias_de_fa(X, Result) :-
    findall(Nombre, materias(_,Nombre,_,X,_), Result).


%devuelve una lista de las materias aprobadas
materias_aprobadas_fa(Result) :-
    findall(Nombre, materias(_,Nombre,_,_,1), Result).

%devuelve una lista de las materias restantes
materias_restantes_fa(Result) :-
    findall(Nombre, materias(_,Nombre,_,_,0), Result).


%devuelve las materias que solo necesitas una correlativa
materias_con_una_correlativa:-
    correlativa(Codigo,[CodCorrelativa]), %%%
    materias(Codigo,Nombre,_,_,_),
    materias(CodCorrelativa,NombreCorrelativa,_,_,_),
    write("Para hacer "),
    write(Nombre),
    write(" solo necesitas "),
    writeln(NombreCorrelativa),
    fail.
    
materias_con_una_correlativa.
        

plan_is:-
    materias(CodigoMateria,NombreMateria,Cuatri, Anio),
    write("Curso:"), 
    write(Anio),
    write(" Cua:"),
    write(Cuatri),
    write(" Nom:"),
    write(NombreMateria),
    correlativa(CodigoMateria, ListaDeCorrelativas),
    (ListaDeCorrelativas == [] ->			%es un if
    	writeln("")
    	;  
    	write(" Correlativas: "),
    	mostrar_lista_correlativas(ListaDeCorrelativas),
    	writeln("")
    ),
    fail.

plan_is.

%
mostrar_lista_correlativas([]).

mostrar_lista_correlativas([Head | Tail]):-
    member(CodCorrelativa, [Head | Tail]), %recorro por cada correlativa
    materias(CodCorrelativa,NombreCorre,_,_,_),
    write(NombreCorre),
    write(" "),
    fail.

mostrar_lista_correlativas([Head | Tail]).





