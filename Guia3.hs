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