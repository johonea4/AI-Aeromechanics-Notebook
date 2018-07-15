import ipywidgets as widgets

#Create Widgets for simple use
PopulationSize = widgets.IntSlider(value=100,min=20,max=2000,step=1)
NumGenerations = widgets.IntSlider(value=1000,min=100,max=10000,step=1)
MutationProbability = widgets.IntSlider(value=20,min=0,max=100,step=1)
countWidget = widgets.IntProgress(value=0, description='Generation')
solutionWidget = widgets.Text(description='Best')
runButton = widgets.Button(description='Run Algorithm')

bx1 = widgets.HBox([widgets.Label('Population Size:'),PopulationSize])
bx2 = widgets.HBox([widgets.Label('Number of Generations:'),NumGenerations])
bx3 = widgets.HBox([widgets.Label('Mutation Probability:'),MutationProbability])