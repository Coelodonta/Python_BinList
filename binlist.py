#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  binlist.py
#  
#  Copyright 2019 Coelodonta
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class BinList():
    def explode(self,number,fixedLength=0):
        self.number=number
        tobin = lambda n: n>0 and [n&1]+tobin(n>>1) or []
        self.binlist=tobin(number)
        self.binlist.reverse()
        if len(self.binlist)<fixedLength:
            for i in range(fixedLength-len(self.binlist)):
                self.binlist.insert(0,0)
        self.isbipolar=False
        return self.binlist
		
    def implode(self,binlist):
        self.binlist=binlist
        self.number = int("".join(str(x) for x in binlist), 2)
        self.isbipolar=False
        return self.number

    def hammingdistance(self,other):
        if len(self.binlist) != len(other.binlist):
            return None
        if self.isbipolar:
            self.uniploar()
        return sum(s != o for s, o in zip(self.binlist, other.binlist))
    
    def bipolar(self):
        if not self.isbipolar:
            bp=lambda x: -1 if (x<1) else 1
            self.binlist=[bp(x) for x in self.binlist]
            self.isbipolar=True
        
    def unipolar(self):
        if self.bipolar:
            up=lambda x: 0 if (x<1) else 1
            self.binlist=[up(x) for x in self.binlist]
            self.isbipolar=False
        

if __name__ == '__main__':
    """
	Test code. The expected output is:
	
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]
        [1, 0, 1, 1, 0, 1]
        49
        49
        3
        [1, 1, 0, 0, 0, 1]
        [0, 1, 0, 1, 0, 1]
        2
        [1, 1, -1, -1, -1, 1]
        [1, 1, 0, 0, 0, 1]
        21
	
    """
	
    # Test fixed length list with padding
    bl=BinList()
    bl.explode(45,16)
    print(bl.binlist)
    # Test with smallest possible length 
    bl.explode(45)
    print(bl.binlist)
    # Test imploding a list to a number
    al=BinList()
    al.implode([1,1,0,0,0,1])
    print(al.number)
    # Test with some extra padding
    al.implode([0,0,0,0,0,1,1,0,0,0,1])
    print(al.number)
    # Test Hamming distance between two lists
    x=BinList()
    y=BinList()
    x.implode([1,1,0,0,0,1])
    y.implode([1,0,1,1,0,1])
    print(x.hammingdistance(y))
    # Test Hamming distance between a list and a number
    y.explode(21,6)
    print(x.binlist)
    print(y.binlist)	
    print(x.hammingdistance(y))
    # Test bipolar conversion
    x.bipolar()
    print(x.binlist)
    # Test unipolar conversion
    x.unipolar()
    print(x.binlist)
    x.implode(y.binlist)
    print(x.number)
