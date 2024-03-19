# 13.7. Parameter Servers

## 13.7.1. Data-Parallel Training
all gradient are aggregated on one GPU, and then broadcast to all GPUs.

### 3 different ways for param synchronizaiton


![pic](pic/image1.png)

## 13.7.2. Ring Synchroniztion
divide gradient to n chunks, and transfer one chunk one time through the ring
![pic](pic/image3.png)
## 13.7.3 Multi-Machine Training
![pic](pic/image2.png) 
a single parameter server is a bottleneck since its bandwidth is finite, in practice we use the same machines both as worker as servers.
## 13.7.4 Key_Value Stores