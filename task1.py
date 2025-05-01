from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value

model = LpProblem(name="production-optimization", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat='Integer')
juice = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

model += lemonade + juice, "Total_Production"

# 1. Вода: 2 од. на лимонад, 1 од. на сік (максимум 100)
model += 2 * lemonade + 1 * juice <= 100, "Water"

# 2. Цукор: 1 од. на лимонад (максимум 50)
model += 1 * lemonade <= 50, "Sugar"

# 3. Лимонний сік: 1 од. на лимонад (максимум 30)
model += 1 * lemonade <= 30, "Lemon_Juice"

# 4. Фруктове пюре: 2 од. на сік (максимум 40)
model += 2 * juice <= 40, "Fruit_Puree"

model.solve()

print("=== Завдання 1 ===")
print(f"Статус: {LpStatus[model.status]}")
print(f"Кількість лимонаду: {lemonade.value()} од.")
print(f"Кількість фруктового соку: {juice.value()} од.")
print(f"Загальна кількість напоїв: {value(model.objective)} од.")
