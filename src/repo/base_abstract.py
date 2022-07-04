from abc import ABC, abstractmethod
from db import Base
from typing import List, Type, TypeVar
from models import BaseModel
from sqlalchemy.orm import Session


ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class ABSRepo(ABC):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    @abstractmethod
    def create(self, db: Session, data_in: CreateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def get(self, db: Session) -> List[ModelType]:
        pass 

    @abstractmethod
    def get_one(self, db: Session, id:int) -> ModelType:
        pass