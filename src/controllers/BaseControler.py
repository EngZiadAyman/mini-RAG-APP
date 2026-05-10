from helpers.config import Config, get_config

import os


class BaseController:
    def __init__(self, config: Config = get_config()):
        self.config = config
        self.base_data_path = os.path.dirname(os.path.dirname(__file__))
        self.files_dir = os.path.join(self.base_data_path, "assets/files")