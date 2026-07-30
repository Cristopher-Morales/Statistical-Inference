from plots import *
from polynomial_model import *

# Small example how to use polynomial fitting class

# define polynomial model
model_1=PolynomialModel(2)
# define input and target
x=[1, 2, 3, 4, 5,6,7]
y=[50,55,65,80,110,150,200]
# set data in the model
model_1.set_data(x,y)
# fit polynomial model
model_1.fit_model()
# Test polynomial model computing predicted values
y_outputs=model_1.predict(x)

# Plot results
# define labels for each plot
label_1 = "Target value"
label_2 = "Predicted value"
# introduce x and y axis labels
xlabel='Input[-]'
ylabel= "Target[-]"
# define markers for each plot
marker_1= 'go'
marker_2= 'rx'

# gather inputs, outputs, markers and labels in lists
x_s=[x,x]
y_s=[y,y_outputs]
markers=[marker_1,marker_2]
labels=[label_1,label_2]
# zip the list of inputs, targets, markers and labels used in the plot.
plots=zip(x_s,y_s,markers,labels)

# define figure variables to be used in creating the plots,
# if some of them are not giving, defaults value are going to be used
figure_name='plot_comparison'
figure_size=(8,6)
marker_size = 4
font_size = 14
legend_location='upper left'
# define plot configuration
plot_config= {'xlabel': xlabel, 'ylabel': ylabel, 'marker_size': marker_size,\
              'figure_size': figure_size, 'font_size': font_size, 'save_figure': 'no',\
              'figure_name': figure_name, 'legend_location': legend_location}

# plot results
multi_plot(plots, **plot_config)