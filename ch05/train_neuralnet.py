# coding: utf-8
import sys, os
parent_dir = os.path.abspath(os.getcwd())
sys.path.append(parent_dir)

import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

# 读入数据
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# 参数
iters_num = 10000 # 训练总次数
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

# 循环训练

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    # 梯度
    #grad = network.numerical_gradient(x_batch, t_batch)
    grad = network.gradient(x_batch, t_batch)
    
    # 更新
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
    
    loss = network.loss(x_batch, t_batch) # 该轮损失
    train_loss_list.append(loss) # 记录每一轮的损失
    
    if i % iter_per_epoch == 0: # 如果每个数据都在期望值上被训练过一遍了
        train_acc = network.accuracy(x_train, t_train) # 训练集精确度
        test_acc = network.accuracy(x_test, t_test) # 测试机精确度
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(train_acc, test_acc) # 打印数据
