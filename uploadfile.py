import requests
r = requests.post('https://cloudmatica.com/python/uploadfile.php', files={'userprofile.png': open('userprofile.png', 'rb')})
print(r.text)