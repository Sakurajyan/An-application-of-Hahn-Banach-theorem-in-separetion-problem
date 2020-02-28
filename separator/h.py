from scipy.stats import multivariate_normal
import numpy as np
from scipy.spatial import ConvexHull
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
from data import *
from sklearn import svm, datasets
# marco
plot_flag = True
plt.rc('font', size=15)
# function


def hit(U, hull):
    eq = hull.equations.T
    V, b = eq[:-1], eq[-1]
    alpha = -b/np.dot(U, V)
    # print('alpha in hit',alpha)
    return np.min(alpha[alpha > 0])*U

def minkowski(U, hull):
    norm_U = np.sqrt(U[0]**2+U[1]**2)
    H = hit(U, hull)
    norm_H = np.sqrt(H[0]**2+H[1]**2)
    return norm_U/norm_H

def extension(x0, L0, hull):
    delta_list = []
    alpha_list = []
    beta_list = []
    max_alpha = -math.inf
    min_beta = math.inf
    # using orthogonal x1
    x1 = np.array([x0[1], -x0[0]])
    # using point in C
    # x1=C[-1]
    for i in range(-500, 500, 1):
        size = 100.0
        k = i/size
        # you should use all number in span{x0}, not x0, but since L0 is a constant, we can use L0 safety, but you need
        delta_list.append(k)
        alpha = -minkowski(-1*x1+k*x0, hull)+k*L0
        beta = minkowski(x1+k*x0, hull)-k*L0
        alpha_list.append(alpha)
        beta_list.append(beta)
        if max_alpha < alpha:
            max_alpha = alpha
        # change x0
        if min_beta > beta:
            min_beta = beta
    # print(i/size,'new',alpha, beta, beta-alpha)
    # this part is wrong, we need L1 in all interval (another inequality for all number in interval)
    # L1 = (beta-alpha)/2+alpha
    # note here the difference is the same in 2D case, we can make use of it
    L1 = (max_alpha+min_beta)/2
    print('alpha', max_alpha, 'beta', min_beta)
    return (x1, (max_alpha+min_beta)/2, alpha_list, beta_list, delta_list)

def extension_vertex_method(x0, L0, hull, C):
    delta_list = []
    alpha_list = []
    beta_list = []
    max_alpha = -math.inf
    min_beta = math.inf
    # using orthogonal x1
    x1 = np.array([x0[1], -x0[0]])
    # using point in C
    # x1=C[-1]
    k_list = []
    for vertex in hull.vertices:
        # k_list.append((C[vertex,0]*x0[0]+C[vertex,1]*x0[1])/np.linalg.norm(x0))
        k1=np.dot(C[vertex], x0)
        k2=np.dot(C[vertex], x1)
        k3=np.dot(C[vertex], -1*x1)
        k_list.append(k1*(np.linalg.norm(x1)**2)/(k2*np.linalg.norm(x0)))
        k_list.append(k1*(np.linalg.norm(x1)**2)/(k3*np.linalg.norm(x0)))
    # print(k_list)
    k_list = sorted(k_list)
    # add one more least and largest k
    k_list.append(k_list[-1]+1)
    k_list.append(k_list[0]-1)
    k_list = sorted(k_list)
    # k_list.reverse()
    for k in k_list:
        # you should use all number in span{x0}, not x0, but since L0 is a constant, we can use L0 safety, but you need
        delta_list.append(k)
        # print(i)
        alpha = -minkowski(-1*x1+k*x0, hull)+k*L0
        beta = minkowski(x1+k*x0, hull)-k*L0
        alpha_list.append(alpha)
        beta_list.append(beta)
        if max_alpha < alpha:
            max_alpha = alpha
        # change x0
        if min_beta > beta:
            min_beta = beta
    # print(i/size,'new',alpha, beta, beta-alpha)
    # this part is wrong, we need L1 in all interval (another inequality for all number in interval)
    # L1 = (beta-alpha)/2+alpha
    # note here the difference is the same in 2D case, we can make use of it
    L1 = (max_alpha+min_beta)/2
    # print('delta k list',delta_list)
    # print('alpha list',alpha_list)
    # print('beta list',beta_list)
    print('max alpha', max_alpha, '\nmin beta ', min_beta)
    return (x1, (max_alpha+min_beta)/2, alpha_list, beta_list, delta_list)

