class VideoFile(object):
    def __init__(self, filename: str):
        self.filename = filename
        self.base_path: str


class ConvertStrategyInterface:
    def convert(self):
        pass


class HLS(ConvertStrategyInterface):
    def convert(self):
        pass


class DASH(ConvertStrategyInterface):
    def convert(self):
        pass


class UploadStrategyInterface:
    def __upload(self):
        pass

    def get_path(self):
        pass


class DownloadStrategyInterface:
    def __download(self):
        pass

    def get_path(self):
        pass


class LocalDownload(DownloadStrategyInterface):
    """
    in this strategy we sure that video file downloaded (client uploads the file with dropzone)
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def __download(self):
        """
        actually this method does nothing, just return the path of uploaded file by user
        :return:
        """
        return self.file_path

    def get_path(self):
        return self.__download()


class LocalUpload(UploadStrategyInterface):
    def upload(self):
        pass


class S3Download(DownloadStrategyInterface):
    def download(self):
        pass


class S3Upload(UploadStrategyInterface):
    def upload(self):
        pass


class FFMPEG(object):
    def __init__(self, file_path: str, download_strategy: DownloadStrategyInterface = None,
                 upload_strategy: UploadStrategyInterface = None,
                 convert_strategy: ConvertStrategyInterface = None):
        self.upload_strategy = upload_strategy if upload_strategy else LocalUpload()
        self.download_strategy = download_strategy if download_strategy else LocalDownload(file_path=file_path)
        self.convert_strategy = convert_strategy if convert_strategy else HLS()

    def convert(self):
        # todo: download the video
        # todo: convert
        # todo: upload
        pass

    def run(self):
        pass


class FFMPEGFactory:
    pass
