from sqlalchemy import  Integer, String, float,date
from Decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

#  DeclarativeBase class is used to create a base class for all the models in the database.
#  It provides a way to define the structure of the database tables and their relationships.




class Transaction(Base):
    __tablename__ = "transactions"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(index=True, nullable=False)
    description : Mapped[str] = mapped_column(index=True, nullable=True)
    amount : Mapped[float] = mapped_column(index=True, nullable=False)
    category : Mapped[str] = mapped_column(index=True, nullable=False)
    time : Mapped[datetime] = mapped_column(index=True, nullable=False)

    


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