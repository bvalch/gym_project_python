from models.member import Member
from models.gymclass import GymClass
from models.gymsession import Gymsession

import repos.member_repo as  member_repo
import repos.gymclass_repo as gymclass_repo
import repos.gymsession_repo as gymsession_repo
import pdb
gymsession_repo.delete_all()
member_repo.delete_all()
gymclass_repo.delete_all()


member1=Member('Shirtless Arnold','male')
member_repo.save(member1)
member2=Member('Rambo of Moria','male')
member_repo.save(member2)
member3=Member('Sonya Blade','female')
member_repo.save(member3)
member4=Member('Ronnie Coleman','male')
member_repo.save(member4)
member5=Member('Condoleezza Rice','female')
member_repo.save(member5)

gymclass1=GymClass('Olympic baby lifting',4)
gymclass_repo.save(gymclass1)

gymclass2=GymClass('Extreme Pilates',3)
gymclass_repo.save(gymclass2)
gymclass3=GymClass('Kangaroo sparring',6)
gymclass_repo.save(gymclass3)

members1=[member1,member2]
members2=[member1,member3,member4]

gymsession1=Gymsession(members1,gymclass1)
gymsession_repo.save(gymsession1)

gymsession2=Gymsession(members2,gymclass2)
gymsession_repo.save(gymsession2)

pdb.set_trace()