"""Exact Python inference port of the generated MATLAB Neural Network Toolbox ANN files.
Generated from the supplied MATLAB *ANN.m files. This reproduces:
mapminmax -> tansig -> linear -> reverse mapminmax.
"""
from pathlib import Path
import json
import numpy as np

WEIGHTS=Path(__file__).with_name("matlab_ann_weights.json")
MODELS=json.loads(WEIGHTS.read_text(encoding="utf-8"))

def _arr(x): return np.asarray(x,dtype=float)

def predict(model_name, X):
    m=MODELS[model_name]
    X=_arr(X)
    if X.ndim==1: X=X.reshape(1,-1)
    if X.shape[1] != len(m['input_offset']):
        raise ValueError(f"{model_name} expects {len(m['input_offset'])} features, got {X.shape[1]}")
    # MATLAB generated function uses column vectors internally; row samples are transposed.
    xp=(X - _arr(m['input_offset'])) * _arr(m['input_gain']) + float(m['input_ymin'])
    a1=np.tanh(xp @ _arr(m['IW1_1']).T + _arr(m['b1']))
    a2=a1 @ _arr(m['LW2_1']).T + _arr(m['b2'])
    y=(a2 - float(m['output_ymin'])) / _arr(m['output_gain']) + _arr(m['output_offset'])
    return y

def model_info(model_name):
    m=MODELS[model_name]
    return {'inputs':len(m['input_offset']),'outputs':len(m['output_offset']),'source':m['source_file']}

if __name__=='__main__':
    for n in sorted(MODELS): print(n, model_info(n))
