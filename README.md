# Python_BinList
Python code for representing a number as a list of 1 and 0s. Bidirectional translation between numerical values and lists.

Also, will calculate Hamming distance between two lists of same length.

Functionality to convert a unipolar (0|1) representation to bipolar(-1|1) and vice versa. Useful for Bidirectional Associative Memory. (BAM)

# Changes:
Added some functions useful in Machine Learning:

- norm() - return count of 1s in list
- complement() - returns a list with 1 in place of 0 and 0 in place of 1
- difference() - compares two BinList objects and returns a list with 1 in the positions where the lists are different and 0 where they are the same. I.e. effectively an XOR of the lists.

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
Example bipolar:
```
    # Test bipolar conversion
    x.bipolar()
    print(x.binlist)
    # Test unipolar conversion
    x.unipolar()
    print(x.binlist)
    x.implode(y.binlist)
    print(x.number)
```
Output bipolar:
```
        [1, 1, -1, -1, -1, 1]
        [1, 1, 0, 0, 0, 1]
        21
```
