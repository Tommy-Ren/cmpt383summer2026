-- demo.hs

add x y = x + y

factorial n = product [1..n]

qsort []     = []
qsort (n:ns) = qsort smalls ++ [n] ++ qsort bigs
             where smalls = [a | a <- ns, a <= n]
                   bigs   = [b | b <- ns, b > n]

--mysum :: Num a => [a] -> a
mysum :: [Int] -> Int
mysum []     = 0
mysum (n:ns) = n + (mysum ns)
