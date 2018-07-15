import ipywidgets as widgets

#Model Settings
NumNodes = widgets.IntSlider(value=1000,min=1000,max=1000000,step=100)
NumDynamic = widgets.IntSlider(value=3,min=1,max=100,step=1)
NumSensors = widgets.IntSlider(value=2,min=1,max=10,step=1)
#Algorithm Settings
pSize = widgets.IntSlider(value=100,min=20,max=2000,step=1)
nGenerations = widgets.IntSlider(value=500,min=100,max=10000,step=1)
mProb = widgets.IntSlider(value=20,min=0,max=100,step=1)
Objective = widgets.FloatSlider(value=0.3,min=0.01,max=1.0,step=0.01)
countOut = widgets.IntProgress(value=0, description='Generation')
solutionOut = widgets.Text(description='Best')
coverageOut = widgets.Text(description='Coverage')
optimize = widgets.Button(description='Run Algorithm')

bx1 = widgets.HBox([widgets.Label('Number of Nodes'),NumNodes])
bx2 = widgets.HBox([widgets.Label('Number of Dynamic Modes:'),NumDynamic])
bx3 = widgets.HBox([widgets.Label('Number of Sensors'),NumSensors])
bx4 = widgets.HBox([widgets.Label('Population Size:'),pSize])
bx5 = widgets.HBox([widgets.Label('Number of Generations:'),nGenerations])
bx6 = widgets.HBox([widgets.Label('Mutation Probability:'),mProb])
bx7 = widgets.HBox([widgets.Label('Minimum Amplitude Ratio:'),Objective])