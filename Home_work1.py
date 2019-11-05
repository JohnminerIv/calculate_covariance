import numpy as np
import math
def cov_matrix_calculation(data):
    # calculate covariance matrix of the data
    new_mat = []
    for x in range(len(data[0])):
        new_row = []
        for y in range(len(data[0])):
            col_1 = []
            col_2 = []
            total = 0
            for a in data:
                col_1.append(a[x])
                col_2.append(a[y])
            col_1_mean = np.mean(col_1)
            col_2_mean = np.mean(col_2)
            for num1, num2 in zip(col_1, col_2):
                num1 = num1 - col_1_mean
                num2 = num2 - col_2_mean
                total += num1*num2
            all_len = len(col_1)
            den = all_len - 1
            cov = total/den
            new_row.append(cov)
        new_mat.append(new_row)
    cov_matx = np.cov(data.T)
    new_mat = np.array(new_mat)
    return new_mat

dataset = np.array([[5, 1, 1], [1, 2, 1], [1, 3, 2], [1, 4, 3]])
print(cov_matrix_calculation(dataset))
print(np.cov(dataset.T))
