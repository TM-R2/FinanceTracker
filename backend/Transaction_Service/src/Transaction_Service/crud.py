from sqlalchemy.orm import Session

from .models import Transaction
from .schemas import TransactionCreate


def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction