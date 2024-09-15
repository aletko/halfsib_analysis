import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
from matplotlib.ticker import FuncFormatter




def plotting(chr_file, locations, output):

    # Read data from CSV files
    chromosomes = pd.read_csv(chr_file, sep=";")
    data = pd.read_csv(locations, sep=";")

    scale = 1000000

    pdf_width = 11.69
    pdf_height = 8.27
    line_width = 5
    plt.figure(figsize=(pdf_width, pdf_height))

    fig, ax = plt.subplots()
    ax.bar(chromosomes['Chr'], chromosomes['length'] / scale, width=0.4, color='grey')

    # Inverted y-axis
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    # Print blue regions from the test locations
    for run in range(1, 30):
        subset = data[data['CHR'] == run]
        if len(subset) > 0:
            for _, row in subset.iterrows():
                start_position = row['BP1'] / scale
                end_position = row['BP2'] / scale
                ax.plot([run, run], [start_position, end_position], lw=line_width, color='red')
        else:
            print(f"No variant on chromosome {run}")

    def scale_format(x, pos):
        return f"{int(x*scale):,}"
    ax.plot([], [], lw=line_width, color='red', label='Variants')
    y_ticks = ax.get_yticks()
    for y in y_ticks:
            ax.axhline(y=y, color='black', linestyle='--', linewidth=0.5)
    ax.yaxis.set_major_formatter(FuncFormatter(scale_format))
    ax.legend(loc='lower right')
    ax.set_ylabel("Length in Mb")
    ax.set_xlabel("Chromosomes")
    ax.set_xticks(chromosomes['Chr'])
    ax.set_xticklabels(chromosomes['Chr'])
    ax.tick_params(axis='x', labelsize=8)
    ax.grid(False)

    plt.savefig(output, format="pdf")
    plt.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Plot output with chromosomes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--chr", required=True, help=".csv file")
    parser.add_argument("--locations", required=True, help=".csv file")
    parser.add_argument("--plot", required=True, help=".csv file")
    args = parser.parse_args()

    plotting(args.chr, args.locations, args.plot)