# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import os

pwd_path = os.path.abspath(os.path.dirname(__file__))

# Training data path.
# CGED chinese corpus
cged_train_paths = [
    os.path.join(pwd_path, '../data/cn/CGED/CGED18_HSK_TrainingSet.xml'),
    os.path.join(pwd_path, '../data/cn/CGED/CGED17_HSK_TrainingSet.xml'),
    os.path.join(pwd_path, '../data/cn/CGED/CGED16_HSK_TrainingSet.xml'),
    # os.path.join(pwd_path, '../data/cn/CGED/sample_HSK_TrainingSet.xml'),
]

sighan_train_path = os.path.join(pwd_path, '../data/cn/sighan_2015/train.tsv')

use_segment = False
segment_type = 'char'

output_dir = os.path.join(pwd_path, 'output')
# Training data path.
train_path = os.path.join(output_dir, 'dev.json')
# Validation data path.
valid_path = os.path.join(output_dir, 'dev.json')
test_path = os.path.join(output_dir, 'dev.json')

dataset = 'sighan'  # 'sighan' or 'cged'
arch = 'SoftMaskedBert'
pretrained_model = 'bert-base-chinese'  # official pretrained model, bert-base-chinese / hfl/chinese-macbert-base

# config
src_vocab_path = os.path.join(output_dir, 'vocab_source.txt')
trg_vocab_path = os.path.join(output_dir, 'vocab_target.txt')
model_dir = os.path.join(output_dir, 'model_{}'.format(dataset))
ckpt_path = os.path.join(model_dir, 'epoch=02-val_loss=0.01904.ckpt')

batch_size = 32
epochs = 1
gpu_ids = [0]

os.makedirs(model_dir, exist_ok=True)