def compute_gamma(a, b, cofactor):
    alpha = -math.inf
    beta = math.inf
    graph_A = [[], []]
    graph_A[0] = [a[:, 0], a[:, 1]]
    graph_B = [[], []]
    graph_B[0] = [b[:, 0], b[:, 1]]
    # print('gamma of a should less than b\n','a',a[:,0],'\nb',b[:,0])
    for i in a:
        temp = np.dot(cofactor, i)[0, 0]
        # print('temp shape',np.dot(cofactor, i).shape)
        graph_A[1].append(temp)
        if alpha < temp:
            alpha = temp
    for i in b:
        temp = np.dot(cofactor, i)[0, 0]
        graph_B[1].append(temp)
        if beta > temp:
            beta = temp
    gamma = (alpha+beta)/2
    print('gamma:', alpha, beta)
    return (alpha, beta, gamma, graph_A, graph_B)

def seperator(data_set_A, data_set_B,chosen):
    a = np.array(data_set_A)
    b = np.array(data_set_B)
    print('data shape:', a.shape, b.shape)
    # compute difference set c
    c = []
    for i in a:
        for j in b:
            c.append(i-j)

    # choose any data from c to move c to origin
    
    
    x0 = -c[1]
    # x0=-np.array([-4.2,-5])
    x0=-np.array([-3.3,-6])
    c=np.array(c)
    print(c.shape)
    hull2=ConvexHull(c)
    plt.subplot(223)
    for simplex in hull2.simplices:
        plt.plot(c[simplex, 0], c[simplex, 1], 'k-')
        plt.plot((0,-x0[0]),(0,-x0[1]),'b-')
    
    print(c)
    # x0=-3*np.array([-1.41,-1.5])
    C = c+x0
    # print(C)
    # enlarge convex to make it as open set
    hull = ConvexHull(C)
    x_hit = hit(x0, hull)
    # plt.subplot(122)
    # plt.plot(x0[0],x0[1],'ro')
    # for simplex in hull.simplices:
    #     plt.plot(C[simplex, 0], C[simplex, 1], 'k-')
    # plt.show()
    # sub-linear functional
    P0 = minkowski(x0, hull)

    # extract linear functional, we choose middle point
    if chosen==0:
        L0 = 1.0
    elif chosen==1:
        L0 = (1.0+P0)/2
    else:
        L0 = P0

    # extension part

    x1, L1, alpha_list, beta_list, delta_list = extension_vertex_method(
        x0, L0, hull, C)
    # x1, L1, alpha_list, beta_list, delta_list = extension(x0, L0, hull)
    # compute the linear functional
    span1 = np.asmatrix([x0, x1]).T
    cofactor = np.dot(np.linalg.inv(span1).T, np.array([L0, L1]))
    print('span',span1)
    print('cofactor',cofactor)
    # compute gamma
    # graph of functional on set A and B: ((x,y),l(x,y)). l: R^2->R
    alpha, beta, gamma, graph_A, graph_B = compute_gamma(a, b, cofactor)

    # plot part
    if plot_flag:
        fun_x = [-7.5, 10.0]
        fun_y = [0, 0]
        fun_y[0] = (gamma-cofactor[0, 0]*fun_x[0])/cofactor[0, 1]
        fun_y[1] = (gamma-cofactor[0, 0]*fun_x[1])/cofactor[0, 1]
        # print(data_set_A.shape)
        print('fun y',fun_y)
        x1_min, x1_max = a[:, 0].min() - 1, a[:, 0].max() + 1
        x2_min, x2_max = b[:, 0].min() - 1, b[:, 0].max() + 1
        y1_min, y1_max = a[:, 1].min() - 1, a[:, 1].max() + 1
        y2_min, y2_max = b[:, 1].min() - 1, b[:, 1].max() + 1
        x_min, x_max = min(x1_min, x2_min), max(x1_max, x2_max)
        y_min, y_max = min(y1_min, y2_min), max(y1_max, y2_max)

        # plot result
        plt.subplot(221)
        title = 'P(x0)='+str(P0)
        plt.title(title)
        for simplex in hull.simplices:
            plt.plot(C[simplex, 0], C[simplex, 1], 'k-')
        print(C.shape)
        plt.plot(*zip(*C), 'bo')
        plt.plot([0, x0[0]], [0, x0[1]], 'b-')
        plt.plot([0, x1[0]], [0, x1[1]], 'r-')
        plt.plot(x_hit[0], x_hit[1], 'b^')
        plt.plot(0, 0, 'ro')

        plt.subplot(222)
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.plot(*zip(*a), 'bo',label="data set A")
        plt.plot(*zip(*b), 'go',label="data set B")
        plt.plot(fun_x, fun_y, 'r-')
        plt.legend()

        # plt.subplot(223)
        # plt.plot(delta_list, alpha_list, 'b')
        # plt.plot(delta_list, alpha_list, 'ro')
        # plt.subplot(224)
        # plt.plot(delta_list, beta_list, 'b')
        # plt.plot(delta_list, beta_list, 'ro')

        # title = 'alpha='+str(round(alpha, 4))+'. beta=' + \
        #     str(round(beta, 4))+'. gamma='+str(round(gamma, 4))
        # fig = plt.figure(title)
        # ax1 = fig.gca(projection='3d')
        # ax1.plot(graph_A[0][0], graph_A[0][1], graph_A[1], 'bo', label='set A')
        # ax1.plot(graph_B[0][0], graph_B[0][1], graph_B[1], 'ro', label='set B')
        # ax1.set_title(title)
        # plt.legend()
        plt.show()
    return gamma, cofactor

