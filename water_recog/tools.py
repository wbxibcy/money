import pickle


# 导入接口
def dumpTree(inputTree, filename):
    try:
        fw = open(filename, 'wb')
        pickle.dump(inputTree, fw)
        fw.close()
        print("模型保存成功")
    except IOError as e:
        print(e)


def loadTree(filename):
    try:
        fr = open(filename, 'rb')
        print("模型加载成功")
        return pickle.load(fr)
    except IOError as e:
        print(e)
    return None



def save_model(clf, save_model_path="model.pk"):
    dumpTree(clf, save_model_path)

def load_model(model_path="model.pk"):
    clf = loadTree(model_path)
    return clf

