from Users.viewsets import  AddViewSets
from rest_framework import routers
from Role.viewsets import RoleViewSets
from Questions.viewsets import QuesViewsets
#from Questions.views import Question_list
#from quiz.Questions.views import Question_list

router=routers.DefaultRouter()
router.register('Users',AddViewSets)
router.register('Questions', QuesViewsets)
router.register('Role',RoleViewSets)
#router.register('All_Question',Question_list)