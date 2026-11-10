#API, Exception
from fastapi import FastAPI, Depends, HTTPException
#Executing SQL statements and managing database sessions
from sqlalchemy.orm import Session


from .database import Base, engine,get_db
#Transaction describes the structure of data in the database. Defined in models.py.
from .models import Transaction
from .schema import TransactionCreate, TransactionResponse, TransactionUpdate
from .crud import create_transaction, get_transaction_all, get_transaction, update_transaction

#Create an instance of the FastAPI class to define the API application.
#Execute app witch uvicorn main:app --reload to start the API server.
app = FastAPI(title="Transaction API", description="API for managing transactions", version="1.0.0")
Base.metadata.create_all(bind=engine)



#response_model defines the pydantic model which describes the structure of the response data.
#Defined in schema.py.
#TransactionCreate is an pydantic model and describes data come in.
#Transaction desribes SQLAlchemy model and describes data in the database.
@app.post("/transactions/", response_model=TransactionResponse)
def post_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db=db, transaction=transaction)

@app.get(
"/transactions/",
response_model=list[TransactionResponse]
)
def read_transaction(db: Session = Depends(get_db)):
    return get_transaction_all(db)

@app.get("/transactions/{transaction_id}",response_model=TransactionResponse)
def read_transation(transaction_id: int,db: Session = Depends(get_db)):
    transaction = get_transaction(db=db, transaction_id=transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction

@app.put("/transactions/{transaction_id}",response_model=TransactionResponse)
def put_transaction(transaction_id: int,transaction: TransactionUpdate,db: Session = Depends(get_db)):
    db_transaction = get_transaction(db=db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return update_transaction(db=db, db_transaction=db_transaction, transaction=transaction)