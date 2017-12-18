import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, output_file, curdoc
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import row, column, widgetbox


#Create steps in a loop and append them to our arrays
def get_walks(walk_length, n_walks):
    """returns a list of lists for the x and y coordinates of a specified
    number of random walks of a specified length"""
    x_walks = [ [] for x in range(n_walks)]
    y_walks = [ [] for x in range(n_walks)]
    for w in range(n_walks):
        x, y = ([0], [0])
        for i in range(walk_length):
            random = np.random.random()
            if random < 0.25:
                x.append(x[i] + 1)
                y.append(y[i])
            elif random < 0.5:
                x.append(x[i] - 1)
                y.append(y[i])
            elif random < 0.75:
                y.append(y[i] + 1)
                x.append(x[i])
            else:
                y.append(y[i] - 1)
                x.append(x[i])
        x_walks[w] = x
        y_walks[w] = y
        x, y = ([0], [0])
    return x_walks, y_walks

x_walks, y_walks = get_walks(1000, 10)

x_min = min([min(w) for w in x_walks])
x_max = max([max(w) for w in x_walks])
y_min = min([min(w) for w in y_walks])
y_max = max([max(w) for w in y_walks])



plot = figure(x_range=(x_min, x_max), y_range=(y_min, y_max))
#x_range=(-1*limit, limit), y_range=(-1*limit, limit),plot_height=700, plot_width=700)

source = ColumnDataSource(data={
    'xs' : x_walks[0][:1],
    'ys' : y_walks[0][:1]
})

def update_plot(attr, old, new):
    ind = slider.value

    new_data = {
    'xs' : [w[:ind] for w in x_walks],
    'ys' : [w[:ind] for w in y_walks]
    }
    source.data = new_data

plot.multi_line(xs='xs', ys='ys', alpha=0.2, source=source)


slider = Slider(start=0, end=len(x_walks[0]), step=1, value=0)
slider.on_change('value', update_plot)

layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)

#output_file('random.html')
#show(plot)
