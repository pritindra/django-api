# # from django.conf import settings
# # from django.core.management.base import BaseCommand, CommandError
# # from ...models import employee, Base
# # import pandas as pd
# # class Command(BaseCommand):
# #     help = 'Migrates SQLAlchemy mapping classes'
    
# #     def handle(self, *args, **options):
# #         try:
# #             Base.metadata.create_all(settings.SNOWFLAKE['engine'])
# #             df = pd.read_csv(r"C:\Users\Dell\Desktop\the_project\employee\management\commands\employee.csv")
# #             df.columns = map(lambda x: str(x).upper(), df.columns)
# #             df.to_sql('employee', con=settings.SNOWFLAKE['engine'], if_exists='append', index=False)
# #             self.stdout.write(self.style.SUCCESS('Mapping classes migrated successfully.'))
# #         except Exception as error:
# #             self.stdout.write(self.style.ERROR(error))

import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from ...models import employee, Base

class Command(BaseCommand):
    help = 'Migrates SQLAlchemy mapping classes and reflects CSV file into database'

    def handle(self, *args, **options):
        try:
            # Reflect CSV file into database
            engine = create_engine('snowflake://vickydeka:Vicky1213@GVNUKEQ-WR96016/new_employee?warehouse=COMPUTE_WH&schema=new_employee')
            metadata = MetaData(bind=engine)
            employee_table = Table('employee', metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('name', String),
                                    Column('age', Integer),
                                    Column('salary', Integer))
            employee_table.create(checkfirst=True)
            df = pd.read_csv(r"C:\Users\Dell\Desktop\the_project\employee\management\commands\employee.csv")
            df.columns = map(lambda x: str(x).upper(), df.columns)
            df.to_sql('employee', con=engine, if_exists='append', index=False)

            # Migrate SQLAlchemy mapping classes
            Base.metadata.create_all(settings.SNOWFLAKE['engine'])
            self.stdout.write(self.style.SUCCESS('Mapping classes migrated successfully.'))
        except Exception as error:
            self.stdout.write(self.style.ERROR(error))


# import pandas as pd
# from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
# from django.conf import settings
# from django.core.management.base import BaseCommand, CommandError
# from ...models import Employee, Base

# class Command(BaseCommand):
#     help = 'Migrates SQLAlchemy mapping classes and reflects CSV file into database'

#     def handle(self, *args, **options):
#         try:
#             # Reflect CSV file into database
#             engine = create_engine('snowflake://vickydeka:Vicky1213@GVNUKEQ-WR96016/new_employee?warehouse=COMPUTE_WH&schema=new_employee')
#             metadata = MetaData(bind=engine)
#             employee_table = Table('employee', metadata,
#                                     Column('ID', Integer, primary_key=True),
#                                   #  Column('empname', String),
#                                     Column('AGE', Integer),
#                                     Column('SALARY', Integer))
#             employee_table.create(checkfirst=True)
#             df = pd.read_csv(r"C:\Users\Dell\Desktop\the_project\employee\management\commands\employee.csv")
#             df.to_sql('employee', con=engine, if_exists='append', index=False)

#             # Migrate SQLAlchemy mapping classes
#             Base.metadata.create_all(settings.SNOWFLAKE['engine'])
#             self.stdout.write(self.style.SUCCESS('Mapping classes migrated successfully.'))
#         except Exception as error:
#             self.stdout.write(self.style.ERROR(error))

