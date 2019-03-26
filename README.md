# Python_BinList
Python code for representing a number as a list of 1 and 0s. Bidirectional translation between numerical values and lists.

Also, will calculate Hamming distance between two lists of same length.

# Example:
```
# Number to fixed length list with padding
bl=BinList()
bl.explode(45,16)
print(bl.binlist)

# Number to list with smallest possible length 
bl.explode(45)
print(bl.binlist)

# Imploding a list to a number
al=BinList()
al.implode([1,1,0,0,0,1])
print(al.number)

# Imploding list with some extra padding
al.implode([0,0,0,0,0,1,1,0,0,0,1])
print(al.number)

# Hamming distance between two lists
x=BinList()
y=BinList()
x.implode([1,1,0,0,0,1])
y.implode([1,0,1,1,0,1])
print(x.hammingdistance(y))

# Hamming distance between a list and a number
y.explode(21,6)
print(x.binlist)
print(y.binlist)	
print(x.hammingdistance(y))
```

Output:
```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]
[1, 0, 1, 1, 0, 1]
49
49
3
[1, 1, 0, 0, 0, 1]
[0, 1, 0, 1, 0, 1]
2
```
