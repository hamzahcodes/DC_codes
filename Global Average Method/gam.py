import numpy as np
import time

num_nodes = 5
data_size = 10

data = [np.random.rand(data_size) for i in range(num_nodes)]
print(data)

learning_rate = 0.1
num_iterations = 50

global_model = np.zeros(data_size)

for i in range(num_iterations):

    for j in range(num_nodes):

        local_model = data[j]
        local_model -= learning_rate * (local_model - global_model)
        data[j] = local_model

    global_model = np.mean(data, axis=0)

    print("Iteration ", {i + 1}, "Global model: ", global_model)

    time.sleep(0.1)