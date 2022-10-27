from mongoengine import connect
import configparser

from pymongo import MongoClient

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# # connect to cluster on AtlasDB with connection string

# connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}.ugu4kvv.mongodb.net/{db_name}?retryWrites=true&w=majority""")
# # connect(host=f"""mongodb+srv://rebutti:{mongodb_pass}@cluster0.ugu4kvv.mongodb.net/?retryWrites=true&w=majority""")

client = MongoClient(
    "mongodb+srv://rebutti:N2EzP4sqlfYE9sJi@cluster0.ugu4kvv.mongodb.net/?retryWrites=true&w=majority"
)

db = client.contacts

# result_one = db.contacts.insert_one(
#     {
#         "first_name": "barsik",
#         "last_name": "Popov",
#         "cell_phone": "38050482563",
#     }
# )

# print(result_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "first_name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)