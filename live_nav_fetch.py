import requests
import pandas as pd
import os

schemes = {
    "125497": "HDFC_Top_100_Direct",
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_Large_Cap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip"
}

os.makedirs("data/raw", exist_ok=True)

for code, name in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        filename = f"data/raw/{name}_{code}.csv"

        df.to_csv(filename, index=False)

        print(f"Saved: {filename}")

    else:
        print(f"Failed: {code}")