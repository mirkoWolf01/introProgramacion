esPar :: Int -> Bool
esPar 0 = True
esPar n = not (esPar (n-1))

ultimoDigito :: Int -> Int 
ultimoDigito n  = mod n 10 

anteultimoDigito :: Int -> Int
anteultimoDigito n   = ultimoDigito (div n 10)

algunDigitoPar :: Int -> Bool
algunDigitoPar a    | a == 0                                            = False
                    | (div a 10) == 0 && not(esPar(ultimoDigito a))     = False
                    | otherwise                                         = ((esPar (ultimoDigito a)) && (ultimoDigito a /= 0)) || (algunDigitoPar (div a 10))  
-- recursion
factorial :: Int -> Int
factorial n     | n == 0 = 1
                | n > 0 = n * factorial (n-1)

llegarA :: Int -> Int -> Int
llegarA numEntrada vecesSumado   | numEntrada <= 0 = vecesSumado
                                 | otherwise       = llegarA (numEntrada-1) (vecesSumado-1)

--Ej1
fib :: Int -> Int 
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

--Ej2
parteEntera :: Float -> Int
parteEntera n   | (abs n) < 1   =   0
                |  n < 0        = (-1) + parteEntera(n+1)
                | otherwise     =   1  + parteEntera(n-1)


--Ej3
esDivisible :: Int -> Int -> Bool
esDivisible a b | a == b             = True
                | a < b              = False
                | otherwise  = True && (esDivisible(a-b) b)

--Ej4 
sumaImpares :: Int -> Int 
sumaImpares a   | a == 1 = 1 
                | otherwise = (2*a-1) + sumaImpares(a-1)

--Ej5
medioFact :: Int -> Int
medioFact n | n <= 0 = 1
            | otherwise = n * medioFact(n-2)

--Ej6 
sumaDigitos :: Int -> Int
sumaDigitos n   | n < 1 = 0 
                | (div n 10) == 0   = n
                | otherwise = (mod n 10) + sumaDigitos (div n 10)
                    
--Ej7
todosDigitosIguales :: Int -> Bool
todosDigitosIguales n   |   n < 1           = False
                        | (mod n 10) == n   = True
                        | otherwise = ((mod n 10) == (mod (div n 10) 10)) && todosDigitosIguales (div n 10)

--Ej8 
iesimoDigito :: Int -> Int -> Int
iesimoDigito a b    | not (a > 0) || not (1 <= b)|| not (b <= cantDigitos a) = 0
                    | otherwise =  mod (div a (10^((cantDigitos a)-b))) 10

cantDigitos :: Int -> Int
cantDigitos a   | k == 0        = 1
                | otherwise     = 1 + cantDigitos (k)
                  where k = div a 10

--Ej9
esCapicua :: Int -> Bool
esCapicua n | div n 10 == 0 = True
            | otherwise = (n == (invertirNum n))

invertirNum :: Int -> Int
invertirNum n   | div n 10 == 0 = n
                | otherwise     = ((ultimoDigito n)* (10^((cantDigitos n)-1))) + invertirNum (div n 10)

--Ej10
f1 :: Int -> Int
f1 n  | n < 0     = 0
      | otherwise = 2^n + f1(n-1)

f2 :: Int -> Float -> Float
f2 n q  | n < 1     = 0
        | otherwise = q^n + f2(n-1) q

f3 :: Int -> Float -> Float
f3 n q  | n < 1  = 0
        | otherwise = q^(2*n) + q^(2*n -1) + f3(n-1) q

f4 :: Int -> Float -> Float
f4 n q  | n < 1  = 0
        | otherwise = (f3 n q) - (f2 (n-1) q)

--Ej11
eAprox :: Int -> Float
eAprox n    | n == 0    = 1
            | otherwise = ((1)/(fromIntegral (factorial n))) + eAprox (n-1)

--Ej12

raizDe2Aprox :: Int -> Float 
raizDe2Aprox a  | a == 1 = 1
                | otherwise = 1 + 1/(1+raizDe2Aprox (a-1)) 

--Ej13
sumatoriaDeLaSumatoria :: Float -> Float -> Float
sumatoriaDeLaSumatoria n m  | n == 1    = sumatoria 1 m
                            | otherwise = sumatoria n m + sumatoriaDeLaSumatoria (n-1) m

