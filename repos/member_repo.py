from database.run_sql import run_sql

def delete_all():
    sql="DELETE FROM members"
    run_sql(sql)



def save(member):
    sql="INSERT INTO members ( first_name,last_name) VALUES (%s,%s) RETURNING id"
    values=[member.name,member.sex]
    results=run_sql(sql,values)
    member.id=results[0]['id']