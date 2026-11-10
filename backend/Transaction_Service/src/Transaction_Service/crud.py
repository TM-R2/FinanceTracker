from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Transaction
from .schema import TransactionCreate

#Frontend sents Json data. Pydantic model is used to convert
# the Json data to a python object.
#model_dump converts the pydantic model to a dict.
def create_transaction(db: Session, transaction: TransactionCreate)-> Transaction:
    db_transaction = Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

#Read one data entry from the database.
def get_transaction(db: Session, transaction_id: int) -> Transaction | None:
    return db.get(Transaction, transaction_id)


#Read all data entries from the database.
#select(Transaction) creates a SQl  SELECT * statement
# to retrieve all rows from the Transaction table.
def get_transaction(db: Session) -> list[Transaction]:
    statement = select(Transaction)
    return list(db.scalars(statement).all())