import numpy as np
import matplotlib.pyplot as plt
import sys
import copy
def dist(f):
    g=copy.deepcopy(f)
    tot_sum = 0
    min_element = f[1, 2]
    for a in range(f.shape[0]):
        for l in range(f.shape[1]):
            if a != l and min_element > f[a, l]:
                min_element = f[a, l]
                last_index1 = a
    path_l = [36]
    last_index1 = 36
    for i in range(f.shape[0]):
        if last_index1 == f.shape[1] - 1:
            path_min = f[last_index1, last_index1 - 1]
        else:
            path_min = f[last_index1, last_index1 + 1]
        for j in range(f.shape[1]):
            if (last_index1 != j) and (path_min >= f[last_index1, j]):
                path_min = f[last_index1, j]
                last_min_index = j
        for k in range(f.shape[1]):
            f[k, last_index1] = sys.maxsize
        last_index1 = last_min_index
        if i != f.shape[1] - 1:
            path_l.append(last_index1)
        else:
            break
        tot_sum = tot_sum + path_min
    first_index = path_l[0]
    last_index = path_l[g.shape[1] - 1]
    tot_sum = g[last_index, first_index] + tot_sum
    path_l.append(path_l[0])
    return path_l,tot_sum
def vis_sol(path_l,x_cord,y_cord):
    con_dot_x = []
    con_dot_y = []
    for b in path_l:
        con_dot_x.append(x_cord[b])
        con_dot_y.append(y_cord[b])
    plt.scatter(x_cord, y_cord)
    plt.scatter(con_dot_x[0], con_dot_y[0], c='red')
    plt.plot(con_dot_x, con_dot_y)
    plt.show()


f = np.loadtxt("wg59_dist.txt")
x_cord = []
y_cord = []
with open('wg59_xy.txt') as g:
    for line in g:
        x, y = line.split()
        x_cord.append(float(x))
        y_cord.append(float(y))
path_l,sum_path=dist(f)
vis_sol(path_l, x_cord, y_cord)
print(path_l, "\n", sum_path)
