import ipywidgets as widgets

#Widgets
NumSensors = widgets.IntSlider(value=2,min=2,max=20,step=1)
NumModes = widgets.IntSlider(value=3,min=2,max=20,step=1)
NumRows = widgets.IntSlider(value=20,min=10,max=2000,step=1)
NumCols = widgets.IntSlider(value=20,min=10,max=2000,step=1)
Decrement = widgets.FloatSlider(value=0.2,min=0.01,max=0.9,step=0.01)
runButton2 = widgets.Button(description='Run Algorithm')
bx1 = widgets.HBox([widgets.Label('Number of Sensors:'),NumSensors])
bx2 = widgets.HBox([widgets.Label('Number of Modes:'),NumModes])
bx3 = widgets.HBox([widgets.Label('Number of Rows:'),NumRows])
bx4 = widgets.HBox([widgets.Label('Number of Columns:'),NumCols])
bx5 = widgets.HBox([widgets.Label('Decrement:'),Decrement])
means = widgets.Text(description='Result Means')