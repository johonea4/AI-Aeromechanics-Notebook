import ipywidgets as widgets
#Widgets For Interaction
R_Start = widgets.BoundedFloatText(value=0.6, min=0, max=1) #Probability of starting with Rain
R_Transition = widgets.BoundedFloatText(value=0.7,min=0,max=1) #Probability of staying in Rain State
S_Transition = widgets.BoundedFloatText(value=0.6,min=0,max=1) #Probability of staying in Sunny State
R_Walk = widgets.BoundedFloatText(value=0.1,min=0,max=1) #Probability of Walking when Raining
R_Shop = widgets.BoundedFloatText(value=0.4,min=0,max=1) #Probability of Shopping when raining
R_Clean = widgets.BoundedFloatText(value=0.5,min=0,max=1) #Probability of cleaning when raining
S_Walk = widgets.BoundedFloatText(value=0.6,min=0,max=1) #Probability of Walking when Sunny
S_Shop = widgets.BoundedFloatText(value=0.3,min=0,max=1) #Probability of Shopping when Sunny
S_Clean = widgets.BoundedFloatText(value=0.1,min=0,max=1) #Probability of cleaning when Sunny
Observations = widgets.Text(value='walk,shop,clean') #The result of the algorithm
solutionWidget = widgets.Text() #The result of the algorithm
runButton = widgets.Button(description='Run Algorithm') #Run the algorithm

bx1 = widgets.HBox([widgets.Label('Probability of starting with Rain:'),R_Start])
bx2 = widgets.HBox([widgets.Label('Probability of staying in Rain State:'),R_Transition])
bx3 = widgets.HBox([widgets.Label('Probability of staying in Sunny State:'),S_Transition])
bx4 = widgets.HBox([widgets.Label('Probability of Walking when Raining:'),R_Walk])
bx5 = widgets.HBox([widgets.Label('Probability of Shopping when Raining:'),R_Shop])
bx6 = widgets.HBox([widgets.Label('Probability of cleaning when Raining:'),R_Clean])
bx7 = widgets.HBox([widgets.Label('Probability of Walking when Sunny:'),S_Walk])
bx8 = widgets.HBox([widgets.Label('Probability of Shopping when Sunny:'),S_Shop])
bx9 = widgets.HBox([widgets.Label('Probability of cleaning when Sunny:'),S_Clean])
bx10 = widgets.HBox([widgets.Label('Observations:'),Observations])
bx11 = widgets.HBox([widgets.Label('Inferred States:'),solutionWidget])
