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

palabras::[Char] -> [[Char]]
palabras [] = []
palabras ls = sacarEspacios (palabrasAux ls [])

palabrasAux :: [Char] -> [Char] -> [[Char]]
palabrasAux [] palabra = [palabra]
palabrasAux (x:xs) palabra | x /= ' '  = palabrasAux xs (palabra ++ [x])
                           | otherwise = [palabra] ++ (palabrasAux xs [])

sacarEspacios :: [[Char]] -> [[Char]]   --Para Strings
sacarEspacios []      =   []
sacarEspacios (x:xs)    | x == [' ']    = sacarEspacios xs  
                        | otherwise     = [x] ++ sacarEspacios xs

palabraMasLarga :: String -> String
palabraMasLarga []  = []
palabraMasLarga ls  = compararLongitud (palabras ls) []

compararLongitud :: [String] -> String -> String
compararLongitud [] a           = a
compararLongitud (x:xs) []      = compararLongitud xs x
compararLongitud (elem:ls) x    | (longitud elem) > (longitud x)    = compararLongitud ls elem
                                | otherwise                         = compararLongitud ls x

aplanar :: [String] -> String
aplanar []      = []
aplanar (x:xs)  = x ++ aplanar xs

aplanarConBlancos :: [String] -> String
aplanarConBlancos []        = []
aplanarConBlancos (x:[])    = x ++ aplanarConBlancos []
aplanarConBlancos (x:xs)    = x ++ " " ++ aplanarConBlancos xs

aplanarConNBlancos :: [[Char]] -> Int -> [Char]
aplanarConNBlancos ls num       | num < 0 = error "no usar numeros menores que 0"
aplanarConNBlancos [] num       = []
aplanarConNBlancos (x:[]) num   = x ++ aplanarConNBlancos [] num
aplanarConNBlancos (x:xs) num   = x ++ (concatenarNVeces " " num) ++ aplanarConNBlancos xs num

concatenarNVeces :: String -> Int -> String
concatenarNVeces ls n   | n <= 0    = ""
                        | otherwise = ls ++ concatenarNVeces ls (n-1)

--type Texto = [Char]

--Ej5
sumaAcumulada :: (Num n) => [n] -> [n]
sumaAcumulada []        = []
sumaAcumulada (x:y:ls)  | null ls   = [x] ++ [x+y]
                        | otherwise = [x] ++ sumaAcumulada ((x+y):ls)

descomponerEnPrimos :: [Int] -> [[Int]] -- Use 2 funciones (separar en multiplos, nEsPrimo) !!! Con numeros muy grandes se traba feo
descomponerEnPrimos []      = []
descomponerEnPrimos (x:xs)  | null xs   = [divisores]
                            | otherwise = [divisores] ++ descomponerEnPrimos xs
                                where divisores = separarEnMultiplos x 1

separarEnMultiplos :: Int -> Int -> [Int] 
separarEnMultiplos 1 contador   = []
separarEnMultiplos x contador   | x `esDivisiblePor` numPrimo   = [numPrimo] ++ separarEnMultiplos (div x numPrimo) 1
                                | otherwise                     = separarEnMultiplos x (contador+1)
                                    where numPrimo  = (nEsPrimo contador)

-- DLC 5++: Expansion pack + enemigos nuevos

--Ej1

type Punto2D = (Float, Float)
type Coordenada = (Float, Float)

prodInt :: Punto2D -> Punto2D -> Punto2D
prodInt (a,b) (c,d) = (a*c, b*d)

todoMenor :: Punto2D -> Punto2D -> Bool
todoMenor (x,y) (a, b) = ((x,y) >= (a,b))

distanciaPuntos :: Punto2D -> Punto2D -> Punto2D
distanciaPuntos (a,b) (c,d) = (abs(a-c), abs(b-d))

crearPar :: Float -> Float -> Coordenada
crearPar x y = (x,y)

--Ej2

type Año        = Int
type EsBisiesto = Bool

bisiesto :: Año -> EsBisiesto
bisiesto año  | not (esMultiploDePNeg año 4) || (esMultiploDePNeg año 100) && not (esMultiploDePNeg año 400) = False
              | otherwise = True
esMultiploDePNeg :: Int -> Int -> Bool
esMultiploDePNeg a b  | mod (abs a) (abs b) ==  0     =   True
                      | otherwise                     =   False

--Ej3

type Coordenada3D =  (Float,Float,Float)
distanciaManhattan :: Coordenada3D -> Coordenada3D -> Float
distanciaManhattan (a,b,c) (x,y,z) = abs(l) + abs (m) + abs (n)
                                    where (l,m,n) = (a-x,b-y,c-z) 

--Ej4

type Texto = String
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos nombre []                = False
enLosContactos nombre (contacto:lista)  | nombre == (elNombre contacto) = True
                                        | otherwise                     = False || enLosContactos nombre lista
                                    

agregarContactos :: Contacto -> ContactosTel -> ContactosTel
agregarContactos persona []                 = [persona]
agregarContactos persona (contacto:lista)   | (elNombre persona) == (elNombre contacto) = [] ++ agregarContactos persona lista
                                            | otherwise                                 = [contacto] ++ agregarContactos persona lista

eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto nombre []                  = []
eliminarContacto nombre (contacto:lista)    | ((elNombre contacto) == nombre)   = [] ++ eliminarContacto nombre lista   
                                            | otherwise                         = [contacto] ++ eliminarContacto nombre lista

elNombre :: Contacto -> Nombre
elNombre contacto   = (fst contacto)

elTelefono :: Contacto -> Telefono
elTelefono contacto   = (snd contacto)

--Ej5

type Identificacion = Int
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
data Disponibilidad = Libre | Ocupado deriving (Eq, Show)

existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker id []                = False
existeElLocker id (locker:lista)    | id == (laIdentificacion locker)   = True
                                    | otherwise                         = False || existeElLocker id lista

ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker id (locker:lista)    | not (existeElLocker id (locker:lista))    = error "Prube un locker existente"
                                        | laIdentificacion locker == id             = laUbicacion (elEstado locker)
                                        | otherwise                                 = ubicacionDelLocker id lista

estaDisponibleElLocker :: Identificacion ->MapaDeLockers ->Bool
estaDisponibleElLocker id (locker:lista)    | not (existeElLocker id (locker:lista))    = error "Prube un locker existente"
                                            | laIdentificacion locker == id             = estaDisponible (laDisponibilidad (elEstado locker))
                                            | otherwise                                 = estaDisponibleElLocker id lista

ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker id []              = []
ocuparLocker id (locker:lista)  | laIdentificacion locker == id             = [(id,(Ocupado, laUbicacion (elEstado locker)))] ++ ocuparLocker id lista
                                | otherwise                                 = [locker] ++ ocuparLocker id lista

laIdentificacion :: Locker -> Identificacion
laIdentificacion locker = fst locker 

elEstado :: Locker -> Estado
elEstado locker = snd locker

laDisponibilidad :: Estado -> Disponibilidad
laDisponibilidad estado = fst estado

estaDisponible :: Disponibilidad -> Bool
estaDisponible Libre    = True
estaDisponible Ocupado  = False

laUbicacion :: Estado -> Ubicacion
laUbicacion estado  = snd estado