import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import ClusterCentroids
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn import svm


def MaxMinStandard(data):
    max = np.max(data, axis=0)
    min = np.min(data, axis=0)
    data = (data - min) / (max - min)
    return data


if __name__ == '__main__':
    fileLocation = r'./trainingset.csv'
    data = pd.read_csv(fileLocation, header=None)
    data = pd.DataFrame(data)

    # 将数据中的 '#REF!' 替换为空缺值 NaN
    data = data.replace('#REF!', np.nan)

    # 将所有数据转化为float类型
    data = data.astype(float)

    # 删除缺失项
    data.dropna(inplace=True)

    # 删除重复行元素
    data.drop_duplicates(inplace=True)

    # 对数据离差标准化处理
    data = MaxMinStandard(data)

    # PCA进行降维
    n_components = 10 # 设置目标维数
    pca = PCA(n_components=n_components)

    data_feature = pca.fit_transform(data.iloc[:, :-1])
    data_feature = pd.DataFrame(data_feature)


    print(data_feature.columns)

    # 数据的结果
    data_result = data.iloc[:, -1]

    # 查看label的分布情况，其是不平衡数据
    print(data_result.value_counts())

    '''
    我们可以使用过采样方法，即通过复制已有的样本或生成新的样本来增加样本数量，
    使得各类别之间的样本数量尽量平衡，从而提高模型性能和泛化能力。过采样方法可以更好地利用已有信息，
    减少信息损失，改善模型学习效果。
    '''

    ros = RandomOverSampler(random_state=42)  # 随机过采用
    X_resampled, y_resampled = ros.fit_resample(data_feature, data_result)

    # 查看过采样分布后的标签分布
    print(y_resampled.value_counts())

    # # 随机森林
    # # 定义候选参数集合
    # n_estimators_list = [100, 200, 300]
    # max_depth_list = [5,10,15]
    # # 先定义空载体，保存最优模型信息
    # best_accuracy = 0.0  # 最佳平均准确率
    # best_model = None  # 对应的分类器

    # # 进行十折交叉验证
    # for n_estimators in n_estimators_list:
    #     for max_depth in max_depth_list:
    #         # 创建新的随机森林分类器
    #         clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    #         # 在当前参数下进行交叉验证，并计算平均评分
    #         scores = cross_val_score(clf, X_resampled, y_resampled, cv=10)
    #         accuracy = np.mean(scores)

    #         # 输出当前参数及其对应的平均评分
    #         print("n_estimators={}, max_depth={}, accuracy={:.4f}"
    #               .format(n_estimators, max_depth, accuracy))

    #         if accuracy > best_accuracy:
    #             # 如果当前模型性能优于之前所有模型，则更新最优模型的信息
    #             best_accuracy = accuracy
    #             best_model = clf


    #支持向量机
    kernel_list = ['linear', 'rbf', "poly"] # 核函数
    gamma_list = [0.5, 0.4, 1, 2, 3, 5]
    # 先定义空载体，保存最优模型信息
    best_accuracy_svm = 0.0  # SVM最佳平均准确率
    best_model_svm = None  # SVM

    for kernel in kernel_list:
        for gamma in gamma_list:
            svm_clf = svm.SVC(kernel=kernel, gamma=gamma, random_state=42)
            # 在当前参数下进行交叉验证，并计算平均评分
            svm_scores = cross_val_score(svm_clf, X_resampled, y_resampled, cv=10)
            svm_accuracy = np.mean(svm_scores)

            # 输出当前参数及其对应的平均评分
            print("kernel={}, gamma={}, accuracy={:.4f}"
                  .format(kernel, gamma, svm_accuracy))

            if svm_accuracy > best_accuracy_svm:
                # 如果当前模型性能优于之前所有模型，则更新最优模型的信息
                best_accuracy_svm = svm_accuracy
                best_model_svm = svm_clf


    # if best_accuracy_svm > best_accuracy:
    #     # 如果SVM模型性能优于随机森林模型，则更新信息
    #     # best_accuracy = best_accuracy_svm
    #     best_model = svm_clf
    # 输出最优模型的信息
    print("\nBest Model:")
    # print(best_model)
    print(best_model_svm)


    # 在整个过采样后的训练集上训练最优模型
    # best_model.fit(X_resampled, y_resampled)
    best_model_svm.fit(X_resampled, y_resampled)

    # 在测试集上进行测试并输出准确率
    test_df = pd.read_csv(r'./testingset.csv',header=None)
    #将数据类型转化为float型
    test_df = test_df.astype(float)

    # #删除重复项
    # test_df.drop_duplicates(inplace=True)

    # #删除缺失项
    # test_df.dropna(inplace=True)
    # test_feature = MaxMinStandard(test_df)

    #将测试数据的特征进行标准化
    test_feature =  pca.fit_transform(test_df.iloc[:,:-1])
    # test_feature = pca.fit_transform(test_feature)


    test_result = test_df.iloc[:,-1]

    X_test, y_test = test_feature, test_result
    # y_pred = best_model.predict(X_test)
    y_pred = best_model_svm.predict(X_test)
    # y_pred = pd.DataFrame(y_pred)
    # print(y_pred)
    # with pd.ExcelWriter(r'C:\Users\Promise\Desktop\数据挖掘\期末大作业\data2.xlsx') as writer:
    #     y_pred.to_excel(writer, sheet_name='Sheet1', index=False)
    print(y_pred)
    print('\n')
    print(y_test.to_numpy())
    accuracy = np.mean(y_pred == y_test)
    print("\nAccuracy on testing set: {:.4f}".format(accuracy))