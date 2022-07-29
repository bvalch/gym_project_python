from database.run_sql import run_sql

def delete_all():
    sql="DELETE FROM gymclasses"
    run_sql(sql)


def save(gymclass):
    sql="INSERT INTO gymclasses(name,price,capacity,runtime) VALUES ( %s,%s,%s,%s) RETURNING id"
    values=[gymclass.name,gymclass.price,gymclass.capacity,gymclass.runtime]
    result=run_sql(sql,values)
    gymclass.id=result[0]['id']
    
