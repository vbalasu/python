import urllib.request
import shutil

shutil.copyfile(urllib.request.urlretrieve('https://cloudmatica.com/img/userprofile.png')[0],'userprofile.png')
