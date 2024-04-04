import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site nao esta acessivel ')
else: 
    print('Site acessado')
    print(site.read())


