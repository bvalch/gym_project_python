from database.run_sql import run_sql

def delete_all():
    sql="DELETE FROM gymclasses"
    run_sql(sql)