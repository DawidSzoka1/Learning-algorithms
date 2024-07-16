names = ['John Johnson', 'Alicja Policja', 'Wladimir Wladymirowicz']


def get_sub_name(name: str, part: int) -> str:
    return name.split(' ')[part]


first_names = [get_sub_name(name, 0) for name in names]
last_names = [get_sub_name(name, 1) for name in names]
print(first_names)
print(last_names)

labda_first_names = [(lambda name, part: name.split(' ')[part])(name, 0) for name in names]
generator_first_names = [name.split(' ')[0] for name in names]

