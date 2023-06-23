import torch
from hloc import matchers,extractors
from hloc.utils.base_model import dynamic_load
from hloc import match_dense, match_features, extract_features

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def get_model(match_conf):
    Model = dynamic_load(matchers, match_conf['model']['name'])
    model = Model(match_conf['model']).eval().to(device)
    return model

def get_feature_model(conf):
    Model = dynamic_load(extractors, conf['model']['name'])
    model = Model(conf['model']).eval().to(device)
    return model
from utils.utils import get_model, get_feature_model, device


matcher_zoo = {
    'sold2': {
        'config': match_dense.confs['sold2'],
        'dense': True
    },
    'gluestick': {
        'config': match_dense.confs['gluestick'],
        'dense': True
    },
    'loftr': {
        'config': match_dense.confs['loftr'],
        'dense': True
    },
    'topicfm': {
        'config': match_dense.confs['topicfm'],
        'dense': True
    },
    'aspanformer': {
        'config': match_dense.confs['aspanformer'],
        'dense': True
    },
    'superglue': {
        'config': match_features.confs['superglue'],
        'config_feature': extract_features.confs['superpoint_max'],
        'dense': False
    },
    'd2net': {
        'config': match_features.confs['NN-mutual'],
        'config_feature': extract_features.confs['d2net-ss'],
        'dense': False
    },
    'disk': {
        'config': match_features.confs['NN-mutual'],
        'config_feature': extract_features.confs['disk'],
        'dense': False
    },
    'r2d2': {
        'config': match_features.confs['NN-mutual'],
        'config_feature': extract_features.confs['r2d2'],
        'dense': False
    },
    'sift': {
        'config': match_features.confs['NN-mutual'],
        'config_feature': extract_features.confs['sift'],
        'dense': False
    },
    'roma': {
        'config': match_dense.confs['roma'],
        'dense': True
    },
    'DKMv3': {
        'config': match_dense.confs['dkm'],
        'dense': True
    },
}