import requests

ACCESS_TOKEN = 'SFsdzsUTPjgifG8Bzg3AiuAt8tD6EqJv5cS8x6ZGA2Zs092CKR3kmX4xp235'
headers = {"Content-Type": "application/json"}
params = {'access_token': ACCESS_TOKEN}
r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
                   params=params,
                   json={},
                   headers=headers)
print(r.status_code)
print(r.json())

bucket_url = r.json()["links"]["bucket"]
filename = "formation.tar"
path = "/Users/aureliealbert/Data/%s" % filename

with open(path, "rb") as fp:
    r = requests.put(
        "%s/%s" % (bucket_url, filename),
        data=fp,
        params=params,
    )

r.json()

deposition_id='1604'

data = {
     'metadata': {
         'title': 'My first upload',
         'upload_type': 'poster',
         'description': 'This is my first upload',
         'creators': [{'name': 'Doe, John',
                       'affiliation': 'Zenodo'}]
     }
 }
r = requests.put('https://zenodo.org/api/deposit/depositions/%s' % deposition_id,
                  params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),
                  headers=headers)

r.status_code

