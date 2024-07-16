plan_list = [
    {'hour': '9:00', 'teacher': 'Wirus', 'lecture': 'Mikrobiologii'},
    {'hour': '12:00', 'teacher': 'kolba', 'lecture': 'Chemii'},
    {'hour': '14:00', 'teacher': 'Olej', 'lecture': 'Etyka'},
]

plan_dict = {
    'Mikrobiologii': plan_list[0],
    'Chamii': plan_list[1],
    'Etyka': plan_list[2],
}

for plan in plan_list:
    print(plan['hour'], " ", plan['lecture'])

for k, v in plan_dict.items():
    print(v['hour'], " ", k)
