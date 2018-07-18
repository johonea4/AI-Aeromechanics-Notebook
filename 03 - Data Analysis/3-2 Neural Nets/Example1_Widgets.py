import ipywidgets as widgets
#Widgets For Interaction
HiddenLayers = widgets.Text(value='4,4') #The result of the algorithm
solutionWidget = widgets.Text() #The result of the algorithm
NumIters = widgets.IntText(value=100000)
countWidget = widgets.IntProgress(value=0, description='Iteration')
runButton = widgets.Button(description='Run Algorithm') #Run the algorithm

bx1 = widgets.HBox([widgets.Label('Hidden Layer Sizes:'),HiddenLayers])
bx2 = widgets.HBox([widgets.Label('Number of Iterations'),NumIters])
bx3 = widgets.HBox([widgets.Label('Current Error:'),solutionWidget])
