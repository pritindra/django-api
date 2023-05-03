from django.db import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

# SQLAlchemy models
Base = declarative_base()

class employee(Base):
    __tablename__ = 'employee'

    # Columns
    id = Column(Integer, Sequence('air_id_seq'), primary_key=True)
    name = Column(String(256), nullable=False)
    age = Column(String(20), nullable=False)
    salary = Column(String, nullable=False)

    objects = models.Manager()

    def __repr__(self):
        """String representation of this class"""
        return f"<employee(id={str(self.id)}, name={self.name})>"

# from django.db import models
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Sequence

# # SQLAlchemy models
# Base = declarative_base()

# class Employee(Base):
#     __tablename__ = 'employee'

#     # Columns
#     ID = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     #empname = Column(String)
#     AGE = Column(Integer)
#     SALARY = Column(Integer)

#     def __repr__(self):
#         """String representation of this class"""
#         return f"<employee(id={str(self.ID)}, name={self.empname})>"
