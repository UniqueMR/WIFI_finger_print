import numpy as np
from numpy.core.fromnumeric import trace
import scipy.io as scio
from sklearn.model_selection import GridSearchCV
from sklearn import neighbors
import matplotlib.pyplot as plt

#导入离线文件和在线文件
offline_data = scio.loadmat('E:\\Wifi指纹_软件课设\\my_work\\database\\offline_data.mat')
online_data = scio.loadmat('E:\\Wifi指纹_软件课设\\my_work\\database\\online_data.mat')

#分别获取离线文件和在线文件的rss指纹以及位置
offline_location, offline_rss = offline_data['offline_location'], offline_data['offline_rss']
trace, rss = online_data['trace'], online_data['rss']

#删除无关变量，释放内存空间
del online_data
del offline_data

#定位精度，定义为Euclidean距离
def accuracy(predictions, labels):
    return np.mean(np.sqrt(np.sum((predictions - labels)**2,1)))

#交叉验证，在knn中用来选择最优的参数K
parameters = {'n_neighbors' : range(1, 50)} #创建等待验证的参数列表
knn_reg = neighbors.KNeighborsRegressor(weights='uniform', metric='euclidean') #创建knn算法对象
clf = GridSearchCV(knn_reg, parameters) #在给定列表中调整k值，找到knn模型的最佳k值
clf.fit(offline_rss, offline_location) #对模型进行拟合
scores = clf.cv_results_['mean_test_score'] #输出所有k值的得分
k = np.argmax(scores) #选择score最大的k

# 绘制超参数k与score的关系曲线
plt.plot(range(1, scores.shape[0] + 1), scores, '-o', linewidth = 2.0) #横轴设置为对应的k值，纵轴为对应k值的得分
plt.xlabel('k')
plt.ylabel('score')
plt.grid(True)
plt.show()

# 使用最优的k做knn回归
knn_reg = neighbors.KNeighborsRegressor(n_neighbors=k, weights='uniform', metric='euclidean') #利用最优的k值构建knn模型
predictions = knn_reg.fit(offline_rss, offline_location).predict(rss) #利用knn模型对offline_data进行拟合，并对online_data进行预测
acc = accuracy(predictions, trace) #利用预测值和真实值计算准确度
print("accuracy : ",acc/100, "m")

