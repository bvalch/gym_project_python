from database.run_sql import run_sql
from models.gymclass import GymClass
from models.member import Member
from models.dagym import DaGym


def delete_all():
    sql="DELETE FROM dagym"
    run_sql(sql)

def save(dagym):
    sql="INSERT INTO dagym (member_id,gymclass_id) VALUES (%s,%s) RETURNING id"
    values=[dagym.member.id, dagym.gymclass.id]
    result=run_sql(sql,values)
    dagym.id=result[0]['id']
