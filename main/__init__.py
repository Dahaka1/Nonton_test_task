from . import config
import os


class Settings:
	def __getattr__(self, item):
		return getattr(config, item)


settings = Settings()


def base_data_path():
	base_folder = [file for file in os.listdir(settings.DATA_BASE_DIR) if file.endswith(settings.DATA_FILES_FORMAT)]
	if base_folder.__len__() != 1:
		raise Exception("Database initializing error")
	result: str = next(filter(lambda path: str(path).endswith(settings.DATA_FILES_FORMAT), base_folder))
	return settings.DATA_BASE_DIR + result
