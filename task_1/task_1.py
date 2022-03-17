import os
from os.path import join
my_project = "my_project"
settings = "settings"
mainapp = "mainapp"
adminapp = "adminapp"
authapp = "authapp"

path1 = join(".", my_project)
os.makedirs(path1,exist_ok=True)
path2 = join( my_project, settings)
os.makedirs(path2,exist_ok=True)
path3 = join( my_project, mainapp)
os.makedirs(path3,exist_ok=True)
path4 = join( my_project, adminapp)
os.makedirs(path4,exist_ok=True)
path5 = join( my_project, authapp)
os.makedirs(path5,exist_ok=True)