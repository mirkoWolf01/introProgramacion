-- Para Numeros en general
esPar :: Int -> Bool
esPar 0 = True
esPar n = not (esPar (n-1))

parteEntera :: Float -> Int
parteEntera n   | (abs n) < 1   =   0
                |  n < 0        = (-1) + parteEntera(n+1)
                | otherwise     =   1  + parteEntera(n-1)

esDivisible :: Int -> Int -> Bool
esDivisible a b | (mod a b) == 0    = True
                | otherwise         = False

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



