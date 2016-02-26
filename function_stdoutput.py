#!usr/bin/env python

def  FuncOut(k, j):
    print "Hi!my name is ",k +"and my age is",j
    print "\nHi!my name is {}  and my age is {}".format(k,j)
    print "\nHi! my name is %s  and my age is %s"%(k,j)

FuncOut("Mary",19)
