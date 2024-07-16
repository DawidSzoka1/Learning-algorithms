def del_item_begin(my_collection):
    next_val = my_collection['next']
    next_val['prev'] = None
    return next_val


def del_item_end(my_collection):
    item = my_collection
    while item['next']:
        item = item['next']
    new_last = item['prev']
    new_last['next'] = None
