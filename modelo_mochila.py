import pyomo.environ as pe

model = pe.AbstractModel()

# Datos de forma abstracta (como conjuntos y parámetros)
model.ITEMS = pe.Set()
model.v = pe.Param( model.ITEMS, within=pe.PositiveReals )
model.w = pe.Param( model.ITEMS, within=pe.PositiveReals )
model.W_max = pe.Param( within=pe.PositiveReals )

# Variables
model.x = pe.Var( model.ITEMS, within=pe.Binary )

# Función objetivo
def value_rule(model):
    return sum( model.v[i]*model.x[i] for i in model.ITEMS )
model.value = pe.Objective( rule=value_rule, sense=pe.maximize )

# Restricción
def weight_rule(model):
    return sum( model.w[i]*model.x[i] for i in model.ITEMS )<= model.W_max
model.weight = pe.Constraint( rule=weight_rule )