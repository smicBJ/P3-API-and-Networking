import requests as req

name = input("Whose record would you like to pull up?\n>> `")

url_string = f"http://10.6.20.146:8000/users/{name}"

response = req.get(url=url_string)

json_data = response.json()

if "msg" in json_data:
    print(json_data['msg'])
else:
    print(f"The student named {json_data['name']} is in grade {json_data['grade']}")
