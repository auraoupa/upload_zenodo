import json
import requests

ACCESS_TOKEN = 'SFsdzsUTPjgifG8Bzg3AiuAt8tD6EqJv5cS8x6ZGA2Zs092CKR3kmX4xp235'
headers = {"Content-Type": "application/json"}
params = {'access_token': ACCESS_TOKEN}

r0 = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
                   params=params,
                   json={},
                   headers=headers)

print(r0.json())

deposition_id=r0.json()['id']

print(deposition_id)

bucket_url = r0.json()["links"]["bucket"]
filename = "eNATL60-BLBT02_y2010m01d01.1d_TSW_60m.nc"
path = "/Users/aureliealbert/Data/sshfs_cal1_data-meom/MODEL_SET/eNATL60/eNATL60-BLBT02/1d/eNATL60/%s" % filename

with open(path, "rb") as fp:
    r1 = requests.put(
        "%s/%s" % (bucket_url, filename),
        data=fp,
        params=params,
    )


print(r1.json())

data = {
    "metadata": {
        "title": "Testing upload 2 files",
        "upload_type": "dataset",
        "publication date":"2023-11-23",
        "description":"This is my first upload",
        "creators": [
            {"name": "Albert, Aurelie", "affiliation": "CNRS"}
        ],
        "access_right":"open"
    }
}

r2 = requests.put('https://sandbox.zenodo.org/api/deposit/depositions/%s' % deposition_id,
                  params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),
                  headers=headers)

print(r2.json())