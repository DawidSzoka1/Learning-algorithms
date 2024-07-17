wi1 = {
    'name': 'aSdg',
    'prev': None,
    'next': None,
}

wi2 = {
    'name': 'bcvwsdvf',
    'prev': None,
    'next': None,
}


def add_item_end(my_collection, new_item):
    if not my_collection:
        my_collection = new_item
        new_item['next'] = None
        new_item['prev'] = None
        return my_collection
    item = my_collection
    while item['next']:
        item = item['next']
    item['next'] = new_item
    new_item['prev'] = item
    return my_collection


work = None
work = add_item_end(work, wi1)
work = add_item_end(work, wi2)

item = work
while item:
    print(item['name'])
    item = item['next']


def del_item_begin(my_collection):
    item = my_collection
    if item:
        my_collection = item['next']
        if my_collection:
            my_collection['prev'] = None
    return my_collection, item


wi3 = {
    'name': "4324234",
    'next': None,
    'prev': None
}

work = add_item_end(work, wi3)

# LIFO add_item_begin() and del_item_begin() that's all
