import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('IOT-temp.csv')

engine = create_engine('postgresql://postgres:1969@localhost:5432/postgres')

df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso!")