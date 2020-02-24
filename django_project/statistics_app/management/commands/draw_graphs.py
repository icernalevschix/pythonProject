import matplotlib.pyplot as plt

def totals_graph(data):
    fig, ax = plt.subplots(figsize = (12,6))
    plt.rcParams['font.family'] = 'Cambria'

    plt.barh(*zip(*data), align='center',color='#86bf91', zorder=2)
    ax.set_xlabel('usage')

    # Despine
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Switch off ticks
    ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    # Draw vertical axis lines
    vals = ax.get_xticks()
    for tick in vals:
        ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    # Set x-axis label
    ax.set_xlabel("Job Posts", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    plt.title("The Most Wanted \nProgramming Languages in Moldova", weight='bold', size=16)

    # create a list to collect the plt.patches data
    totals = []

    # find the values and append to list
    for i in ax.patches:
        totals.append(i.get_width())

    # set individual bar lables using above list
    total = sum(totals)

    # set individual bar lables using above list
    for i in ax.patches:
        # get_width pulls left or right; get_y pushes up or down
        ax.text(i.get_width()+.3, i.get_y()+.38, \
                str(round((i.get_width()/total)*100, 2))+'%', fontsize=15,
    color='dimgrey')

    # invert for largest on top 
    ax.invert_yaxis()

    return plt