import requests
url = "http://0.0.0.0:9696/predict"

employee = {
  'education': 'bachelors',
  'joiningyear': 2014,
  'city': 'bangalore',
  'paymenttier': 3,
  'age': 35,
  'gender': 'female',
  'everbenched': 'no',
  'experienceincurrentdomain': 2
}
client = requests.post(url, json=employee)
print(client.json())