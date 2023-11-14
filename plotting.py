import matplotlib.pyplot as plt

def plot_curve(x, y, xlabel, ylabel, xticks=None, ylim=None, title=""):
    #  plt.axis("equal")
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    if xticks is not None:
        plt.xticks(xticks, fontsize=10)
    else:
        plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    if ylim is not None:
        plt.ylim(ylim)
    plt.title(title)
    plt.plot(x, y, "ro-", linewidth=2, markersize=4) 
    plt.grid(True)
    plt.show()
    
def plot_curve2(x1, y1 , x2, y2, xlabel, ylabel, xticks=None, ylim=None, title=""):
    # ts = np.linspace(1,12,100)
    # val_x = lagrange(t,x, ts)
    plt.grid(True)
    plt.plot(x1, y1, "bo-",linewidth=1, markersize=1)
    plt.plot(x2, y2, "ro", linestyle='dashed', linewidth=1, markersize=3)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    if xticks is not None:
        xticks = list(xticks)
        xticks.append(xticks[-1]+1)
        plt.xticks(xticks, fontsize=10)
    else:
        plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    if ylim is not None:
        plt.ylim(ylim)
    plt.title(title)
    plt.legend(["Lagrange","sample"])
    plt.show()
    
