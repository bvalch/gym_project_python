from models.member import Member
from models.gymclass import GymClass
from models.dagym import DaGym

import repos.member_repo as  member_repo
import repos.gymclass_repo as gymclass_repo
import repos.dagym_repo as dagym_repo

member_repo.delete_all()
gymclass_repo.delete_all()
dagym_repo.delete_all()

member1=Member('Arnold Swarzenegger','male')
member_repo.save(member1)
member2=Member('Rambo of Moria','male')
member_repo.save(member2)
member3=Member('Sonya Blade','female')
member_repo.save(member3)
member4=Member('Ronnie Coleman','male')
member_repo.save(member4)
member5=Member('Condoleeza Rice','female')
member_repo.save(member5)

gymclass1=GymClass('Olympic baby lifting',4)
gymclass_repo.save(gymclass1)

gymclass2=GymClass('Extreme Pilates',3)
gymclass_repo.save(gymclass2)
gymclass3=GymClass('Kangaroo sparring',6)
gymclass_repo.save(gymclass3)


dagym1=DaGym(member1,gymclass1)
dagym_repo.save(dagym1)