ben = {
    'name': 'Ben',
    'phone': '123',
    'email': 'ben@gas.com'
}

jan = {
    'name': 'Jan',
    'phone': '123233',
    'email': 'jan@gas.com'
}

ann = {
    'name': 'Ann',
    'phone': '125453',
    'email': 'ann@gas.com'
}

contact_list = [ben, jan, ann]

all_emails = ''

for c in contact_list:
    all_emails += c['email'] + '; '

# print(all_emails)

contact_dict = {}

for c in contact_list:
    contact_dict[c['name']] = c
