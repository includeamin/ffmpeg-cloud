from pydantic import BaseModel


class LocalDownload(BaseModel):
    file_path: str
