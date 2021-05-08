import os
from webdav4.client import Client
from Django_Admin.settings import BASE_DIR
# /home/pi/Developer/security-controller-raspi

class Camera(object):

    def __init__(self, name):
        self.name = name + ".jpg"

    def shoot(self):
        path = BASE_DIR + "/media/"
        os.system("sudo raspistill -o {}{}".format(path, self.name))
        return True

    def save(self):
        # http://www.louisyoung.site:8089/photo/share/scUP9PKA#!List
        client = Client(base_url='http://www.louisyoung.site:5005/',auth=('PhotoService', 'ImageHostingService'))
        client.ls(path='/', detail=False)
        path = BASE_DIR + "/media/"
        from_path = path + self.name
        to_path = '/photo/Image Hosting Service/' + self.name
        client.upload_file(from_path=from_path,to_path=to_path,overwrite=True)
        return True

