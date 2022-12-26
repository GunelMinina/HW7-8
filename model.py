import config
import os

db = []

def is_db_exist():
    return os.path.exists(config.path_db)

def init_db():
    #Если файла нет, создаем
    if (not is_db_exist()):
        open(config.path_db, "w", encoding="utf8")
    db_load()

def db_save(): 
    open(config.path_db, 'w+', encoding="utf8").writelines((f"{row['id']},{row['lastname']},{row['firstname']},{row['phone']}\n" for row in db))

def split_string(str):
    data = str.split(',')
    db.append({
        'id': data[0],
        'lastname': data[1], 
        'firstname': data[2], 
        'phone': data[3], 
    })

def db_load():
    lines = open(config.path_db,'r', encoding="utf8").read().splitlines()
    db = list(map(split_string, lines))

def insert_row(row):
    try:
        row['id'] = len(db) + 1
        db.append(row)
        db_save()
        return row
    except ValueError:        
        return False

def find_by_id(id):
    for i in range(0, len(db)):
        if (db[i]['id'] == id):
            return db[i]
    return

def update(id, data):
    for i in range(0, len(db)):
        if (db[i]['id'] == id):
            db[i] = data
            db[i]['id'] = id
    db_save()
    
def get_all():
    return db

def find(str):
    result = []
    for i in range(0, len(db)):
        if (str.lower() in db[i]['firstname'].lower() or str.lower() in db[i]['lastname'].lower() or str.lower() in db[i]['phone'].lower()):
            result.append(db[i])
    return result