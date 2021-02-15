from schematics import Model
from schematics.types import IntType, StringType, ListType, ModelType, DateTimeType

from сonstants.test_data import DATE_TIME_FORMAT, RELEASE_DATE_FORMAT


class Film(Model):
    characters = ListType(StringType, required=True)
    created = DateTimeType(required=True, formats=DATE_TIME_FORMAT)
    director = StringType(required=True)
    edited = DateTimeType(required=True, formats=DATE_TIME_FORMAT)
    episode_id = IntType(required=True)
    opening_crawl = StringType(required=True)
    planets = ListType(StringType, required=True)
    producer = StringType(required=True)
    release_date = DateTimeType(required=True, formats=RELEASE_DATE_FORMAT)
    species = ListType(StringType, required=True)
    starships = ListType(StringType, required=True)
    title = StringType(required=True)
    url = StringType(required=True)
    vehicles = ListType(StringType, required=True)


class Films(Model):
    count = IntType(required=True)
    next = StringType(required=False)
    previous = StringType(required=False)
    results = ListType(ModelType(Film, required=True))
