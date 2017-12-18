import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, output_file, curdoc, save
from bokeh.models import ColumnDataSource, Slider, Select, Range1d
from bokeh.layouts import row, column, widgetbox
from bokeh.palettes import inferno
from bokeh.resources import CDN
from bokeh.embed import components


#Create steps in a loop and append them to our arrays
def get_walks(n_walks, walk_length):
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

x_walks, y_walks = get_walks(10, 100)

x_min = min([min(w) for w in x_walks])
x_max = max([max(w) for w in x_walks])
y_min = min([min(w) for w in y_walks])
y_max = max([max(w) for w in y_walks])

colors = [np.random.choice(inferno(100)) for x in x_walks]

plot = figure(x_range=(x_min, x_max), y_range=(y_min, y_max), plot_height=500, plot_width=500)


def update_plot(attr, old, new):
    ind = slider.value

    new_data = {
    'xs' : [w[:ind] for w in x_walks],
    'ys' : [w[:ind] for w in y_walks],
    'colors': colors
    }
    source.data = new_data

def update_menu(attr, old, new):
    new_n_walks = int(menu1.value)
    new_walk_length = int(menu2.value)
    global x_walks
    global y_walks
    global colors
    x_walks, y_walks = get_walks(new_n_walks, new_walk_length)

    x_min = min([min(w) for w in x_walks])
    x_max = max([max(w) for w in x_walks])
    y_min = min([min(w) for w in y_walks])
    y_max = max([max(w) for w in y_walks])
    colors = [np.random.choice(inferno(100)) for w in x_walks]

    new_data = {
    'xs' : x_walks,
    'ys' : y_walks,
    'colors' : colors
    }
    source.data = new_data
    plot.x_range.start = x_min
    plot.x_range.end = x_max
    plot.y_range.start = y_min
    plot.y_range.end = y_max
    slider.end = new_walk_length


source = ColumnDataSource(data={
    'xs' : x_walks,
    'ys' : y_walks,
    'colors' : colors
})

plot.multi_line(xs='xs', ys='ys', alpha=0.4, line_color='colors', line_width=3, source=source)


slider = Slider(start=0, end=len(x_walks[0]), step=1, value=0)
slider.on_change('value', update_plot)

menu1 = Select(options=['1', '10', '100'], value='10', title='Number of Walks')
menu1.on_change('value', update_menu)

menu2 = Select(options=['10', '100', '1000', '2000'], value='100', title='Length of Walks')
menu2.on_change('value', update_menu)

layout = column(widgetbox(menu1, menu2, slider), plot)
curdoc().add_root(layout)

#script, div = components(layout)
#print(script)
#print(div)
#output_file('random.html')
#save(layout)

#show(plot)
