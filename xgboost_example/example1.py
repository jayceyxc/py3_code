#!/usr/bin/env python3
'''
@File    :   example1.py
@Time    :   2020/03/28 19:50:05
@Author  :   Yu Xuecheng 
@Version :   1.0
@Contact :   yuxuecheng@xinluomed.com
@License :   (C)Copyright 2020-2022, yuxuecheng
@Desc    :   XGBoost简单示例
'''

# here put the import lib
import xgboost as xgb

XGBOOST_PATH = '/Users/yuxuecheng/Learn/OpenSource/cpp/xgboost'


def main():
    # 数据读取
    xgb_train = xgb.DMatrix(f'{XGBOOST_PATH}/demo/data/agaricus.txt.train')
    xgb_test = xgb.DMatrix(f'{XGBOOST_PATH}/demo/data/agaricus.txt.test')

    # 定义模型训练参数
    params = {
        "objective": "binary:logistic",
        "booster": "gbtree",
        "max_depth": 3
    }
    # 训练轮数
    num_round = 5

    # 训练过程中实时输出评估结果
    watchlist = [(xgb_train, 'train'), (xgb_test, 'test')]

    # 模型训练
    model = xgb.train(params, xgb_train, num_round, watchlist)

    # 模型预测
    preds = model.predict(xgb_test)
    print(list(preds))


if __name__ == "__main__":
    main()
