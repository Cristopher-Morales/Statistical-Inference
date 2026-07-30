import matplotlib.pyplot as plt
import os

def single_plot(x, y, **kwargs):
    title  = kwargs.pop( 'title' , 'Title' )
    xlabel = kwargs.pop( 'xlabel', 'x-axis')
    ylabel = kwargs.pop( 'ylabel', 'y_axis' )
    marker = kwargs.pop( 'marker', 'go')
    '''defaul values for marker size, figure size, font size and legend'''
    marker_size = 4
    fig_size = (8,6)
    font_size = 12
    legend_location = 'upper right'
    if kwargs.get( 'figure_size' ) is not None:
        fig_size = kwargs.pop( 'figure_size' )
    if kwargs.get( 'marker_size' )  is not None:
        marker_size = kwargs.pop( 'marker_size' )
    if kwargs.get( 'font_size' ) is not None:
        font_size = kwargs.pop( 'font_size')
    if kwargs.get( 'legend_location' ) is not None:
        legend_location=str(kwargs.pop( 'legend_location'))
    plt.rcParams['font.size'] = font_size
    plt.figure(figsize=fig_size)
    plt.plot(x, y, marker,markersize=marker_size, label=title)
    plt.legend(loc=legend_location)
    fig = plt.gcf()
    axis = None
    for axis in fig.axes:
        axis.xaxis.set_label_text( xlabel )
        axis.yaxis.set_label_text( ylabel )
    if kwargs.get( 'x_limits' )is not None:
        plt.xlim(kwargs.pop( 'x_limits'))
    if kwargs.get( 'y_limits' )is not None:
        plt.ylim(kwargs.pop( 'y_limits'))
    if kwargs.get( 'save_figure' )is not None:
        if kwargs.pop( 'save_figure' ) == 'yes':
            figure_name = 'figure_plot'
            if kwargs.get( 'figure_name') is not None:
                figure_name = kwargs.pop( 'figure_name' )
            fig.savefig(os.getcwd()+'/Pictures/'+figure_name+'.pdf', format='pdf',transparent=False,bbox_inches="tight", dpi=1400)
    return axis

def multi_plot(plots,**kwargs):
    xlabel = kwargs.pop( 'xlabel', 'Inputs' )
    ylabel = kwargs.pop( 'ylabel', 'Targets' )
    '''defaul values for marker size, figure size, font size and legend'''
    marker_size = 4
    fig_size = (8,6)
    font_size = 12
    legend_location = 'upper right'
    if kwargs.get( 'figure_size' ) is not None:
        fig_size = kwargs.pop( 'figure_size' )
    if kwargs.get( 'marker_size' )  is not None:
        marker_size = kwargs.pop( 'marker_size' )
    if kwargs.get( 'font_size' ) is not None:
        font_size = kwargs.pop( 'font_size')
    if kwargs.get( 'legend_location' ) is not None:
        legend_location=str(kwargs.pop( 'legend_location'))
    plt.figure(figsize=fig_size)
    plt.rcParams['font.size'] = str(font_size)
    for plot in tuple(plots):
        tuple(plot[0])
        plt.plot(plot[0], plot[1], plot[2],markersize=marker_size, label=plot[3])
        plt.legend(loc=legend_location)
    fig = plt.gcf()
    for axis in fig.axes:
        axis.xaxis.set_label_text( xlabel )
        axis.yaxis.set_label_text( ylabel )
    if kwargs.get( 'x_limits' )is not None:
        plt.xlim(kwargs.pop( 'x_limits'))
    if kwargs.get( 'y_limits' )is not None:
        plt.ylim(kwargs.pop( 'y_limits'))
    if kwargs.get( 'y_scale' )is not None:
        plt.yscale(kwargs.pop( 'y_scale' ))
    if kwargs.get( 'x_scale' )is not None:
        plt.xscale(kwargs.pop( 'x_scale' ))
    plt.show()
    if kwargs.get( 'save_figure' )is not None:
        if kwargs.pop( 'save_figure' ) == 'yes':
            figure_name = 'figure_plot'
            if kwargs.get( 'figure_name') is not None:
                figure_name = kwargs.pop( 'figure_name' )
            fig.savefig(os.getcwd()+'/Pictures/'+figure_name+'.pdf', format='pdf',transparent=False,bbox_inches="tight", dpi=1200)