#!/usr/bin/python

import numpy;


class square :
    def __init__(self, x) :
        self.possibles = numpy.ones(x)
        self.value = 0; 

    def getvalue(self):
        return self.value;

    def setvalue(self, value):
        self.value = value;

    def string(self):
        return "hej"
        

class soduku :
    size = 0;
    squares=[]
    def __init__(self, x) :
        self.size=x;
        sqrt = numpy.floor(x/3)

        if sqrt*sqrt != x :
            print "error the size of the board must be divisble by 3!"
            return ; 

        
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.squares.append(square(x))

    def solve(self):
        return 0

    # fixme we must know the width
    def get_group(self, n) :
        line = (n/self.size)
        column = (n%self.size);
        x = line / 3;
        y = column / 3; 
#        print ("n ", n, " line ", line , " column ", column, " x ", x, "y", y);
        group = [];

        for i in range(0, 3) :                         
            group.append(3*(x)+3*y+9*i)
            group.append(3*(x)+3*y+9*i+1)
            group.append(3*(x)+3*y+9*i+2)
#        print group
        return group

#this is a very very basic validator, it only validates lines and columns, not groups
    def validate(self, n) :
        line = (n/self.size)
        column = (n%self.size);         
        group = 0; 
#        print ("n ", n, " line ", line , " column ", column);

        for i in self.get_group(n):
            if(i == n):
                continue
            if(self.squares[i].getvalue() == self.squares[n].getvalue()):
 #               print("FAIL\n", self.squares[i].getvalue(), self.squares[n].getvalue())
                return -1


  #      print ("LINE TEST")
        #Now test the line
        for i in range(0, self.size) :
            z = line*9 + i; 
            if(n == z) :
                continue
            if(self.squares[z].getvalue() == self.squares[n].getvalue()):
                return -1
            
        #Now test the column
        for i in range(0, self.size) :
            z = column + i*9; 
            if(n == z) :
                continue
            if(self.squares[z].getvalue() == self.squares[n].getvalue()):
                return -1
            
        return 0

    def setsquarevalue(self, n, val):
        oldval = self.squares[n].getvalue()
        self.squares[n].setvalue(val)

        if(self.validate(n) != 0):
            self.squares[n].setvalue(oldval)
            return 0
        return 1

    def randomize(self, n): 
        #random_integers is inclusive and we start from 0 so -1. 
        squares = numpy.random.random_integers(0, self.size*self.size-1, n);
        values = numpy.random.random_integers(1, self.size, n);

        for i in range(0, n):
            val = values[i]; 
            
            while(self.setsquarevalue(squares[i], val) == 0) :
                val = numpy.random.random_integers(1, self.size, 1);
                val = val[0]
#                print ("Damn try another value ", val)
            #print squares[i]
            #print values[i]

    def printme(self):
        for i in range(0, self.size):
            line = []
            for j in range(0, self.size):
                line.append(self.squares[i*self.size+j].getvalue())
            print(line)

    def reduce(self):
        for i in range(self.size*self.size-1):
            reduce_square(n)

    def is_in_group(self, g, x) :
        for i in(self.get_group(g)):
            if(self.squares[i].getvalue() == x):
                return 1;
        return 0

    def is_in_line(self, l, x) : 
        for i in range(0, 9):
            if(self.squares[9*l+i].getvalue() == x):
                return 1
        return 0;
    def is_in_column(self, c, x) :
        for i in range(0, 9):
            if(self.squares[9*i+c].getvalue() == x):
                return 1
        return 0;

    def reduce_square(self, n) : 
        line = (n/self.size)
        column = (n%self.size);         
        
        for i in self.get_group(n):
            if(i == n):
                continue
            if(self.squares[i].getvalue() == self.squares[n].getvalue()):
 #               print("FAIL\n", self.squares[i].getvalue(), self.squares[n].getvalue())
                return -1


  #      print ("LINE TEST")
        #Now test the line
        for i in range(0, self.size) :
            z = line*9 + i; 
            if(n == z) :
                continue
            if(self.squares[z].getvalue() == self.squares[n].getvalue()):
                return -1
            
        #Now test the column
        for i in range(0, self.size) :
            z = column + i*9; 
            if(n == z) :
                continue
            if(self.squares[z].getvalue() == self.squares[n].getvalue()):
                return -1


        
s=soduku(9)
s.randomize(30)
#s.solve(); 
s.reduce()
s.reduce()
s.printme()
print s

print 
