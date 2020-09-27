import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib
import matplotlib.pyplot as plt
s=Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
s.plot()