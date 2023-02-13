from django.urls import path
from . views import *
urlpatterns = [
    path("",home),
    path("std/home/",home),
    path("std/add_std/",std_add),
    path("std/delete_std/<int:roll>",delete_std),
    path("std/update_std/<int:roll>",update_std),
    path("std/do_update_std/<int:roll>",do_update_std),
    

]
