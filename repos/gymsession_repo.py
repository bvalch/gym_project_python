from database.run_sql import run_sql
from models.gymclass import GymClass
from models.member import Member
from models.gymsession import Gymsession
import repos.gymclass_repo as gymclass_repo
import repos.member_repo as member_repo


def delete_all():
    sql="DELETE FROM gymsessions"
    run_sql(sql)

def save(gymsession):
    for member in gymsession.member:
        sql="INSERT INTO gymsessions(member_id,gymclass_id) VALUES (%s, %s) RETURNING id"
        values=[member.id,gymsession.gymclass.id]
        result=run_sql(sql,values)
    gymsession.id=result[0]["id"]

def select_all():
    sql="SELECT * FROM gymsessions"
    results=run_sql(sql)
    gymsessions=[]
    for result in results:
        member=member_repo.select(result["member_id"])
        gymclass=gymclass_repo.select(result["gymclass_id"])
        gymsession=Gymsession(member,gymclass,result["id"])
        gymsessions.append(gymsession)
    return gymsessions

 

def show_attendees(class_id):
    attendees=[]
    sql="SELECT members.* FROM members INNER JOIN gymsessions ON gymsessions.member_id = members.id WHERE gymsessions.gymclass_id =%s"
    values=(class_id)
    results=run_sql(sql,values)
    for item in results:
        attendees.append(item['name'])
    return attendees

def get_capacity(class_id,members_list):
    sql="SELECT members.* from members INNER JOIN gymsessions ON gymsessions.member_id =members.id WHERE gymsessions.gymclass_id = %s"
    values=(class_id)
    results=run_sql(sql,values)
    gymclass=gymclass_repo.select(class_id)
    if len(results)+len(members_list)<=gymclass.capacity:
    
        return True
    else:
         return False

   