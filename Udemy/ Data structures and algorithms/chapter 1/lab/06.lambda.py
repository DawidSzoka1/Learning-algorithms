my_list = list(range(10))


def fun_square(x):
    return x * x


new_list = [fun_square(x) for x in my_list]

map_list = list(map(lambda x: x*x, my_list))

print(new_list)
print(map_list)

print([(lambda x: x*x)(x) for x in my_list])
