import argparse
import json 
import pickle
from re import I
import pandas as pd 
import numpy as np
from pathlib import Path
import os 
from typing import List
from sklearn.model_selection import StratfiedKFold
import pprint
from tqdm import tqdm 
import torch 
import cv2 


def parse_arguments(args: List[str] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='VGG model classifier')
    parser.add_argument()

    return parser.parse_args(args)

class PreprocessWM811K(object):
    def __init__(
        self,
        data_path: str,
        column_name_wafermap: str = "waferMap",
        column_name_label: str = "",
        config_class2idx_path: str = "",
        save_flag: bool = True
        ) -> None:
        
    def stratify_split(self):
        kf = StratfiedKFold()
        return 

    def find_dim(self, x):
        dim0 = np.size(x, axis=0)
        dim1 = np.size(x, axis=1)
        return dim0, dim1

    def extract_with_label_data(self):

    def _init_dataset(self):


def format_input(X: np.ndarray, height=80, width=80):
    

    