# compute seperation hyperplane

# iris = datasets.load_iris()
# # breast_cancer = datasets.load_breast_cancer()
# # wine = datasets.load_wine()
# X = iris.data[:, :2]  # we only take the first two features.
# y = iris.target
# # print(X.shape, y.shape)
# data_set_A = []
# data_set_B = []
# # print(X,y)
# for i in range(y.shape[0]):
#     if y[i] == 0:
#         data_set_A.append(X[i])
#     if y[i] == 1:
#         data_set_B.append(X[i])
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1)
# plt.show()
# print(data_set_A,data_set_B)
# gamma_list=[]
# cofactor_list=[]
# for i in range(1):
#     gamma,cofactor=seperator(rectangular_data_set_A, rectangular_data_set_B,i)
#     gamma_list.append(gamma)
#     cofactor_list.append(cofactor)
# for i in range(1):
#     fun_x = [-7.5, 10.0]
#     fun_y = [0, 0]
#     fun_y[0] = (gamma_list[i]-cofactor_list[i][0, 0]*fun_x[0])/cofactor_list[i][0, 1]
#     fun_y[1] = (gamma_list[i]-cofactor_list[i][0, 0]*fun_x[1])/cofactor_list[i][0, 1]
#     print('slope:',(fun_y[1]-fun_y[0])/(fun_x[1]-fun_x[0]))
#     if i==0:
#         plt.plot(fun_x, fun_y, 'r-')
#     if i==1:
#         plt.plot(fun_x, fun_y, 'g-')
#     if i==2:
#         plt.plot(fun_x, fun_y, 'b-')
# plt.plot(*zip(*rectangular_data_set_A), 'bo')
# plt.plot(*zip(*rectangular_data_set_B), 'go')
# plt.show()

# gamma,cofactor=seperator(data_set_A,data_set_B,2)
gamma,cofactor=seperator(rectangular_data_set_A,rectangular_data_set_B,2)