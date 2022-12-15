from ortools.sat.python import cp_model

#se declara el modelo cp_model
model = cp_model.CpModel()

#El solucionador crea tres variables, x, y y z, cada una de las 
# cuales puede tomar los valores 0, 1 o 2.
num_vals = 3
x = model.NewIntVar(0, num_vals - 1, 'x')
y = model.NewIntVar(0, num_vals - 1, 'y')
z = model.NewIntVar(0, num_vals - 1, 'z')

#El siguiente código crea la restricción x ≠ y 
model.Add(x != y)

