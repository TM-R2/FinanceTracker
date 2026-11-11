from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Transaction
from .schema import TransactionCreate, TransactionUpdate

#Frontend sents Json data. Pydantic model is used to convert
# the Json data to a python object.
#model_dump converts the pydantic model to a dict.
def create_transaction(db: Session, transaction: TransactionCreate)-> Transaction:
    db_transaction = Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

#Read one dataset from the database.
#SELECT * FROM Transaction WHERE id = transaction_id
#Transaction is a SQLAlchemy model
# and describes data in the database.
#db.get is used to retrieve a single record
# from the database based on its primary key.
#get is as method of the Session object
# and takes two arguments:
def get_transaction(db: Session, transaction_id: int) -> Transaction | None:
    return db.get(Transaction, transaction_id)


#Read all data entries from the database.
#select(Transaction) creates a SQl  SELECT * statement
# to retrieve all rows from the Transaction table.
def get_transaction_all(db: Session) -> list[Transaction]:
    statement = select(Transaction)
    return list(db.scalars(statement).all())

#model_dump converts the pydantic model to a dict.
def update_transaction(db: Session, db_transaction: Transaction, transaction: TransactionUpdate) -> Transaction:
    update_data = transaction.model_dump()
    #print(f"Vorher: {db_transaction.amount}")
    #print(f"Update: {update_data}")
    for key, value in update_data.items():
        setattr(db_transaction, key, value)
    
    #print(f"Nachher: {db_transaction.amount}")
    db.commit()
    db.refresh(db_transaction)
    #print(f"Nach Commit: {db_transaction.amount}")

    return db_transaction


#DELETE FROM transactions where id = transaction_id
def delete_transaction(db: Session, db_transaction: Transaction) -> None:
    db.delete(db_transaction)
    db.commit()
