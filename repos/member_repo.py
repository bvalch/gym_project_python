from database.run_sql import run_sql

def delete_all():
    sql="DELETE FROM members"
    run_sql(sql)



def save(member):
    sql="INSERT INTO members ( first_name,last_name,sex,wallet) VALUES (%s,%s,%s,%s) RETURNING id"
    values=[member.name,member.sex,member.wallet]
    results=run_sql(sql,values)
    member.id=results[0]['id']