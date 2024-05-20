{-
ghci abre el interprete 
    :l para compilar el codigo
    :r para volver a compilar
    :q para salir
-}
double :: Int -> Int --como se define una funcion
double n = 2 * n

signo :: Int -> Int
signo x | x > 0 = 1
        | x < 0 = -1
        | otherwise = 0

esNatural :: Int -> Bool
esNatural n | n >= 1 = True
            | n <  1 = False

matchea :: Int -> Int
matchea 0 = 0 
matchea 2 = -2
matchea 1 = 200
