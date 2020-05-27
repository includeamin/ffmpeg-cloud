import ffmpeg_streaming
from ffmpeg_streaming import Representation, Formats, CloudManager
import tempfile


class HLS:
    def __init__(self, file_path: str, destination_type: str):
        self.path = file_path
