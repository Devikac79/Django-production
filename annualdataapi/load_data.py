# import pandas as pd
# from api.models import AnnualData

# def load_data():
#     # file_path = "https://ohiodnr.gov/static/documents/oil-gas/production/20210309_2020_1%20-%204.xls"
#     df = pd.read_excel('data.xls')
    

#     for _, row in df.iterrows():
#         AnnualData.objects.create(
#             API_WELL_NUMBER=row['API_WELL_NUMBER'],
#             OIL=row['OIL'],
#             GAS=row['GAS'],
#             BRINE=row['BRINE']
#         )

# if __name__ == "__main__":
#     load_data()

import pandas as pd
from api.models import AnnualData

def load_data():
    file_path = "https://ohiodnr.gov/static/documents/oil-gas/production/20210309_2020_1%20-%204.xls"
    df = pd.read_excel(file_path)

    # Group data by well API number and calculate annual totals
    annual_data = df.groupby('API WELL  NUMBER').sum()

    for _, row in annual_data.iterrows():
        AnnualData.objects.create(
            well=row.name,
            oil=row['OIL'],
            gas=row['GAS'],
            brine=row['BRINE']
        )

if __name__ == "__main__":
    load_data()

