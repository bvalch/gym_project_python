from database.run_sql import run_sql

def delete_all():
    sql="DELETE FROM gymclasses"
    run_sql(sql)


def save(gymclass):
    sql="INSERT INTO gymclasses(name,capacity) VALUES ( %s,%s) RETURNING id"
    values=[gymclass.name,gymclass.capacity]
    result=run_sql(sql,values)
    gymclass.id=result[0]['id']
    
