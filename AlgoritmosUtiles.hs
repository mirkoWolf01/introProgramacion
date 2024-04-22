module AlgoritmosUtiles 
( esPar
, parteEntera
, esDivisible
, invertirNum
, menorDivisor
, esPrimo
, ultimoDigito
, ultimoDigito
, anteultimoDigito
, iesimoDigito
, cantDigitos
, algunDigitoPar
) where

-- Para Numeros en general
esPar :: Int -> Bool
esPar 0 = True
esPar n = not (esPar (n-1))

parteEntera :: Float -> Int   --Np funca para un numero de mas de 16 digitos
parteEntera n   = floor n 

esDivisible :: Int -> Int -> Bool
esDivisible a b | (mod a b) == 0    = True
                | otherwise         = False

invertirNum :: Int -> Int
invertirNum n   | div n 10 == 0 = n
                | otherwise     = ((ultimoDigito n)* (10^((cantDigitos n)-1))) + invertirNum (div n 10)

menorDivisor :: Int ->  Int 
menorDivisor a  = (menorDivisorAux a 2)

menorDivisorAux :: Int -> Int -> Int
menorDivisorAux a b | b > a                     = 0
                    | not (a `esDivisible` b)   = menorDivisorAux a (b+1)
                    | otherwise                 = b

esPrimo :: Int -> Bool
esPrimo a = (menorDivisor a) == a

-- Para Digitos 
ultimoDigito :: Int -> Int 
ultimoDigito n  = mod n 10 

anteultimoDigito :: Int -> Int
anteultimoDigito n   = ultimoDigito (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito a b    | not (a > 0) || not (1 <= b)|| not (b <= cantDigitos a) = 0
                    | otherwise =  mod (div a (10^((cantDigitos a)-b))) 10

cantDigitos :: Int -> Int
cantDigitos a   | k == 0        = 1
                | otherwise     = 1 + cantDigitos (k)
                  where k = div a 10

algunDigitoPar :: Int -> Bool
algunDigitoPar a    | a == 0                                            = False
                    | (div a 10) == 0 && not(esPar(ultimoDigito a))     = False
                    | otherwise                                         = ((esPar (ultimoDigito a)) && (ultimoDigito a /= 0)) || (algunDigitoPar (div a 10))  
