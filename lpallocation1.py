from pulp import *

'''
###Question

A company makes two products (X and Y) using two machines (A and B). Each unit of X that is produced requires 50 minutes processing time on machine A and 30 minutes processing time on machine B. Each unit of Y that is produced requires 24 minutes processing time on machine A and 33 minutes processing time on machine B.

At the start of the current week there are 30 units of X and 90 units of Y in stock. Available processing time on machine A is forecast to be 40 hours and on machine B is forecast to be 35 hours.

The demand for X in the current week is forecast to be 75 units and for Y is forecast to be 95 units. Company policy is to maximise the combined sum of the units of X and the units of Y in stock at the end of the week.

    Formulate the problem of deciding how much of each product to make in the current week as a linear program.
'''


####### Creating a problem which is a maximization function


prob = LpProblem("Allocation Problem", LpMaximize) #Since it is a maximization problem
Xprod = LpVariable("X produced", 45, None,LpInteger) #Defining the variable Xprod which has a lower limit of 45 and no upper limit. Integer type
Yprod = LpVariable("Y produced", 6, None,LpInteger) #Defining the variable Yprod which has a lower limit of 6 and no upper limit. Integer type

####### Adding the given data

#The starting stock
Xstart = 30
Ystart = 90

#The demand
Xdemand = 75
Ydemand = 95

#Time (Syntax: PRODUCTmachine)
Xa = 30
Xb = 30
Ya = 24 
Yb = 33

#Available Time
Atot = 2400
Btot = 2100

### Derived Variables
### Calculating the requirement for the week
Xreq = Xdemand - Xstart
Yreq = Ydemand - Ystart


####### Adding the objective function to the 'prob' variable. Note that the comma after the expression is important to give a brief description of the expression

prob += Xprod + Xstart - Xdemand + Yprod + Ystart - Ydemand , "Total Number of products for sale"

####### Adding the constraints

prob += Xprod * Xa + Yprod * Ya <= Atot #Total Time constraint on A
prob += Xprod * Xb + Yprod * Yb <= Btot #Total Time constraint on B

prob += Xprod >= Xreq #X produced is above requirement
prob += Yprod >= Yreq #Y produced is above requirement

######## Saving the problem data onto an .lp file and then saving it

prob.writeLP("AllocationModel.lp")
prob.solve()

######## Printing the status on the screen

print("Status:", LpStatus[prob.status])



######## Printing the value of the decision variables and optimization function


### Decision Variables
for v in prob.variables():
    print(v.name, "=", v.varValue)

### Optimization Function
print("Total number of products produced within the constraints = ", value(prob.objective))
