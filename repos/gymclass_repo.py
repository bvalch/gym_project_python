from database.run_sql import run_sql
from models.gymclass import GymClass

def delete_all():
    sql="DELETE FROM gymclasses"
    run_sql(sql)


def save(gymclass):
    sql="INSERT INTO gymclasses(name,capacity) VALUES ( %s,%s) RETURNING id"
    values=[gymclass.name,gymclass.capacity]
    result=run_sql(sql,values)
    gymclass.id=result[0]['id']
    return gymclass

def select_all():
    sql="SELECT * FROM gymclasses"
    result=run_sql(sql)
    gymclasses=[]
    for item in result:
        gymclass=GymClass(item['name'],item['capacity'],item['id'])
        gymclasses.append(gymclass)
    return gymclasses
    
def select(id):
    sql="SELECT * FROM gymclasses WHERE id=%s"
    values=[id]
    results=run_sql(sql,values)[0]
    gymclass=GymClass(results['name'],results['capacity'])
    return gymclass