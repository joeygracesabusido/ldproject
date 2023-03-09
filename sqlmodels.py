from sqlmodel import Field, Session, SQLModel, create_engine,select,func,funcfilter,within_group
import urllib.parse
from typing import Optional
from pydantic import condecimal
from datetime import datetime, date

connection_string = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
    user="joeysabusido",
    password=urllib.parse.quote("Genesis@11"),
    host="192.46.225.247",
     port=3306,
    database="ldglobal"
)



engine = create_engine(connection_string, echo=True)


class payroll_computation(SQLModel, table=True): 
    """This is for cost or expenses table"""
    id: Optional[int] = Field(default=None, primary_key=True)
    cut_off_date: date
    employee_id: str = Field(index=True)
    salary_rate: condecimal(max_digits=18, decimal_places=2) = Field(default=0)


def updateSalaryRate(id,salary_rate):
    
    """This function is for updating rate in Payroll computation Table"""
    with Session(engine) as session:
        statement = select(payroll_computation).where(payroll_computation.id == id)
        results = session.exec(statement)

        result = results.one()

           
        result.salary_rate = salary_rate
       

    
        session.add(result)
        session.commit()
        session.refresh(result)


