
## pyMCFSimplex

pyMCFSimplex is a Python-Wrapper for the C/C++ MCFSimplex Solver Class from 
the University of Pisa.
MCFSimplex is a Class that solves large Minimum Cost Flow Problems
very fast.
See also [1] for a comparison.

pyMCFSimplex was being made through SWIG. Don't ask for the time spent on
figuring out how SWIG works. With more knowledge in C++ I would have been
faster - but I'm not a C++ guy! I want it in Python!

The authors of MCFSimplex are Alessandro Bertolini and Antonio Frangioni from
the Operations Research Group at the Dipartimento di Informatica of the 
University of Pisa [2].

pyMCFSimplex was originally created Johannes from the G#.Blog 

	http://www.sommer-forst.de/blog. 

It was updated for Python 3 by Arjan van den Boogaart

### Installation

`pip install pyMCFSimplex`

### Usage

Here is a first start. "sample.dmx" must be in the same location of your python script.
With these lines of code you can parse a minimum cost flow problem in DIMACS file format and solve it.

```from pyMCFSimplex import *

mcf = MCFSimplex()
f = open('sample.dmx','r')
inputStr = f.read()
f.close()
mcf.LoadDMX(inputStr)

mcf.SetMCFTime()
mcf.SolveMCF()
if mcf.MCFGetStatus() == 0:
    print("Optimal solution: %s" %mcf.MCFGetFO())
    print("Time elapsed: %s sec " %(mcf.TimeMCF()))
else:
    print("Problem unfeasible!")
    print("Time elapsed: %s sec " %(mcf.TimeMCF()))
```

If you want to load a network not from a DIMACS file, you'll have to call LoadNet() while passing C-arrays to the method.
C arrays in Python? Yes - don't worry. There are helper methods in pyMCFSimplex, that'll do this for you.
Look at the following piece of code.

```mcf = MCFSimplex()

'''
Problem data of a MCFP in DIMACS notation

c Problem line (nodes, links)
p min 4 5
c
c Node descriptor lines (supply+ or demand-)
n 1 4
n 4 -4
c
c Arc descriptor lines (from, to, minflow, maxflow, cost)
a 1 2 0 4 2
a 1 3 0 2 2
a 2 3 0 2 1
a 2 4 0 3 3
a 3 4 0 5 1
'''

# MCFP problem transformed to integers and lists
nmx     = 4 # max number of nodes
mmx     = 5 # max number of arcs
pn      = 4 # current number of nodes
pm      = 5 # current number of arcs
pU      = [4,2,2,3,5] # column maxflow
pC      = [2,2,1,3,1] # column cost
pDfct   = [-4,0,0,4]  # node deficit (supply/demand)
pSn     = [1,1,2,2,3] # column from
pEn     = [2,3,3,4,4] # column to

# call LoadNet() with the return values of the helper methods
# e.g. CreateDoubleArrayFromList(pU) takes a python list and returns a pointer to a 
# corresponding C array, that is passed as an argument to the method LoadNet()
mcf.LoadNet(nmx, mmx, pn, pm, CreateDoubleArrayFromList(pU), CreateDoubleArrayFromList(pC),
            CreateDoubleArrayFromList(pDfct), CreateUIntArrayFromList(pSn),
            CreateUIntArrayFromList(pEn))

print("Setting time..")
mcf.SetMCFTime()
mcf.SolveMCF()
if mcf.MCFGetStatus() == 0:
    print("Optimal solution: %s" %mcf.MCFGetFO())
    print("Time elapsed: %s sec " %(mcf.TimeMCF()))
else:
    print("Problem unfeasible!")
    print("Time elapsed: %s sec " %(mcf.TimeMCF()))
```


Please check out the sample script gsharpblog_mcfsolve_test.py for more information.


### Good to know

The original source code of MCFClass.h was changed a little bit for SWIG compatibility.
All changes are marked by the following comment line "//Johannes Sommer".
This included:
- LoadDMX() accepts in pyMCFSimplex a string value (original: c iostream). The original LoadDMX method is omitted.
- as SWIG cannot deal with nested classes, I pulled the classes Inf, MCFState and MCFException out of the main class MCFClass.

Perhaps the above mentioned changes to the original source are not necessary, if you know SWIG very well.

[1] http://bolyai.cs.elte.hu/egres/tr/egres-13-04.ps
[2] http://www.di.unipi.it/optimize/Software/MCF.html#MCFSimplex
