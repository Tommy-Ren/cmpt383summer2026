-- mylist.hs

-- List a is a recursive data representing a list of values of type a
data List a = Nil | Cons a (List a)
    deriving (Eq, Show)

lst1 = Cons 5 (Cons 2 (Cons 6 Nil))
lst2 = Cons "cat" (Cons "dog" (Cons "bird" (Cons "cow" Nil)))

-- TODO 1: get the first element of a list


-- TODO 2: get the rest of a mylist


-- TODO 3: get the length of a mylist


-- TODO 4: convert a regular Haskell list to a mylist


-- TODO 5: convert a mylist to a regular Haskell list (using recursion)


-- TODO 6: fold right for a mylist


-- TODO 7: convert a mylist to a regular Haskell list (using fold right)
