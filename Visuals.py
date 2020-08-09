from matplotlib import pyplot as plt
import numpy as np
from matplotlib import style

style.use('ggplot')

plt.grid(True, color='k')

X = [1, 2, 3]

Y = [4, 5, 6]

X_1 = [7, 8, 9]

Y_1 = [10, 11, 12]

plt.plot(X, Y, 'g', label='line one', linewidth=5)

plt.plot(X_1, Y_1, 'b', label='line two', linewidth=5)

plt.legend()

plt.title('Title')

plt.xlabel('X-Axis')

plt.ylabel('Y-Axis')

plt.show()

plt.bar([1, 3, 5, 7, 8], [5, 6, 8, 7, 5], color='r')
plt.bar([3, 4, 6, 8, 10], [8, 6, 3, 5, 6], color='g')
plt.title('Example_2')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

Random_Numbers = np.random.random([1, 20])
Random_Numbers_1 = np.linspace(1, 20, num=20, endpoint=True)
plt.hist(Random_Numbers, Random_Numbers_1, histtype='bar', rwidth=0.8)
plt.title('Histogram')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

plt.scatter(Random_Numbers, Random_Numbers_1, color='k')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

Random_Numbers = [1, 2, 3, 4]
Lable = ['Random_1', 'Random_2', 'Random_3', 'Random_4']
Colors = ['c', 'm', 'r', 'b']
plt.pie(Random_Numbers, labels=Lable, colors=Colors, startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
        autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()


def f(x):
    return np.exp(-x) * np.sin(2 * np.pi * x)


x_1 = np.arange(0.0, 5.0, 0.1)
x_2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(x_1, f(x_1), 'bo', x_2, f(x_2))

plt.subplot(212)
plt.plot(x_2, np.sin(2 * np.pi * x_2))
plt.show()
