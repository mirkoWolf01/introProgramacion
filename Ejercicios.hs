-- Ej 1
funcion :: Int -> Int
funcion 1 = 8
funcion 4 = 131
funcion 16 = 16

funcionPorBarras :: Int -> Int
funcionPorBarras n  | n == 1  = 8
                    | n == 4  = 131
                    | n == 16 = 16

funcionInversa :: Int -> Int
funcionInversa m    | m == 131 = 1
                    | m == 16 = 4
                    | m == 8 = 16

funcionCompuestaH :: Int -> Int
funcionCompuestaH h = funcion(funcionInversa(h))

funcionCompuestaK :: Int -> Int
funcionCompuestaK k = funcionInversa(funcion(k))

-- Ej2

maximoEntre3 :: Int -> Int -> Int -> Int
maximoEntre3 x y z  | x >= y && x >= z = x
                    | y >= x && y >= z = y
                    | z >= x && z >= y = z

sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | x /= y && x /= z = x + y + z
                    | x == y && x /= z = x + z
                    | x /= y && x == z = x + y
                    | x == y && x == z = x

sumaDistintosHard :: Int -> Int -> Int -> Int
sumaDistintosHard x y z | x /= y && x /= z && y /= z = x + y + z
                        | x /= z = x + z
                        | x /= y = x + y
                        | otherwise = x

digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

digitoDecenas :: Int -> Int
digitoDecenas x  = div(mod x 100 - digitoUnidades x) 10

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (x,y) (a, b)  | x >= a          = False
                        | y >= b          = False
                        | otherwise      = True