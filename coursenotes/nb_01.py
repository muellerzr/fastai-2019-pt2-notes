# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/matmul.ipynb (unless otherwise specified).

__all__ = ['MNIST_URL']

# Cell
from pathlib import Path
from IPython.core.debugger import set_trace
import pickle, gzip, math, torch, matplotlib as mpl
import matplotlib.pyplot as plt
from torch import tensor
from fastcore.test import test_eq, test_close

from fastdownload import FastDownload

# Cell
MNIST_URL = "https://figshare.com/ndownloader/files/25635053"