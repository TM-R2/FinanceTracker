from datetime import date
from decimal import Decimal
from pydantic import BaseModel, ConfigDict



class TransactionBase(BaseModel):
    name: str
    description: str | None = None
    amount: Decimal
    category: str
    time: date

#Get data from Client. Data is sent as Json from the client. 
# The TransactionCreate class is used to convert the Json data to a pydantic model.
class TransactionCreate(TransactionBase):
    pass

#Read data from database. Data is returned as dict from database. 
# The TransactionResponse class is used to convert the dict to a pydantic model.
#From_attributes=True allows Pydantic to create Json data from the attributes of the Transaction model.
class TransactionResponse(TransactionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class TransactionUpdate(BaseModel):
    pass



