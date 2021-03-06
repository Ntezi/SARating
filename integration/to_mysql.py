import pandas as pd
import MySQLdb

from pandas.io import sql
from sqlalchemy import create_engine

results = pd.read_csv('../data/results/aspects_file_.csv', index_col=0)
results.drop(results.columns[results.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
# print(results)

engine = create_engine('mysql://root:mysqlroot@localhost/sa_rating')

with engine.connect() as conn, conn.begin():
    results.to_sql('aspect_sentiments', conn, if_exists='append')
