import pandas as pd

print("Extract Data FRom MYSQL")

data = {
    "id": [1,2,3],
    "name": ["avnish","kiran","vaibhav"],
    "salary": [10000,20000,30000]
}

df = pd.DataFrame(data)

print(df)