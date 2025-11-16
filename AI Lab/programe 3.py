#Python script for building a puzzle solver.

words = ["cat", "dog", "tac", "god", "act", "bat","tab","atb"]
scramble = input("Enter scrambled word: ")
sol = [w for w in words if sorted(w) == sorted (scramble)]
print("possible words:", sol if sol else "no match")                 
