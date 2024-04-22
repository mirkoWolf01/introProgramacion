--import AlgoritmosUtiles

--Ej1
longitud :: [t] -> Int      --length
longitud []     = 0 
longitud t      = 1 + (longitud (tail t))

ultimo :: [l] -> l          -- last
ultimo (l:ls)   | (longitud (l:ls)) == 1    = l
                | otherwise                 = (ultimo ls)

principio :: [l] -> [l]     -- init
principio (l:ls)    | (longitud ls) == 0    = []
                    | otherwise             = l:(principio ls)

reverso :: [l] -> [l]   --reverse
reverso []  = []
reverso l   = (ultimo l):(reverso (principio l))

--Ej2
pertenece :: (Eq t) => t -> [t] -> Bool     --elem
pertenece a []      = False
pertenece a (l:ls)  = (a == l) || (pertenece a ls)

todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:[]) = True
todosIguales (x:xs) = (x == (head xs)) && todosIguales (xs)

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:[])       = True
todosDistintos (x:xs)       = not(pertenece x xs) && todosDistintos (xs)

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos  []                = False
hayRepetidos (x:xs)             = (pertenece x xs) || (hayRepetidos xs)

quitar :: (Eq t) => t -> [t] -> [t]
quitar a (x:xl) | a == x        = xl
                | otherwise     = x:(quitar a xl)

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos a []                                                = []
quitarTodos a (x:xs)    | a == x                                = []++(quitarTodos a xs)
                        | otherwise                             = [x]++(quitarTodos a xs)

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos []        = []
eliminarRepetidos (x:xs)    = [x] ++ eliminarRepetidos (quitarTodos x xs) 

mismosElementos ::  (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ys   = (todosPertenecen xs ys) && (todosPertenecen ys xs)

todosPertenecen :: (Eq t) => [t] -> [t] -> Bool --Aux Para mismosElementos
todosPertenecen (x:[]) ys = (x `pertenece` ys)
todosPertenecen (x:xs) ys = (x `pertenece` ys) && (todosPertenecen xs ys)

capicua :: (Eq t) => [t] -> Bool 
capicua xl  = (xl == (reverso xl))

--Ej3