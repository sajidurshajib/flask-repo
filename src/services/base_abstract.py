from abc import ABC, abstractmethod
from typing import TypeVar, Type, List
from db import Base
from models import BaseModel
from sqlalchemy.orm import Session
from repo import BaseRepo

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)
ModelRepo = TypeVar('ModelRepo', bound=BaseRepo)

class ABSService(ABC):

    def __init__(self, model: Type[ModelType], repo:Type[ModelRepo]):
        self.model = model
        self.repo = repo

    @abstractmethod
    def create(self, db: Session, data_in: CreateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def get(self, db: Session) -> List[ModelType]:
        pass 

    @abstractmethod
    def get_one(self, db: Session, id:int) -> ModelType:
        pass