import pandas as pd
import sqlalchemy

# read/write methods for db
class db_io:

    @classmethod
    def write_from_xlsx(cls, connection, textfield, exc):
        try:
            dbdata = pd.read_excel(textfield).sort_values(by=['TagName'], ignore_index=True)

            dbdata.to_sql(name='table_xlsx', con=connection, if_exists='replace',
                          dtype={
                              'DateTime': sqlalchemy.types.TIMESTAMP,
                              'TagName': sqlalchemy.types.TEXT,
                              'Type': sqlalchemy.types.TEXT,
                              'Value': sqlalchemy.types.REAL
                          }
                          )
        except Exception:
            exc('xlsx')

    @classmethod
    def write_from_csv(cls, connection, textfield, exc):
        try:
            dbdata = pd.read_csv(textfield).sort_values(by=['TagName'], ignore_index=True)
            dbdata.to_sql(name='table_csv', con=connection, if_exists='replace',
                          dtype={
                              'TagName': sqlalchemy.types.TEXT,
                              'Type': sqlalchemy.types.TEXT,
                              'Value': sqlalchemy.types.REAL
                          }
                          )
        except Exception:
            exc('csv')

    @classmethod
    def export_to_xlsx(cls, connection):
        xlsx_out = pd.read_sql(sql="select * from table_xlsx", con=connection)
        xlsx_out.to_excel('out.xlsx')

    @classmethod
    def export_to_csv(cls, connection):
        csv_out = pd.read_sql(sql="select * from table_csv", con=connection)
        csv_out.to_csv('out.csv')

