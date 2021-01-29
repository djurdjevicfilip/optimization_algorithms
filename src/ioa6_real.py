from scipy.optimize import linprog
import numpy as np


func = np.array([310, 380, 350, 285,310, 380, 350, 285,310, 380, 350, 285 ])
# Because we maximize the function
func*=(-1)

# left hand side
lhs_ineq = [[1,1,1,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,1,1,1,1],
            [480,650,580,390,0,0,0,0,0,0,0,0],
            [0,0,0,0,480,650,580,390,0,0,0,0],
            [0,0,0,0,0,0,0,0,480,650,580,390],
            [1,0,0,0,1,0,0,0,1,0,0,0],
            [0,1,0,0,0,1,0,0,0,1,0,0],
            [0,0,1,0,0,0,1,0,0,0,1,0],
            [0,0,0,1,0,0,0,1,0,0,0,1]]
# right hand side
rhs_ineq = [10,16,8,6800,8700,4300,18,15,23,12]

# bounds
bnd = [(0, 18),(0, 18),(0, 18),
       (0, 15),(0, 15),(0, 15),
       (0, 23),(0, 23),(0, 23),
       (0, 12),(0, 12),(0, 12)]

opt = linprog(c=func, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,method="simplex")

print(opt)

solution = np.array([0,10,0,0,0,5,6,4,0,0,6,1])

def check(arr):
    if(arr[0]+arr[1]+arr[2]+arr[3]>10):
        return False
    if(arr[4]+arr[5]+arr[6]+arr[7]>16):
        return False
    if(arr[8]+arr[9]+arr[10]+arr[11]>8):
        return False


    if(480*arr[0]+650*arr[1]+580*arr[2]+390*arr[3]>6800):
        return False
    if(480*arr[4]+650*arr[5]+580*arr[6]+390*arr[7]>8700):
        return False
    if(480*arr[8]+650*arr[9]+580*arr[10]+390*arr[11]>4300):
        return False

    if(arr[0]+arr[4]+arr[8]>18):
        return False
    if(arr[1]+arr[5]+arr[9]>15):
        return False
    if(arr[2]+arr[6]+arr[10]>23):
        return False
    if(arr[3]+arr[7]+arr[11]>12):
        return False

    return True
max=0
final_solution = []
for i in range(3, 10):
    for j in range(1, 8):
        for k in range(3, 10):
            for l in range(0, 5):
                solution[6]=i
                solution[7]=j
                solution[10]=k
                solution[11]=l
                if(check(solution)):
                    sum = np.sum(func*solution)
                    if(abs(sum)>max):
                        max=abs(sum)
                        final_solution = solution.copy()
