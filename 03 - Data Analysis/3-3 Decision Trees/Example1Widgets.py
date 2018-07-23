import ipywidgets as widgets
#Widgets For Interaction
solutionWidget = widgets.Text() #The result of the algorithm
runButton = widgets.Button(description='Run Algorithm') #Run the algorithm

bx1 = widgets.HBox([widgets.Label('Test Result:'),solutionWidget])