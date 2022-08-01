from database.run_sql import run_sql
from models.member import Member

def delete_all():
    sql="DELETE FROM members"
    run_sql(sql)


def save(member):
    sql="INSERT INTO members (name, sex,active) VALUES (%s, %s,%s) RETURNING id"
    values=[member.name,member.sex,member.active]
    results=run_sql(sql,values)
    member.id=results[0]['id']
    return member

def select_all():
    sql ="SELECT * FROM members"
    results=run_sql(sql)
    members=[]
    for member in results:
        member=Member(member['name'],member['sex'],member['id'],member['active'])
        members.append(member)
    return members

def select(id):
    sql="SELECT * FROM members where ID = %s"
    values=[id]
    result=run_sql(sql,values)[0]
    member=Member(result['name'],result['sex'],result['id'],result['active'])
    return member

def update(member):
    sql="UPDATE members SET (name,sex) = (%s,%s) WHERE id = %s"
    values=[member.name,member.sex,member.active,member.id]
    run_sql(sql,values)

def update_deactivate(member):
    sql="UPDATE members SET active=NOT active  WHERE id = %s"
    values=[member.id]
    run_sql(sql,values)
