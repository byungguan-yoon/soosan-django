from visualize.models import Result, Labeling, Data
from django.contrib.auth.models import User as U
from ninja import Schema
from ninja.orm import create_schema
import datetime

ResultSchema = create_schema(Result)
LabelingSchema = create_schema(Labeling)
DataSchema = create_schema(Data)
UserSchema = create_schema(U)

class Images(Schema):
    id: int
    filename: str = None
    created_at: datetime.datetime
    labeling: LabelingSchema = None
    result: ResultSchema = None

class AI_Models(Schema):
    id: int
    status: str = None
    train_start: datetime.datetime = None
    train_end: datetime.datetime = None
    score: float = None
    path: str = None
    dataset: DataSchema = None
    user: UserSchema = None

class AI_Models_Update(Schema):
    train_start: datetime.datetime = None
    train_end: datetime.datetime = None
    score: float = None
    path: str = None

class AI_Models_Update_Status(Schema):
    status: str = None

class Datasets(Schema):
    id: int
    dataset_start: datetime.datetime
    dataset_end: datetime.datetime
    user: UserSchema