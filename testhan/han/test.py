import matplotlib.pyplot as plt

num_list = [0.00265288]
num_list_1 = [0.001415729]
x = list(range(len(num_list)))

total_width, n = 0.8, 2
width = total_width / n 

plt.bar(x,num_list, width=width, label = 'old',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x,num_list_1, width=width, label="new", fc='r')
plt.legend()
plt.show()


