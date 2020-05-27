class BaseCloud:
    def upload(self, path: str, file_name: str):
        pass

    def download(self, file_name: str, path: str):
        pass

    def log(self, info: dict):
        pass
