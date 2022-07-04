from mysqlx import Session
from repo.base_abstract import ABSRepo, ModelType, CreateSchemaType, UpdateSchemaType
from typing import Generic, List, Type

class BaseRepo(Generic[ModelType, CreateSchemaType, UpdateSchemaType], ABSRepo):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, db: Session, data_in: CreateSchemaType) -> ModelType:
        data = self.model(**data_in.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    def get(self, db: Session) -> List[ModelType]:
        query = db.query(self.model).all()
        return query

    def get_one(self, db: Session, id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == id).first()
        