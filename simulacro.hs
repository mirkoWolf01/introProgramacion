relacionesValidas :: [(String, String)] -> Bool
relacionesValidas []        = True 
relacionesValidas (x:xs)    | (fst x) == (snd x) || (pertenece x xs)  = False     
                            | otherwise                               = True && relacionesValidas xs

pertenece :: (Eq a) => (a,a) -> [(a,a)] -> Bool
pertenece a []      = False
pertenece a (x:xs)  | a == x || (snd a, fst a) == x = True
                    | otherwise                     = pertenece a xs

personas :: [(String, String)] -> [String]
personas xs = (personasAux xs [])

personasAux ::  [(String, String)]-> [String] -> [String]
personasAux [] ls       = ls
personasAux (x:xs) ls   | not (primero `perteneceElemento` ls) && not (segundo `perteneceElemento` ls)  =  personasAux xs (ls ++ [primero] ++ [segundo])
                        | not (primero `perteneceElemento` ls)                                          =  personasAux xs (ls ++ [primero])
                        | not (segundo `perteneceElemento` ls)                                          =  personasAux xs (ls ++ [segundo])
                        | otherwise                                                                     =  personasAux xs (ls)
                            where primero = fst x  
                                  segundo = snd x

perteneceElemento :: (Eq a) => a -> [a] -> Bool
perteneceElemento a []      = False
perteneceElemento a (x:xs)  | a == x                        = True
                            | otherwise                     = perteneceElemento a xs

amigoDe :: String -> [(String, String)] -> [String] 
amigoDe persona ls = (amigoDeAux persona ls [])


amigoDeAux :: (Eq a) => a -> [(a,a)] -> [a]-> [a]
amigoDeAux persona [] lsAmigos      = lsAmigos
amigoDeAux persona (x:xs) lsAmigos  | persona == primElem           = amigoDeAux persona xs (lsAmigos ++ [segunElem])
                                    | persona == segunElem          = amigoDeAux persona xs (lsAmigos ++ [primElem])
                                    | otherwise                     = amigoDeAux persona xs lsAmigos
                                        where   primElem    = fst x 
                                                segunElem   = snd x

longitud :: [a] -> Int
longitud []     = 0
longitud (x:ls) = 1 + longitud ls

personaConMasAmigos :: [(String, String)] -> String 
personaConMasAmigos xs  = (personaConMasAmigosAux xs "Nadie" xs)

personaConMasAmigosAux :: [(String, String)] -> String -> [(String, String)] -> String 
personaConMasAmigosAux [] persona lsEntera      = persona
personaConMasAmigosAux (x:xs) "Nadie" lsEntera  = personaConMasAmigosAux (x:xs) (fst x) lsEntera
personaConMasAmigosAux (x:xs) masAmig lsEntera  | longitud (amigoDe primElem lsEntera) > longitud (amigoDe masAmig lsEntera) && longitud (amigoDe primElem lsEntera) > longitud (amigoDe segunElem lsEntera)    = personaConMasAmigosAux (xs) primElem lsEntera
                                                | longitud (amigoDe segunElem lsEntera) > longitud (amigoDe masAmig lsEntera) && longitud (amigoDe segunElem lsEntera) > longitud (amigoDe primElem lsEntera)   = personaConMasAmigosAux (xs) segunElem lsEntera
                                                | otherwise                                                                                                                                                     = personaConMasAmigosAux xs masAmig lsEntera
                                                    where   primElem    = fst x 
                                                            segunElem   = snd x
