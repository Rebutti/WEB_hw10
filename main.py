import argparse
from functools import wraps

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://rebutti:N2EzP4sqlfYE9sJi@cluster0.ugu4kvv.mongodb.net/?retryWrites=true&w=majority")
db = client.contacts

parser = argparse.ArgumentParser(description='Contacts')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--first_name')
parser.add_argument('--last_name')
parser.add_argument('--email')
parser.add_argument('--cell_phone')
parser.add_argument('--address', nargs='+')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
first_name = my_arg.get('first_name')
last_name = my_arg.get('last_name')
email = my_arg.get('email')
cell_phone = my_arg.get('cell_phone')
address = my_arg.get('address')
_id = my_arg.get('id')


class ExceptionValidation(Exception):
    pass


def validate(func):
    @wraps(func)
    def wrapper(*args):
        for el in args:
            if el is None:
                raise ExceptionValidation(f'Вхідні данні не валідні: {func.__name__}{args}')
        result = func(*args)
        return result

    return wrapper


def find_by_id(_id):
    result = db.contacts.find_one({"_id": ObjectId(_id)})
    return result


@validate
def create(first_name, last_name, cell_phone, email, address):
    result = db.contacts.insert_one({
        "first_name": first_name,
        "last_name": last_name,
        "cell_phone": cell_phone,
        "email": email,
        "address": address,
    })
    return find_by_id(result.inserted_id)


@validate
def find():
    return db.contacts.find()


@validate
def update(_id, first_name, last_name, cell_phone, email, address):
    r = db.contacts.update_one({"_id": ObjectId(_id)}, {
        "$set": {
            "first_name": first_name,
            "last_name": last_name,
            "cell_phone": cell_phone,
            "email": email,
            "address": address,
        }
    })
    print(r)
    return find_by_id(_id)


@validate
def remove(_id):
    r = db.contacts.delete_one({"_id": ObjectId(_id)})
    return r


def main():
    try:
        match action:
            case 'create':
                r = create(first_name, last_name, cell_phone, email, address)
                print(r)
            case 'find':
                r = find()
                [print(el) for el in r]
            case 'update':
                r = update(_id, first_name, last_name, cell_phone, email, address)
                print(r)
            case 'remove':
                r = remove(_id)
                print(r)
            case _:
                print('Unknowns command')
    except ExceptionValidation as err:
        print(err)


if __name__ == '__main__':
    main()
    # print(find_by_id('6318d73f74bc292c95cdaa3d'))