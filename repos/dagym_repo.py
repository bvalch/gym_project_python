from database.run_sql import run_sql
from models.gymclass import GymClass
from models.member import Member


def delete_all():
    sql="DELETE FROM dagym"
    run_sql(sql)