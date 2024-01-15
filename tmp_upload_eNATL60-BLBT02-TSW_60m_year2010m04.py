import json
import requests
import numpy as np


ACCESS_TOKEN = 'C1MmDeDNgbgzt7rQNl1JwLjwQJM7Icft25TtU8599PNvdM6m6aPI0vVtwNWI'
headers = {"Content-Type": "application/json"}
params = {'access_token': ACCESS_TOKEN}

r0 = requests.post('https://zenodo.org/api/deposit/depositions',
                   params=params,
                   json={},
                   headers=headers)

print(r0.json())

deposition_id=r0.json()['id']

print(deposition_id)

bucket_url = r0.json()["links"]["bucket"]

for day in np.arange(1,30+1):
    dd="{:02d}".format(day) 
    filename = "eNATL60-BLBT02_y2010m04d"+str(dd)+".1d_TSW_60m.nc"
    path = "/mnt/summer/DATA_MEOM/MODEL_SET/eNATL60/eNATL60-BLBT02/1d/eNATL60/%s" % filename
    with open(path, "rb") as fp:
        r1 = requests.put(
            "%s/%s" % (bucket_url, filename),
            data=fp,
            params=params,
        )

print(r1.json())

data = {
    "metadata": {
        "title": "eNATL60-BLBT02 TSW 60m y2010m04",
        "upload_type": "dataset",
        "publication date":"2023-12-01",
        "description":"Daily files of eNATL60-BLBT02 Temperature Salinity and Vertical velocity fields at 60m for year 2010 month 04",
        "creators": [
            {"name": "Albert, Aurelie", "affiliation": "CNRS"}
        ],
        "access_right":"open"
    }
}

r2 = requests.put('https://zenodo.org/api/deposit/depositions/%s' % deposition_id,
                  params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),
                  headers=headers)

print(r2.json())
