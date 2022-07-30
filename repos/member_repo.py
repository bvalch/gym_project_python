from database.run_sql import run_sql
from models.member import Member

def delete_all():
    sql="DELETE FROM members"
    run_sql(sql)


def save(member):
    sql="INSERT INTO members (name, sex) VALUES (%s, %s) RETURNING id"
    values=[member.name,member.sex]
    results=run_sql(sql,values)
    member.id=results[0]['id']
    return member

def select_all():
    sql ="SELECT * FROM members"
    results=run_sql(sql)
    members=[]
    for member in results:
        member=Member(member['name'],member['sex'],member['id'])
        members.append(member)
    return members