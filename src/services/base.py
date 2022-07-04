from services.base_abstract import ABSService, ModelRepo, ModelType, CreateSchemaType, UpdateSchemaType
from typing import Generic, Type, List
from sqlalchemy.orm import Session

class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType], ABSService):
    
    def __init__(self, model: Type[ModelType], repo:Type[ModelRepo]):
        self.model = model
        self.repo = repo

    def create(self, db: Session, data_in: CreateSchemaType) -> ModelType:
        print(data_in)
        return self.repo.create(db=db, data_in=data_in)

    def get(self, db: Session) -> List[ModelType]:
        return super().get(db)
    
    def get_one(self, db: Session, id: int) -> ModelType:
        return super().get_one(db, id)