from mongoengine import Document
from mongoengine.fields import StringField




class Contact(Document):
    first_name = StringField(max_length=50, null=False)
    last_name = StringField(max_length=50, null=False)
    email = StringField(max_length=40, null=True)
    address = StringField(max_length=120, null=True)
    cell_phone = StringField(max_length=30, null=True)
