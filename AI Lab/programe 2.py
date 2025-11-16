#Use logic programming in Python parse a family tree and infer the relationships between the family members.

relations = {
     "parent": [("John", "Anna"), ("Marry", "Anna"),
                ("John", "Bob"), ("Marry", "Bob"),
                ("Bob", "Carla")],
     "spouse": [("John", "Marry"), ("Anna", "Mike")]
 }

def parents_of(x): 
      return [p for p,c in relations["parent"] if c == x]

def children_of(x): 
      return [c for p,c in relations["parent"] if p == x]

def siblings_of(x):
     sibs = []
     for p in parents_of(x):
         sibs += [c for c in children_of(p) if c!= x]
     return sibs

name = input("Enter name: ")
print("Parents:", parents_of(name))
print("Children:", children_of(name))
print("Siblings:", siblings_of(name))
