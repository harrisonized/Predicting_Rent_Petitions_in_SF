import matplotlib.pyplot as plt


# Objects included in this file:

# Functions included in this file:
# # plot_empty (mpl)


def plot_empty(xlabel=None, ylabel=None,
               title=None,
               figsize=(8, 5)):
    """Initialize fig object for seaborns objects that do not include fig by default
    """
    fig = plt.figure(figsize=figsize, dpi=80)

    ax = fig.gca()
    ax.set_xlabel(xlabel, fontsize=16)
    ax.set_ylabel(ylabel, fontsize=16)
    ax.set_title(title, fontsize=24)

    return fig, ax
