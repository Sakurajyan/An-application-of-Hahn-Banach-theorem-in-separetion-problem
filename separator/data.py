from scipy.stats import multivariate_normal
import numpy as np
import math as math


mu1 = [-2, 0]
mu2 = [4, 5]
sigma1 = np.asmatrix(np.array([[3, 1], [1, 2]]))
sigma2 = np.asmatrix(np.array([[4, 2], [2, 3]]))

# test
data_set_A1 = [[-0.41672557,  1.398315],
               [-1.24825038, 1.58039025],
               [-2.2832855, 3.81191653],
               [-0.38543374, 3.42340223],
               [-0.43210812, 3.21891443],
               [-0.80985653, 2.47240024],
               [-0.97596337, 3.26604028],
               [-0.9967618, 2.38629391],
               [-0.85850381, 1.88482301],
               [-0.54923661, 1.97026391],
               [-0.10340924, 2.02179385],
               [-1.58804805, 2.81234695],
               [0.51095765, 3.93865714],
               [-0.77889936, 3.55420906],
               [0.15744491, 3.1123339],
               [-0.85149984, 3.42612581]]
data_set_B1 = [[3.7866518, 5.82479],
               [3.53811409, 5.45558053],
               [3.59220714, 6.42932479],
               [3.92520523, 6.04514376],
               [4.47671295, 7.56423331],
               [4.55294128, 5.53446897],
               [3.71891267, 6.41374143],
               [3.91462593, 6.93449917],
               [4.20957364, 6.81814764],
               [6.01200715, 5.4364312],
               [5.10160758, 6.84527904],
               [4.98709866, 6.22253377],
               [3.93943144, 3.19737325],
               [2.88400649, 4.66255114],
               [6.26682822, 7.40459127],
               [4.95671104, 6.44343971]]
data_set_A = [[-2.48567933, -2.41689157],
              [-3.01463895, -1.57848873],
              [-4.17742529, -3.72771572],
              [-3.68497224, -2.19331339],
              [-4.43445, -2.93764659],
              [-1.99948133, -2.73300006],
              [-3.50959037, -1.82023787],
              [-4.41728477, -3.61380097],
              [-3.2522333, -3.53522886],
              [-2.93981534, -2.09512714],
              [-3.88345728, -1.96414957],
              [-4.30817053, -4.75770629],
              [-4.23616495, -2.7989539],
              [-3.32343483, -2.17558301],
              [-2.36560386, -2.05017034],
              [-2.77330307, -2.92850008]]

data_set_B = [[7.04272424, 6.59600282],
              [3.74454555, 6.34025232],
              [4.92737701, 6.36462701],
              [4.31114103, 4.49385861],
              [5.17383546, 6.06265392],
              [5.46584576, 6.0593176],
              [5.01633088, 7.70028267],
              [6.45836458, 5.87081359],
              [5.60306597, 5.41604542],
              [5.60631279, 5.79070753],
              [5.50343026, 5.57260416],
              [5.61728279, 6.1568033],
              [4.02779673, 6.86853153],
              [6.05461899, 7.08300063],
              [3.91855717, 7.75915824],
              [5.62758577, 4.67142235]]


# data_set_A = np.random.multivariate_normal(mu1, sigma1, 16)
# data_set_B = np.random.multivariate_normal(mu2, sigma2, 16)

data_set_A3 = [[0.45840146,  4.2589557],
               [-0.27126001,  0.86440821],
               [-0.37408603,  1.96826864],
               [-1.36175428,  3.70895365],
               [-0.84542701,  2.45196437],
               [-1.00549296,  1.38016292],
               [-1.03851767,  2.76892133],
               [-1.55974203,  3.91156088]]
data_set_B3 = [[5.21225911, 4.64282414],
               [4.20891528, 4.64331109],
               [2.87638914, 6.16162457],
               [3.86796725, 5.60158208],
               [3.9469907, 5.60258318],
               [3.6385538, 5.09862199],
               [3.54397608, 5.89238139],
               [3.88304839, 6.72681335]]
rectangular_data_set_A=[[0,0],[0,1],[1,0],[1,1]]
rectangular_data_set_B=[[4,5],[4,7],[5,5],[5,7]]