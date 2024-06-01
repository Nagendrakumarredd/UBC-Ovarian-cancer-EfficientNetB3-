import numpy as np # linear algebra
import pandas as pd
There are two categories of images: whole slide images (WSI) and tissue microarray (TMA).
Whole slide images are at 20x magnification and can be quite large. The TMAs are smaller (roughly 4,000x4,000 pixels) but at 40x magnification.

train=pd.read_csv("/kaggle/input/UBC-OCEAN/train.csv")
print(train.head())
print(train.shape)
