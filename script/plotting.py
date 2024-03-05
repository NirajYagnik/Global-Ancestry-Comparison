from matplotlib.lines import Line2D
from matplotlib import pyplot as plt
import pandas as pd

# def PlotPCA(evecfile, pcx, pcy, colorby="superpop", highlight_samples=[None], ax=None, 
#            use_legend=True):
def PlotPCA(data, pcx=1, pcy=2, prefix="PC", colorby="superpop", highlight_samples=[None], ax=None, use_legend=True) :
    """
    Make a PCA scatter plot from the plink .eigenvec file

    evecfile : str
        Path to the .eigenvec file output by plink --pca
    pcx : int
        PC to plot along the x axis
    pcy : int
        PC to plot along the y axis
    colorby : str (optional)
        Which category to color by. Default: "superpop"
        Options: "superpop", "pop"
    highlight_samples : list of str (optional)
        Highlight the location of these samples with big black dots
    ax : matplotlib Axes object (optional)
        If not specified, make a new axis
    use_legend : bool
        If False, don't plot legend
    """
    # Superpopulation color codes to use
    superpop_to_color = {
        "EUR": "purple",
        "AFR": "red",
        "SAS": "orange",
        "AMR": "blue",
        "EAS": "green"
    }

    pop_to_color = {
        "CHB": "olivedrab",
        "JPT": "yellowgreen",
        "CHS": "palegreen",
        "CDX": "darkgreen",
        "KHV": "green",
        "CHB": "lime",
        "CEU": "mediumpurple",
        "TSI": "lavender",
        "GBR": "thistle",
        "FIN": "plum",
        "IBS": "purple",
        "YRI": "firebrick",
        "LWK": "maroon",
        "GWD": "red",
        "MSL": "salmon",
        "ESN": "tomato",
        "ASW": "mistyrose",
        "ACB": "darksalmon",
        "MXL": "deepskyblue",
        "PUR": "dodgerblue",
        "CLM": "steelblue",
        "PEL": "royalblue",
        "GIH": "orange",
        "PJL": "darkorange",
        "BEB": "peru",
        "STU": "burlywood",
        "ITU": "bisque"
    }

    # Load metadata
    IGSRFILE="igsr_samples.tsv"
    samp = pd.read_csv(IGSRFILE, sep="\t")
    samp = samp[["Sample name", "Superpopulation code", "Population code"]]
    samp.rename(columns={"Sample name": "IID"}, inplace=True)

    # Load eigenvecs
#     data = pd.read_csv(evecfile, delim_whitespace=True, header=None)
#     data.columns = ["FID","IID"] + ["PC%s"%i for i in range(1, 11)]

    # Merge sample info
    data = pd.merge(data, samp, on=["IID"], how="left")

    if colorby == "superpop":
        data["color"] = data.apply(lambda x: superpop_to_color.get(x["Superpopulation code"], "gray"), 1)
    elif colorby == "pop":
        data["color"] = data.apply(lambda x: pop_to_color.get(x["Population code"], "gray"), 1)
    else:
        print("Invalid colorby (%s)%. Must be one of: superpop, pop."%colorby)

    if use_legend:
        if colorby == "superpop":
            legend_elements = [Line2D([0], [0], marker='o', color='w', label=spop,
                          markerfacecolor=superpop_to_color[spop], markersize=10) \
                  for spop in superpop_to_color.keys()]
        else:
            legend_elements = [Line2D([0], [0], marker='o', color='w', label=pop,
                          markerfacecolor=pop_to_color[pop], markersize=5) \
                  for pop in pop_to_color.keys()]

    # Plot pcx vs. pcy
    alpha = 1
    if len(highlight_samples)>0: alpha = 0.2
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
    ax.scatter(data[prefix + str(pcx)], data[prefix + str(pcy)], color=data["color"], s=5, alpha=alpha)

    for sample in highlight_samples:
        ax.scatter(data[data["IID"]==sample][prefix + str(pcx)], \
                  data[data["IID"]==sample][prefix + str(pcy)], s=50, color="black", edgecolor="darkgray")

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    if use_legend: ax.legend(handles=legend_elements, loc="lower right",
                             bbox_to_anchor=(1.3, 0))
    ax.set_xlabel(prefix + str(pcx))
    ax.set_ylabel(prefix + str(pcy))