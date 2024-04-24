import AlgoritmosUtiles

--Ej1
longitud :: [t] -> Int      --length
longitud []     = 0 
longitud (x:xs) = 1 + (longitud xs)

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
todosIguales (x:xs) = (x == (xs !! 0)) && todosIguales (xs)

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
quitarTodos a []                    = []
quitarTodos a (x:xs)    | a == x    = []++(quitarTodos a xs)
                        | otherwise = [x]++(quitarTodos a xs)

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
sumatoria :: [Int] -> Int
sumatoria []        = 0
sumatoria (x:xs)    = x + (sumatoria xs)

productoria :: [Int] -> Int
productoria []        = 1
productoria (x:xs)    = x * (productoria xs)

maximo :: [Int] -> Int      --maximum
maximo []       = error "Entrada no valida. Se requiere una lista de numeros enteros."
maximo (x:xs)   | null xs           = x
                | x > elSiguiente   = maximo (quitarTodos elSiguiente (x:xs))
                | otherwise         = maximo xs
                    where elSiguiente = xs !! 0

minimo :: [Int] -> Int      --minimum
minimo []       = error "Entrada no valida. Se requiere una lista de numeros enteros."
minimo (x:xs)   | null xs           = x
                | x < elSiguiente   = minimo (quitarTodos elSiguiente (x:xs))
                | otherwise         = minimo xs
                    where elSiguiente = xs !! 0

sumarN :: Int -> [Int] -> [Int]
sumarN a []     = []
sumarN a (x:xs) | null xs   = [sum]
                | otherwise = [sum] ++ sumarN a xs
                    where sum = a+x

sumarElPrimero :: [Int] -> [Int] 
sumarElPrimero []       = error "Entrada no valida. Se requiere una lista de numeros enteros."
sumarElPrimero (x:xs)   = sumarN x (x:xs)

sumarElUltimo :: [Int] -> [Int] 
sumarElUltimo []        = error "Entrada no valida. Se requiere una lista de numeros enteros."
sumarElUltimo (xs)      = sumarN (xs !! ((longitud xs) -1)) xs 

pares :: [Int] -> [Int]
pares []        = []
pares (x:xs)    | esPar x   = [x] ++ pares xs
                | otherwise = pares xs

multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN  a []      = []
multiplosDeN  a (x:xs)  | x `esDivisiblePor` a = [x] ++ multiplosDeN a xs
                        | otherwise         = multiplosDeN a xs

ordenar :: [Int] -> [Int]
ordenar []      = []
ordenar (x:xs)  | null xs   = [x]
                | otherwise = [min] ++ ordenar (quitar min (x:xs))
                    where min = minimo(x:xs)

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos []        = []
sacarBlancosRepetidos (x:xs)    | null xs                       = [x]
                                | x == ' ' && x == (xs !! 0)    = [] ++ sacarBlancosRepetidos xs
                                | otherwise                     = [x] ++ sacarBlancosRepetidos xs

contarPalabras :: [Char] -> Integer
contarPalabras []                                       = 0
contarPalabras (x:[])   | x == ' '                      = 0
                        | otherwise                     = 1
contarPalabras (x:xs)   | x /= ' ' && (xs !! 0) == ' '  = 1 + contarPalabras xs
                        | otherwise                     = 0 + contarPalabras xs

{- palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (x:[]) | x == ' '                      = []
                | otherwise                     = [x]
 -}

{- recortar :: [Char] -> [Char]
recortar [] = []
 -}