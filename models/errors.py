from schematics import Model
from schematics.types import StringType


class NotFound(Model):
    detail = StringType(required=True)
