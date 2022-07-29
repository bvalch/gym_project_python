from models.member import Member
from models.gymclass import GymClass
from models.dagym import DaGym

import repos.member_repo as  member_repo
import repos.gymclass_repo as gymclass_repo
import repos.dagym_repo as dagym_repo

member_repo.delete_all()
gymclass_repo.delete_all()
dagym_repo.delete_all()

