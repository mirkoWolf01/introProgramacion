--Ej1
longitud :: [t] -> Int
longitud []     = 0 
longitud t      = 1 + (longitud (tail t))

ultimo :: [l] -> l
ultimo (l:ls)   | (longitud (l:ls)) == 1    = l
                | otherwise                 = (ultimo ls)

principio :: [l] -> [l]
principio (l:ls)    | (longitud ls) == 0    = []
                    | otherwise             = l:(principio ls)

reverso :: [l] -> [l]
reverso []  = []
reverso l   = (ultimo l):(reverso (principio l))

--Ej2
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece a []      = False
pertenece a (l:ls)  = (a == l) || (pertenece a ls)

todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:xs) | xs == []  = True
                    | otherwise = (x == (head xs)) && todosIguales (xs)

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:xs)   | xs == []  = True
                        | otherwise = (x /= (head xs)) && todosDistintos (xs)

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos (x:xs) | xs == []  = False
                    | otherwise = (pertenece x xs) || (hayRepetidos xs)

quitar :: (Eq t) => t -> [t] -> [t]
quitar a (x:xl) | a == x        = xl
                | otherwise     = x:(quitar a xl)

{- quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos a (x:xs)    | not (pertenece a (x:xs))  = (x:xs)
                        | otherwise                 = quitarTodos a (quitar a (x:xs)): quitar -}