sumatoria :: Float -> Float -> Float      -- n^m
sumatoria n m   | m < 1     = 0
                | otherwise = n**m + sumatoria n (m-1)

--Ej14
sumaPotencias :: Int -> Int -> Int -> Int
sumaPotencias q n m | m == 1          = sumaPotAux q n 1
                    | otherwise       = (sumaPotAux q n m) + sumaPotencias q n (m-1)

sumaPotAux :: Int -> Int -> Int -> Int
sumaPotAux q n m    | n == 1    = q^(1+m) 
                    | otherwise = q^(n+m) + sumaPotAux q (n-1) m

--Ej 15
sumaRacionales :: Int -> Int -> Float
sumaRacionales n m  | n == 1    = (auxSumaRacionales 1 mFloat)
                    | otherwise = (auxSumaRacionales nFloat mFloat) + (sumaRacionales (n-1) m)
                        where nFloat = (fromIntegral n)
                              mFloat = (fromIntegral m)

auxSumaRacionales :: Float -> Float -> Float
auxSumaRacionales n m   | m == 1         =  n
                        | otherwise      = (n/m) + (auxSumaRacionales n (m-1))

--Ej16
menorDivisor :: Int ->  Int 
menorDivisor a  = (menorDivisorAux a 2)

menorDivisorAux :: Int -> Int -> Int
menorDivisorAux a b | b > a                     = 0
                    | not (a `esDivisible` b)   = menorDivisorAux a (b+1)
                    | otherwise                 = b

esPrimo :: Int -> Bool
esPrimo a = not ((menorDivisor a) == a)

sonCoprimos :: Int -> Int -> Bool
sonCoprimos a b =  not((a `esDivisible` (menorDivisor b)) || (b `esDivisible` (menorDivisor a)))

nEsPrimo :: Int -> Int
nEsPrimo a  = (nEsPrimoAux a 2)

nEsPrimoAux :: Int -> Int -> Int
nEsPrimoAux contador numPrimo   | contador == 0 = (numPrimo -1)
                                | (menorDivisor numPrimo) == numPrimo   = nEsPrimoAux (contador-1)(numPrimo+1)
                                | otherwise                             = nEsPrimoAux contador (numPrimo+1)

--Ej17
esFibonacci :: Int -> Bool
esFibonacci n   | n < 0         = False
                | otherwise     = (esFibonacciAux n 0)

esFibonacciAux :: Int -> Int -> Bool
esFibonacciAux a b  | a == fib b    = True
                    | a <  fib b    = False
                    | otherwise     = True && (esFibonacciAux a (b+1))

--Ej18
mayorDigitoPar :: Int -> Int
mayorDigitoPar a    | a == 0                    = 0
                    | not (algunDigitoPar a)    = -1
                    | otherwise                 = (mayorDigitoParAux a 0)

mayorDigitoParAux :: Int -> Int -> Int          
mayorDigitoParAux a b   |(esPar (ultimoDigito a)) && ((ultimoDigito a) > b) = mayorDigitoParAux (div a 10) (ultimoDigito a)
                        | not (algunDigitoPar (div a 10))                   = b 
                        | otherwise                                         = mayorDigitoParAux (div a 10) b

--Ej19
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n | n < 0     = False
                        | otherwise = (esSumaInicialDePrimosAux n 1 2)

esSumaInicialDePrimosAux :: Int -> Int -> Int -> Bool
esSumaInicialDePrimosAux n b numPrimo   | numPrimo > n  = False
                                        | numPrimo == n = True 
                                        | otherwise     = esSumaInicialDePrimosAux n (proximoEntero) (numPrimo + (nEsPrimo proximoEntero))
                                            where proximoEntero = b+1

--Ej21 
pitagoras :: Int ->Int ->Int ->Int
pitagoras m n r | m < 0 || n < 0 || r < 0   = 0
                | m == (-1)     = (pitagorasAuxContador 1 n r 0)
                | otherwise     = (pitagorasAuxContador m n r 0) + (pitagoras (m-1) n r)

pitagorasAuxContador :: Int ->Int ->Int ->Int -> Int 
pitagorasAuxContador m n r contador     | n == (-1)    = contador
                                        | (m^2 + n^2) <= r^2    = pitagorasAuxContador m (n-1) r (contador+1)
                                        | otherwise             = pitagorasAuxContador m (n-1) r (contador) 