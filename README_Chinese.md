## Overview

这个文档是MIT596操作系统课程期末测试

[中文说明](./README_Chinese.md) [English Doc](./README.md)



## 题目介绍

### 1.CPU调度算法

计算CPU可以处理空闲时间

输入：最少3个进程，最多6个进程;  
输出：表（请参阅示例表）

示例表



![image-20220207010528604](./img/img1.png)

甘特图

![image-20220207010528604](./img/img2.png)





> 词汇说明
>
> BT = 指*CPU*从接到命令到开始处理命令所需时间
>
> AT = *CPU*从接到命令的时间
>
> S = 开始执行的时间
>
> E = 结束的时间
>
> RT = 进程到达CPU首次执行的时间
>
> WT= 等待时间
>
> TT = 进程到达到执行完所需的时间



### 2. 页面替换算法 (FIFO, OPTIMAL 和LRU);

规范：

输入：最少3帧，最多5帧;引用字符串最小值为 20 个字符;

输出：模拟表

​        缺页异常的数量

​		命中的数量



### 3.磁盘调度算法

规范：

FSCS, SSTF, LOOK, C-LOOK, SCAN, C-SCAN

输入：请求数（最少12个）;当前头部位置，先前的头部位置
输出：图表
	 遍历的轨道数。



## 快速上手配置

```
# centos
yum install python

# ububut
apt install python3 python3-pip
pip3 install prettytable colorama

# windows
# Install python3 by yourself
pip3 install prettytable colorama
```



## result



![image-20220207011321494](./img/image-20220207011321494.png)

![image-20220207011321494](./img/image-20220207011321496.png)
