'''
 A firm has 3 factories - A, E, and K. There are four major warehouses situated at B, C, D, and M. Average daily product at A, E, K is 30, 40, and 50 units respectively. The average daily requirement of this product at B, C, D, and M is 35, 28, 32, 25 units respectively. The transportation cost (in Rs.) per unit of product from each factory to each warehouse is given below:
Warehouse
Factory 	B 	C 	D 	M 	Supply
A 	        6 	8 	8 	5 	30
E 	        5 	11 	9 	7 	40
K 	        8 	9 	7 	13 	50
Demand 	    35 	28 	32 	25 	 

The problem is to determine a routing plan that minimizes total transportation costs.

'''
####### Importing Packages
from pulp import * # LP programming package


############# Formulating the LP problem

######## Creating a Problem
prob = LpProblem("Transporting Problem 1",LpMinimize) #Since we wish to minimize transportation costs


####### Given Inputs

### Costs of transportation (in INR)
Cab = 6
Cac = 8
Cad = 8
Cam = 5
Ceb = 5
Cec = 11
Ced = 9
Cem = 7
Ckb = 8
Ckc = 9
Ckd = 7
Ckm = 13

### Demand Constraints (in number of units)
Db = 35
Dc = 28
Dd = 7
Dm = 13

### Supply constraints (in number of units)
Sa = 30
Se = 40
Sk = 50


######## Decision Variables and Optimization Function

### Decision Variables
#### Notation Legend Xij: where i is the factory and j is the warehouse


Xab = LpVariable("A to B", 0, None, LpInteger)
Xac = LpVariable("A to C", 0, None, LpInteger)
Xad = LpVariable("A to D", 0, None, LpInteger)
Xam = LpVariable("A to M", 0, None, LpInteger)
Xeb = LpVariable("E to B", 0, None, LpInteger)
Xec = LpVariable("E to C", 0, None, LpInteger)
Xed = LpVariable("E to D", 0, None, LpInteger)
Xem = LpVariable("E to M", 0, None, LpInteger)
Xkb = LpVariable("K to B", 0, None, LpInteger)
Xkc = LpVariable("K to C", 0, None, LpInteger)
Xkd = LpVariable("K to D", 0, None, LpInteger)
Xkm = LpVariable("K to M", 0, None, LpInteger)

### Optimization Function
#### Minimizing Costs by multiplying unit cost and units shipped

prob += Xab*Cab + Xac*Cac + Xad*Cad + Xam*Cam + Xeb*Ceb + Xec*Cec + Xed*Ced + Xem*Cem + Xkb*Ckb + Xkc*Ckc + Xkd*Ckd + Xkm*Ckm , "Total Cost of Transportation" 

####### Constraints

########### Supply Constraints
prob += Xab + Xac + Xad + Xam <= 30
prob += Xeb + Xec + Xed + Xem <= 40
prob += Xkb + Xkc + Xkd + Xkm <= 50

########### Demand Constraints
prob += Xab + Xeb + Xkb >= 35
prob += Xac + Xec + Xkc >= 28
prob += Xad + Xed + Xkd >= 7
prob += Xam + Xem + Xkm >= 13


####### Solving the problem

prob.writeLP("TransportationModel.lp")
prob.solve()


############ Print Status and Solutions

####### Status
print("Status:", LpStatus[prob.status])

####### Decision Variables

for v in prob.variables():
    print(v.name, "=", v.varValue)

####### Optimized function
print("Total cost of transportation = ", value(prob.objective))

