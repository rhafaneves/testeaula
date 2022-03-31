
from pymongo import MongoClient

def printname(rhafa):
    print(rhafa)


def get_database(database):
   client = mongoclient("mongo://localhost:27017")
   #client = mongoclient(database"localhost"port"27017")
   return client(database)

def insert_farm(farm):
    db = get_database("class_19004")

    ret = bd.farms.insert_one(farms)
    returne ret.inserted_id

if __name__ == "__main__":
  #pyton lista,tuplas,dicionarios
  #mongo_json{"field":"valeu"}

  newfarm =(
    "name": "farm`s Python 1"
    "manager": "joao quebra toco"
       )


  id = insert_farm(newfarm)


  print(f"Fazenda inserida. ID:{id}")


