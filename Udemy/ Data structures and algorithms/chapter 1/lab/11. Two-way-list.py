wi1 = {
    'name': 'aSdg',
    'start_hour': 8,
    'duration_min': 15,
    'prev': None,
    'next': None,
}

wi2 = {
    'name': 'bcvwsdvf',
    'start_hour': 9,
    'duration_min': 60,
    'prev': None,
    'next': None,
}

wi3 = dict(name='gfdbvc', start_hour=12, duration_min=120, prev=None, next=None)

wi1['next'] = wi2
wi2['next'] = wi3
wi2['prev'] = wi1
wi3['prev'] = wi2

work = wi1

item = work

while item:
    print(item['name'])
    item = item['next']


def add_item_begin(my_collection, new_item):
    new_item['next'] = my_collection
    new_item['prev'] = None

    if my_collection:
        my_collection['prev'] = new_item

    return new_item


def add_item_end(my_collection, new_item):
    item = my_collection
    while item['next']:
        item = item['next']
    item['next'] = new_item
    new_item['prev'] = item
    return my_collection
