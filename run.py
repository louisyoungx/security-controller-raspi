import os

def Do(cmd):
    os.system(str(cmd))

Do('nohup python3 utils/sunny.py &')

Do('python3 manage.py runserver 127.0.0.1:8011')



