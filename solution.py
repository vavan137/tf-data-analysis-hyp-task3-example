import pandas as pd
import numpy as np
#from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind

chat_id = 5463739632 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array,y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.01 
    #p = mannwhitneyu(x, y, alternative = 'greater')[1] #1/3
    _,p = ttest_ind(x, y, equal_var=False)
    return p < alpha
