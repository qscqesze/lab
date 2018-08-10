import json, sys
from sklearn import cross_validation,metrics
from sklearn import svm
import pandas as pd
import numpy as np

class KaggleCore(object):
    def __init__(self):
        return

    def get_testx_validx(self, d):
        df1 = pd.read_csv(d['method_other'].get('file1'))
        df2 = pd.read_csv(d['method_other'].get('file2'))
        test_y = df1['Survived']
        validy = df2['Survived']
        return test_y,validy

    def solve_1001(self, d):
        print('start solve!')
        test_y, validy = self.get_testx_validx(d)
        auc = metrics.roc_auc_score(test_y, validy)
        d['status'] = str(auc)
        print(str(d))

    def solve(self,line):
        print(line)
        d = json.loads(line.replace("'",'"'))
        if d['problem'] == '1001':
            self.solve_1001(d)



def test():
    print('Im in!')
    j = {"id": "1","problem": "1001","method": "auc","method_other": {"file1": "/home/qingjun/lab/test/kaggle_core_test/titanic.csv","file2": "/home/qingjun/lab/test/kaggle_core_test/gender_submission.csv",},"status": "pending" ,}
    kaggle_core = KaggleCore()
    kaggle_core.solve(str(j))


if __name__ == '__main__':
    test()
    #kaggle_core = KaggleCore()
    #for line in sys.stdin:
    #    KaggleCore.solve(line)