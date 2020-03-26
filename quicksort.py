def sort1(list):
    """sorts ints, alphabetizes strings"""
    if len(list) in [0,1]:
        return list
    eq = [i for i in list if i == list[0]]
    smaller = [i for i in list if i<list[0]]
    larger = [i for i in list if i>list[0]]
    return sort1(smaller) + eq + sort1(larger)

def sort2(list):
    """sort list of strings by length"""
    if len(list) in [0,1]:
        return list
    eq = [i for i in list if len(i) == len(list[0])]
    smaller = [i for i in list if len(i)<len(list[0])]
    larger = [i for i in list if len(i)>len(list[0])]
    return sort2(smaller) + eq + sort2(larger)

if __name__ == "__main__":
    x = [1,3,2,9,-2,.32,0,2,4]
    y = ["z","","a b","b-","ab","a","hello","sdf"]
    print(f"x:        {x}")    
    print(f"x sorted: {sort1(x)}")
    
    print(f"y:                  {y}")    
    print(f"y sorted by length: {sort2(y)}")
    print(f"y sorted by length, alphabetical: {sort2(sort1(y))}")
