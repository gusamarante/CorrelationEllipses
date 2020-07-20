import numpy as np
import pandas as pd
from correllipse import CorrEllipses

d = 10  # number of varibles
k = 1  # number of factors (for the correlation matrix simulation)

# ===== SIMULATE THE CORRELATION MATRIX =====
W = np.random.randn(d, k)  # randomly generate several k < d factor loadings W
S = W@W.T + np.diag(np.random.rand(1, d))  # form the covariance WW' and add a random diagonal D
S = np.diag(1./np.sqrt(np.diag(S))) @ S @ np.diag(1./np.sqrt(np.diag(S)))  # normalize coviariance to a correlation
corr_mat = pd.DataFrame(data=S, index=range(d), columns=range(d))

new_order = list(corr_mat.sort_values(0).index)

corr_mat = corr_mat[new_order].loc[new_order]

# ==== PLOT =====
CorrEllipses(corr_mat, cmap='RdBu', clim=[-1, 1])

