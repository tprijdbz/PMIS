

'''
import pymongo
import mongoengine

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient)
mydb = myclient["jiekxueyuan"]
print(mydb)
'''

from mongoengine import *

connect('jikexueyuan')

class People(Document):
    pid = StringField(required=True)
    name = StringField(required=True)
    age = IntField(required=True)
    sex = StringField(required=True)
    salary = IntField()

'''
kingname = People(name = 'kingname', age = 22, sex = 'male', salary = 999999)
kingname.save()

jike = People(name = 'jike', age = 5, sex = 'unknown', salary = 1)
jike.save()

amei = People(name = 'amei', age = 25, sex = 'female', salary = 8888)
amei.save()

ameili = People(name = 'ameili', age = 18, sex = 'female', salary = 6867564)
ameili.save()
'''

namelist = People.objects(sex = 'female')
print(namelist)
for x in namelist:
    print(x)
    print(x.name)
