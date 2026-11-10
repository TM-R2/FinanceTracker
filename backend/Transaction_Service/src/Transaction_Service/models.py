from sqlalchemy import  Integer, String, Float,Date
from datetime import date
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

#  DeclarativeBase class is used to create a base class for all the models in the database.
#  It provides a way to define the structure of the database tables and their relationships.




class Transaction(Base):
    __tablename__ = "transactions"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(nullable=False)
    description : Mapped[str] = mapped_column(nullable=True)
    amount : Mapped[float] = mapped_column(nullable=False)
    category : Mapped[str] = mapped_column(nullable=False)
    time : Mapped[date] = mapped_column(Date, nullable=False)

    


    def __repr__(self):
        return (
               f"Transaction("
               f"id={self.id},"
               f"name={self.name},"
               f"description={self.description},"
               f"amount={self.amount},"
               f"category={self.category},"
               f"time={self.time}"
               f")"
        )