import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

def add_arrow_to_line2D(
    axes, line, arrow_locs=[0.2, 0.4, 0.6, 0.8],
    arrowstyle='-|>', arrowsize=1, transform=None):
    """
    Add arrows to a matplotlib.lines.Line2D at selected locations.

    Parameters:
    -----------
    axes: 
    line: Line2D object as returned by plot command
    arrow_locs: list of locations where to insert arrows, % of total length
    arrowstyle: style of the arrow
    arrowsize: size of the arrow
    transform: a matplotlib transform instance, default to data coordinates

    Returns:
    --------
    arrows: list of arrows
    """
    if not isinstance(line, mlines.Line2D):
        raise ValueError("expected a matplotlib.lines.Line2D object")
    x, y = line.get_xdata(), line.get_ydata()

    arrow_kw = {
        "arrowstyle": arrowstyle,
        "mutation_scale": 10 * arrowsize,
    }

    color = line.get_color()
    use_multicolor_lines = isinstance(color, np.ndarray)
    if use_multicolor_lines:
        raise NotImplementedError("multicolor lines not supported")
    else:
        arrow_kw['color'] = color

    linewidth = line.get_linewidth()
    if isinstance(linewidth, np.ndarray):
        raise NotImplementedError("multiwidth lines not supported")
    else:
        arrow_kw['linewidth'] = linewidth

    if transform is None:
        transform = axes.transData

    arrows = []
    for loc in arrow_locs:
        s = np.cumsum(np.sqrt(np.diff(x) ** 2 + np.diff(y) ** 2))
        n = np.searchsorted(s, s[-1] * loc)
        arrow_tail = (x[n], y[n])
        arrow_head = (np.mean(x[n:n + 2]), np.mean(y[n:n + 2]))
        p = mpatches.FancyArrowPatch(
            arrow_tail, arrow_head, transform=transform,
            **arrow_kw)
        axes.add_patch(p)
        arrows.append(p)
    return arrows

fig1 = plt.figure(figsize=[6.4,2.0])
ax1 = plt.axes(frameon=False)

ax1.axis([-3,3,-1,1])
ax1.get_xaxis().tick_bottom()
ax1.axes.get_yaxis().set_visible(False)

xmin, xmax = ax1.get_xaxis().get_view_interval()
ymin, ymax = ax1.get_yaxis().get_view_interval()

arrowdensity = 3

x1 = np.linspace(-3,-1,500)
y1 = np.zeros_like(x1)
l1 = mlines.Line2D(x1,y1)
x2 = np.linspace(-1,0,300)
y2 = np.zeros_like(x2)
l2 = mlines.Line2D(x2,y2)
x3 = np.linspace(0,3,500)
y3 = np.zeros_like(x3)
l3 = mlines.Line2D(x3,y3)

add_arrow_to_line2D(ax1, l1, arrow_locs=np.linspace(0.1,0.9,arrowdensity*2), arrowstyle='->', arrowsize=2)
add_arrow_to_line2D(ax1, l2, arrow_locs=np.linspace(0.1,0.9,arrowdensity*1,endpoint=False), arrowstyle='<-', arrowsize=2)
add_arrow_to_line2D(ax1, l3, arrow_locs=np.linspace(0.1,1.0,arrowdensity*3), arrowstyle='->', arrowsize=2)

ax1.add_line(l1)
ax1.add_line(l2)
ax1.add_line(l3)
ax1.plot([-1,0],[0,0],'go')

plt.show()
