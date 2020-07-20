import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import EllipseCollection


def CorrEllipses(corr, ax=None, colorbar=True, **kwargs):

    M = np.array(corr)

    assert M.ndim == 2, "'corr' must have two dimensions"

    if ax is None:
        fig, ax = plt.subplots(1, 1, subplot_kw={'aspect': 'equal'})
        ax.set_xlim(-0.5, M.shape[1] - 0.5)
        ax.set_ylim(-0.5, M.shape[0] - 0.5)
    else:
        fig = ax.gcf()

    # generate the center coodinates of the ellipses
    xy = np.indices(M.shape)[::-1].reshape(2, -1).T

    # generate width, height and angles of the ellipses
    w = np.ones_like(M).ravel()
    h = 1 - np.abs(M).ravel()
    a = 45 * np.sign(M).ravel()

    ec = EllipseCollection(widths=w, heights=h, angles=a, units='x', offsets=xy,
                           transOffset=ax.transData, array=M.ravel(), **kwargs)
    ax.add_collection(ec)

    # if data is a DataFrame, use the row/column names as tick labels
    if isinstance(corr, pd.DataFrame):
        ax.set_xticks(np.arange(M.shape[1]))
        ax.set_xticklabels(corr.columns, rotation=90)
        ax.set_yticks(np.arange(M.shape[0]))
        ax.set_yticklabels(corr.index)

    if colorbar:
        ec = fig.colorbar(ec)

    plt.tight_layout()
    plt.show()

    return ec
