# import constants as const
import peewee
import os

# db = peewee.SqliteDatabase(const.PEEWEE_DATABASE_URI)
db = peewee.SqliteDatabase(f"{os.getcwd()}\\mv_studio_orm.db")

class BaseModel(peewee.Model):

    class Meta:

        database = db