from visualize.models import Result, Labeling
from ninja import Schema
from ninja.orm import create_schema
import datetime

ResultSchema = create_schema(Result)
LabelingSchema = create_schema(Labeling)


class Images(Schema):
    id: int
    filename: str = None
    created_at: datetime.datetime
    labeling: LabelingSchema = None
    result: ResultSchema = None
