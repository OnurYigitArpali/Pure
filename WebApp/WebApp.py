from flask import Flask, render_template, request
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

from bokeh.models import Plot, GraphRenderer, StaticLayoutProvider, Oval, TapTool, BoxSelectTool, Arrow, OpenHead
from bokeh.palettes import Spectral8
from bokeh.models.graphs import NodesAndLinkedEdges
from bokeh.models.callbacks import CustomJS
from bokeh.models.ranges import Range1d

app = Flask(__name__)

# Load the Iris Data Set
iris_df = pd.read_csv("data/iris.data",
                      names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
feature_names = iris_df.columns[0:-1].values.tolist()


# Create the main plot
def create_figure(current_feature_name, bins):
    #p = figure(plot_width=600, plot_height=400)
    #p.vbar(x = "asd")
#     p = Histogram(iris_df, current_feature_name, title=current_feature_name, color='Species',
#                   bins=bins, legend='top_right', width=600, height=400)
#    
#     # Set the x axis label
#     p.xaxis.axis_label = current_feature_name
#    
#     # Set the y axis label
#     p.yaxis.axis_label = 'Count'
    p = figure(plot_width=400, plot_height=400)
    
    # add a circle renderer with a size, color, and alpha
    p.circle([1, 2], [1, 2], size=60, color="navy", alpha=1)
    p.add_layout(Arrow(line_color="red", end=OpenHead(line_color="red", line_width=2),
                   x_start=2, y_start=2, x_end=1, y_end=1))


    return p
# Index page
@app.route('/')
def index():
    # Determine the selected feature
    current_feature_name = request.args.get("feature_name")
    if current_feature_name == None:
        current_feature_name = "Sepal Length"

    # Create the plot
    plot = create_figure(current_feature_name, 5)

    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template("index.html", script=script, div=div,
                           feature_names=feature_names, current_feature_name=current_feature_name)


# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)
