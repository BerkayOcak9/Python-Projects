import numpy as np
import matplotlib.pyplot as plt
import sys
import copy
import time
def greedy_alg(f):
    g = copy.deepcopy(f)
    count = 0
    tot_sum_l = []
    while count < f.shape[0]:
        last_index1 = count
        path_l = [count]
        tot_sum = 0
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
        f = copy.deepcopy(g)
        first_index = path_l[0]
        last_index = path_l[g.shape[1] - 1]
        tot_sum = g[last_index, first_index] + tot_sum
        path_l.append(path_l[0])
        tot_sum_l.append(tot_sum)
        if count == 0:
            last_path = path_l
            m_sum = tot_sum_l[count]
        if count > 0 and m_sum > tot_sum_l[count]:
            last_path = path_l
            m_sum = tot_sum_l[count]
        count += 1
        min_path = min(tot_sum_l)
    return last_path, min_path


def vis_sol(path, cord_x, cord_y):
    con_dot_x = []
    con_dot_y = []
    for b in path:
        con_dot_x.append(cord_x[b])
        con_dot_y.append(cord_y[b])
    plt.scatter(cord_x, cord_y)
    plt.scatter(con_dot_x[0], con_dot_y[0], c='red')
    plt.plot(con_dot_x, con_dot_y)
    plt.pause(0.5)
def vis_dyn(path, cord_x, cord_y):
    con_dot_x = []
    con_dot_y = []
    for b in path:
        con_dot_x.append(cord_x[b])
        con_dot_y.append(cord_y[b])
    return con_dot_x, con_dot_y


def distance_calc(route, dis_mat):
    sum = 0
    j = 0
    s = 0
    for i in route:
        if j != 0 and j != len(route):
            sum += dis_mat[s, i]
        s = i
        j += 1

    return sum


def two_opt(in_route, g, x_cord, y_cord):
    best_route = in_route
    t_f = True
    plt.show()
    axes = plt.gca()
    a, b = vis_dyn(best_route, x_cord, y_cord)
    tr_2, = axes.plot(a, b)
    plt.scatter(x_cord, y_cord)
    plt.scatter(a[0], b[0], c='red')
    while t_f:
        t_f = False
        for i in range(1, len(in_route) - 2):
            for j in range(i+1, len(in_route)):
                opt2_route = copy.deepcopy(in_route)
                opt2_route[i:j] = in_route[j - 1:i - 1:-1]
                if distance_calc(opt2_route, g) < distance_calc(best_route, g):
                    best_route = opt2_route
                    t_f = True
                    c,d = vis_dyn(best_route,x_cord,y_cord)
                    tr_2.set_xdata(c)
                    tr_2.set_ydata(d),
                    plt.draw()
                    plt.pause(1e-17)
                    time.sleep(0.5)
        in_route = best_route
    plt.show()
    print("Route distance:", distance_calc(best_route, g), "Route:", best_route)


dist_matrix = np.loadtxt("wg59_dist.txt")
z = copy.deepcopy(dist_matrix)
x_cord = []
y_cord = []
with open('wg59_xy.txt') as g:
    for line in g:
        x, y = line.split()
        x_cord.append(float(x))
        y_cord.append(float(y))
route1, sum_path = greedy_alg(dist_matrix)
two_opt(route1, z, x_cord, y_cord)


