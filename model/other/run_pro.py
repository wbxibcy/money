# %%
# load packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
import platform
if platform.system() == "Windows":
    plt.rcParams['font.family'] = ['SimHei'] # Windows
elif platform.system() == "Darwin":
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # MacOS
plt.rcParams['axes.unicode_minus']=False 


data = pd.read_excel("/Users/liyong/Downloads/1(2).xlsx")

# %%
X = data.iloc[:,1:]
y = data.iloc[:,0]

# %%
###  Regression Models
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

# SVR，KNN，GBDT，RF，LR
models_untrained = [
	RandomForestRegressor(),
	GradientBoostingRegressor(),
	DecisionTreeRegressor(max_depth=3),
	AdaBoostRegressor(),
	LinearRegression()
]

def scatterplot_comparison(model=None,X_test=None,y_test=[],y_pred_test=[],X_train=None,y_train=[],y_pred_train=[]):
	"""define a function that plots comparison in scatter"""
	if model is not None:
		if X_test is not None:
			y_pred_test = model.predict(X_test)
		if X_train is not None:
			y_pred_train = model.predict(X_train)
	# change to list
	y_train = list(y_train)
	y_test = list(y_test)
	y_pred_train = list(y_pred_train)
	y_pred_test = list(y_pred_test)
	# plot
	plt.figure(figsize=(8,7))
	if len(y_train)>0:
		plt.scatter(y_train,y_pred_train,marker='o',s=30,edgecolors='black',linewidths=0.5,alpha=0.9)
	if len(y_test)>0:
		plt.scatter(y_test,y_pred_test,marker='o',s=30,edgecolors='black',linewidths=0.5,alpha=0.9)
	# axis ranges
	ranges = min(y_test+y_train),max(y_test+y_train)
	# plot range
	plt.plot(ranges,ranges,'r')
	plt.xlabel('True Value')
	plt.ylabel('Predictions')
	plt.legend()

	model = 'Model' if model is None else model
	plt.title(f"{type(model).__name__}")
	plt.tight_layout()
	plt.savefig(f"{type(model).__name__} - predict value.jpg",dpi=300)
	plt.show()



def evaluation_regression(y_test,y_pred):
    """评估回归模型"""
    metrics = {}
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import mean_absolute_error
    from sklearn.metrics import r2_score
    metrics['MSE'] = mean_squared_error(y_test,y_pred)
    metrics['RMSE'] = mean_squared_error(y_test,y_pred) ** 0.5
    metrics['MAE'] = mean_absolute_error(y_test,y_pred)
    metrics['R2'] = r2_score(y_test,y_pred)
    return metrics

eval_dic= {}
for model in models_untrained:
    model.fit(X,y)
    y_pred = model.predict(X)
    metric = evaluation_regression(y,y_pred)
    print("="*100)
    scatterplot_comparison(model=model,X_test=X,y_test=y)
    print(type(model).__name__)
    eval_dic[type(model).__name__] = metric.copy()
    print(metric)
    
# plot one metric
def plot_metric(metric_dic,metric = 'SCORE',dataset_name = None):
	"""
	metric_dic looks like: {'model_name':{'metric_name': value}}
	"""
	# 画图，画出各个模型的指标对比
	x = []
	y = []
	# 提取数据
	for model_name in metric_dic.keys():
		x.append(model_name)
		y.append(metric_dic.get(model_name).get(metric))
	plt.figure(figsize=(10,7))
	# 画柱形图
	plt.bar(x,y)
	for i,j in zip(range(len(x)),y):
		plt.text(i,j,'{:.4}'.format(j),va='bottom',ha='center')
	# 设置标题坐标轴名称
	plt.title(f"{dataset_name} - " if dataset_name else '' + f"Model Comparison")
	plt.xlabel("Model Name")
	plt.ylabel(metric.title())
	plt.xticks(rotation=45)
	plt.ylim(np.min(y)*0.9,np.max(y)*1.05)
	plt.tight_layout()
	# 保存图片
	plt.savefig(f"{dataset_name} - " if dataset_name else '' + f"Comparison - {metric}.jpg",dpi=300)
	plt.show()
plot_metric(eval_dic,metric='R2')

# %%



