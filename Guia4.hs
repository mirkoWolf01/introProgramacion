esOrigen :: (Float , Float ) -> Bool
esOrigen (0, 0) = True
esOrigen (x, y) = False

angulo0 :: (Float , Float ) -> Bool
angulo0 (_, 0) = True
angulo0 (_, _) = False

angulo45 :: (Float , Float ) -> Bool
angulo45 (x, y) = x == y

-- recursion

factorial :: Int -> Int
factorial n     | n == 0 = 1
                | n > 0 = n * factorial (n-1)

esPar :: Int -> Bool
esPar 0 = True
esPar n = not (esPar (n-1))

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
parteEntera n   | (abs n) < 1   = 0
                |  n < 0         = - 1 + parteEntera(n+1)
                | otherwise     = 1 + parteEntera(n-1)


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
                | otherwise     = (ultimoDigito * (10^((cantDigitos n) -1))) + invertirNum (div n 10)
                   where ultimoDigito = mod n 10

--Ej10