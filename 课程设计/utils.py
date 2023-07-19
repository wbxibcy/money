import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn import metrics

def Score(data_predicted):
    data_real_np = np.load('evaluate.npy')
    data_real = pd.DataFrame(data_real_np)
    data_real.columns = ['ID', 'Label_real']
    data = pd.merge(data_real, data_predicted, how='left', on='ID')
    # accuracy
    accuracy = data.Label_real[(data.Label_real == data.Label)].count() / len(data.Label_real)
    # f1_score
    f1_score = metrics.f1_score(data.Label_real, data.Label, average="weighted")
    print('='*60)
    # 评估报告
    print(classification_report(data.Label_real, data.Label))
    print('='*60)
    print('你的成绩为：%.2f' % (f1_score*100))