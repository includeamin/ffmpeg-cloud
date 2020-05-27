import tempfile


class PathManager:
    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.base_path = tempfile.TemporaryDirectory().name
