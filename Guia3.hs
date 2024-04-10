--Ej2 
absoluto :: Int -> Int 
absoluto x = abs x

{-
problema maximoAbsoluto(x,y:Z): Z
requiere: {True}
asegura:  {cual de los dos valores absolutos es mayor} 
-}
maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y  | absoluto(x) > absoluto(y) = x
                    | otherwise                 = y

{-
problema algunoEs0(a,b:R): Bool
requiere: {True}
asegura:  {Para a = 0 o b = 0, devuelve un True sino False} 
-}
algunoEs0 :: Float -> Float -> Bool
algunoEs0 a b   | a /= 0 && b /= 0 = False
                | otherwise        = True

algunoEs0Pattern :: Float -> Float -> Bool
algunoEs0Pattern 0 b = True
algunoEs0Pattern a 0 = True
algunoEs0Pattern a b = False

{-
problema ambosSon0(a,b:R): Bool
requiere: {True}
asegura:  {Para a = 0 Y b = 0 devuelve un True sino False} 
-}
ambosSon0 :: Float -> Float -> Bool
ambosSon0 a b   | a /= 0 || b /= 0  = False
                | otherwise         = True

ambosSon0PPattern :: Float -> Float -> Bool
ambosSon0PPattern 0 0 = True
ambosSon0PPattern a b = False

{-
problema mismoIntervalo(a,b:R): Bool
requiere: {True}
asegura:  {Tanto a como b tienen que pertenecer al mismo intervalo de entre los siguientes intervalos (−∞, 3] o (3, 7] o (7, ∞) }
-}

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo a b  | a <= 3 &&  b <= 3                         = True
                    | a > 7  &&  b > 7                          = True
                    | a > 3  &&  a <= 7 && b > 3  &&  b <= 7    = True
                    | otherwise                                 = False

{-
problema  esMultiploDe(a,b:N): Bool
requiere: {True}
asegura:  {si a es k veces b, k siendo un numero natural, devuelve True}
-}

esMultiploDe :: Int -> Int -> Bool
esMultiploDe a b    | a <= 0            =   False
                    | b <= 0            =   False
                    | mod a b ==  0     =   True
                    | otherwise         =   False

esMultiploDePNeg :: Int -> Int -> Bool
esMultiploDePNeg a b  | mod (abs a) (abs b) ==  0     =   True
                      | otherwise                     =   False
--Ej3

{-
  a +  b ∗ k = 0
  (b*k)/a - 1 = 0
  por ende b tiene que ser un multiplo de a para que de 1, todo esto con a /= 0
-}

estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b   | a == 0 || b == 0              = False
                        | mod (abs a) (abs b) ==  0     =   True
                        | otherwise                     = False

--Ej4 

prodInt :: (Float,Float) -> (Float,Float) -> (Float,Float)
prodInt (a,b) (c,d) = (a*c, b*d)

distanciaPuntos :: (Float,Float) -> (Float,Float) -> (Float,Float) 
distanciaPuntos (a,b) (c,d) = (abs(a-c), abs(b-d))

sumaTerna :: (Int,Int,Int) -> Int
sumaTerna (a,b,c) = a+b+c

devuelveMultiplo :: Int -> Int -> Int
devuelveMultiplo a b  | (esMultiploDePNeg a b) = a
                      | otherwise              = 0

sumarSoloMultiplos :: (Int,Int,Int)  -> Int -> Int
sumarSoloMultiplos (a,b,c) x  = (devuelveMultiplo a x) + (devuelveMultiplo b x) + (devuelveMultiplo c x)


posPrimerPar :: (Int,Int,Int) -> Int
posPrimerPar (a,b,c)  | (esMultiploDePNeg a 2) == True  = 1
                      | (esMultiploDePNeg b 2) == True  = 2
                      | (esMultiploDePNeg c 2) == True  = 3
                      |otherwise                        = 4

crearPar :: a -> b -> (a,b)
crearPar x y = (x,y)

inverir :: (a,b) -> (b,a)
inverir (a,b) = (b,a)

--Ej5

f :: Int -> Int
f   n   | n <= 7 = n*n
        | n > 7  = 2*n-1

g :: Int -> Int
g   n   | (esMultiploDePNeg n 2)  = div n 2
        | otherwise               = 3*n + 1

todosMenores :: (Int, Int, Int) -> Bool
todosMenores (a,b,c)  | (f a) > (g a) && (f b) > (g b) && (f c) > (g c) = True
                      | otherwise                                       = False

--Ej6 

bisiesto :: Int -> Bool 
bisiesto año  | not (esMultiploDePNeg año 4) || (esMultiploDePNeg año 100) && not (esMultiploDePNeg año 400) = False
              | otherwise = True

--Ej7

distanciaManhattan :: (Float,Float,Float) -> (Float,Float,Float) -> Float
distanciaManhattan (a,b,c) (x,y,z) = abs(l) + abs (m) + abs (n)
                                    where (l,m,n) = (a-x,b-y,c-z) 

--Ej 8 

sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = mod (abs x) 10

--comparar :: Int -> Int -> Int