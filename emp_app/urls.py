
from django.urls import path
from emp_app.views import *

urlpatterns = [
    path('index/',index,name='index'),
    path('All_emp/',all_emp,name='all_emp'),
    path('add_emp/',add_emp,name='add_emp'),
    path('remove_emp/',remove_emp,name='remove_emp'),
    path('remove_emp/<int:emp_id>',remove_emp, name='remove_emp'),
    path('Filter_emp/',Filter_emp,name='Filter_emp'),
    

]