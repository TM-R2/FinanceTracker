#API, Exception
from fastapi import FastAPI, Depends, HTTPException
#Executing SQL statements and managing database sessions
from sqlalchemy.orm import Session


from .database import Base, engine,get_db
#Transaction describes the structure of data in the database. Defined in models.py.
from .models import Transaction
from .schema import TransactionCreate, TransactionResponse, TransactionUpdate
from .crud import create_transaction, get_transaction_all, get_transaction, update_transaction, delete_transaction

#Create an instance of the FastAPI class to define the API application.
#Execute app witch uvicorn main:app --reload to start the API server.
app = FastAPI(title="Transaction API", description="API for managing transactions", version="1.0.0")
Base.metadata.create_all(bind=engine)


#Create C
#response_model defines the pydantic model which describes the structure of the response data.
#Defined in schema.py.
#TransactionCreate is an pydantic model and describes data come in.
#Transaction desribes SQLAlchemy model and describes data in the database.
@app.post("/transactions/", response_model=TransactionResponse)
def post_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db=db, transaction=transaction)

#Read all transactions from the database. R
@app.get(
"/transactions/",
response_model=list[TransactionResponse]
)
def read_transaction(db: Session = Depends(get_db)):
    return get_transaction_all(db)

#Read one transaction from the database by id R
@app.get("/transactions/{transaction_id}",response_model=TransactionResponse)
def read_transation(transaction_id: int,db: Session = Depends(get_db)):
    transaction = get_transaction(db=db, transaction_id=transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction

#Update a transaction by id. U (Put)
#Decorator @app.put registers the function at FASTAPI put_transaction
# as a handler for HTTP PUT requests to the specified endpoint.
#db_transaction is the transaction object(data)
# retrieved from the database using the get_transaction function.
#FASTAPI automatically converts the
# incoming JSON data to a TransactionUpdate object and stores it in transaction.
#JSON data is converted to a TransactionUpdate object using Pydantic's model parsing and validation.
#Depends(get_db) is a dependency
# injection mechanism provided by FastAPI.Returns session object to the function.
#Returns the updated transaction object 
# after committing the changes to the database.For the client.
@app.put("/transactions/{transaction_id}",response_model=TransactionResponse)
def put_transaction(transaction_id: int,transaction: TransactionUpdate,db: Session = Depends(get_db)):
    db_transaction = get_transaction(db=db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return update_transaction(db=db, db_transaction=db_transaction, transaction=transaction)

#Delete a transaction by id. D (Delete). SELECT FROM transactions WHERE id = transaction_id
#status_code=204 means no content is returned in the response.
#dB.session is used to edit data in the database.
@app.delete("/transactions/{transaction_id}", status_code=204)
def delete_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = get_transaction(db=db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    delete_transaction(db=db, db_transaction=db_transaction)
    