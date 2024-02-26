import numpy as np
import random

y_data = []
x_data = []

for i in range(0,100):
    x_data.append(i)
    #y_data.append(((2*(i**2))+(3*i)+4)*random.uniform(0.8, 1.2)) #cлучайные значения
    y_data.append((2*(i**2))+(3*i)+4) # четкая парабола

#y_data = [1,2,3,4,5]
#x_data = [1,2,3,4,5]

print('x_data: \n{}\n'.format(x_data))
print('y_data: \n{}\n'.format(y_data))


string_to_matrix_x = '['
string_to_matrix_y = '['
for i in range(0, len(x_data)):
    string_to_matrix_x += '{}, {}, 1;'.format(str(x_data[i]**2), str(x_data[i]))
    string_to_matrix_y += '{} ;'.format((str(y_data[i])))
    #x_matrix[i][0] = x_data[i]**2
    #x_matrix[i][1] = x_data[i]
    #x_matrix[i][2] = 1
string_to_matrix_x = string_to_matrix_x[0:-1] + ']'
string_to_matrix_y = string_to_matrix_y[0:-1] + ']'
print(string_to_matrix_y)

y_matrix = np.matrix(string_to_matrix_y)
print('у-матрица: \n{}\n'.format(y_matrix))


x_matrix = np.matrix(string_to_matrix_x)
print("x-Матрица:\n{}\n".format(x_matrix))
x_matrix_transposed = np.transpose(x_matrix)
print("Транспонированная:\n {}\n".format(x_matrix_transposed))
xt_x_x = np.dot(x_matrix_transposed,x_matrix)
print("перемноженная:\n {}\n".format(xt_x_x))
x_matrix_multiplayed_inverted = (xt_x_x**(-1))
print("Обратная матрица: \n {}\n".format(x_matrix_multiplayed_inverted))
inverted_dot_xt = x_matrix_multiplayed_inverted*x_matrix_transposed
print("Обратная матрица, умноженная на транспоннированную: \n {}\n".format(inverted_dot_xt))
beta_matrix = inverted_dot_xt*y_matrix
print("Бета-матрица: \n {}\n".format(beta_matrix))

eps_matrix = y_matrix-x_matrix*beta_matrix
print("Вектор ошибок: \n {}\n".format(eps_matrix))

#функция потерь:
loss_funcrion = 0
for i in range(0,len(y_data)):
    loss_funcrion += (y_matrix[i]-x_matrix[i]*beta_matrix)**2
print("функция потерь: \n {}\n".format(loss_funcrion))

loss_funcrion_percent = 0
for i in range(0,len(y_data)):
    loss_funcrion_percent += ((y_matrix[i]-x_matrix[i]*beta_matrix)/y_matrix[i])**2
loss_funcrion_percent = (loss_funcrion_percent/len(y_data))**1/2
print("функция потерь в процентах: \n {}\n".format(loss_funcrion_percent))
