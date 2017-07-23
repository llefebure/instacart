import numpy as np
import pandas as pd

def _f1_score_per_order(truth_str, pred_str):
    truth_set = set(truth_str.split())
    pred_set = set(pred_str.split())
    tp = len(truth_set & pred_set)
    if tp == 0:
        return 0.
    p = 1. * tp / len(pred_set)
    r = 1. * tp / len(truth_set)
    return 2 * p * r / (p + r)

def _f1_score(truth_list, pred_list):
    return np.mean([_f1_score_per_order(x, y) for x, y in zip(truth_list, pred_list)])

def _collapse(x):
    product_list = filter(lambda y: y != "", x)
    if len(product_list) == 0:
        return "None"
    else:
        return " ".join(map(str, product_list))

def binaryPredictionToString(X, preds, thr, dynamic = False):
    mat = X[["order_id", "product_id"]]
    if not dynamic:
        mat = mat.assign(products = map(lambda (pid, pr): "" if pr < thr else pid,
                                        zip(mat.product_id, preds)))
        preds_str = mat.groupby("order_id").agg({
            "products": _collapse
        })
        return preds_str
    else:
        mat = mat.assign(products = map(lambda (pid, pr, thr_v): "" if pr < thr_v else pid,
                                        zip(mat.product_id, preds, thr)))
        preds_str = mat.groupby("order_id").agg({
            "products": _collapse
        })
        return preds_str

def evaluate(X, y, preds, thr = np.linspace(.18, .22, 8), dynamic = False):
    truth_str = binaryPredictionToString(X, y, .5)
    rv = dict()
    if not dynamic:
        for t in thr:
            pred_str = binaryPredictionToString(X, preds, t)
            rv[t] = _f1_score(truth_str.values.flatten(), pred_str.values.flatten())
    else:
        pred_str = binaryPredictionToString(X, preds, thr, True)
        rv["dynamic"] = _f1_score(truth_str.values.flatten(), pred_str.values.flatten())
    return rv