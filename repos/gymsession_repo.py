from database.run_sql import run_sql
from models.gymclass import GymClass
from models.member import Member
from models.gymsession import Gymsession


def delete_all():
    sql="DELETE FROM gymsessions"
    run_sql(sql)

def save(gymsession):
    sql="INSERT INTO gymsessions (member_id,gymclass_id) VALUES (%s,%s) RETURNING id"
    values=[gymsession.member.id, gymsession.gymclass.id]
    result=run_sql(sql,values)
    gymsession.id=result[0]['id']



