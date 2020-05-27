from pydantic import BaseSettings, validator

valid_storage = ["S3",
                 "LOCAL"]


class DataBase(BaseSettings):
    URL: str = "mongodb://mongo"
    NAME: str = "ffmpeg-cloud"
    IN_PROGRESS_COLLECTION: str = "in-progress"


database_settings = DataBase()


class Celery:
    BROKER: str = "pyamqp://rabbitmq"
    BACKEND: str = database_settings.URL


celery_settings = Celery()


class Notification(BaseSettings):
    SMTP_SERVER: str
    USERNAME: str
    PASSWORD: str


class UploadSettings(BaseSettings):
    TYPE: str
    HOST: str = None
    ACCESS_KEY: str = None
    SECRET_KEY: str = None

    @validator('TYPE')
    def type_validator(cls, v):
        if not isinstance(v, str):
            raise Exception("storage type should be string")
        v = v.upper()
        if v not in valid_storage:
            raise Exception(f"invalid storage:\n {valid_storage}")
