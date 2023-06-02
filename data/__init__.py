import os.path
from typing import Any
from main import settings


def init_database(cls: Any) -> str:
	filepath = settings.DATA_BASE_DIR + cls.__name__ + settings.DATA_FILES_FORMAT
	if not os.path.exists(filepath):
		file = open(filepath, 'wb')
		file.close()
	return filepath


def read_data(filepath: str) -> list[tuple[str]]:
	def read_txt():
		with open(filepath) as file:
			raw = file.read().split(';')
			return read_raw_data(raw)

	def read_bytes():
		with open(filepath, 'rb') as file:
			try:
				raw = file.read().decode('utf-8').split(';')
			except Exception:
				raise Exception("Encoding bytes data error")
			return read_raw_data(raw)

	def read_raw_data(raw):
		out = []
		raw = [item for item in raw if item]
		if not any(raw):
			return out
		for item in raw:
			key, value = item.split('_')
			item = int(key) if str(key).isdigit() else key, int(value) if str(value).isdigit() else value  # -> tuple
			out.append(item)
		return out

	funcs = {
		"bytes": read_bytes,
		"text": read_txt
	}

	try:
		return funcs[settings.DATA_TYPING]()
	except KeyError:
		raise KeyError("Non-supported data typing format")
	except FileNotFoundError:
		return []
	except Exception as exs:
		raise Exception("Reading data error: " + str(exs))


def write_data(data: list[tuple[str]], filepath: str) -> None:
	def write_txt():
		with open(filepath, 'w') as file:
			output = format_data_to_raw()
			file.write(output)

	def write_bytes():
		with open(filepath, 'wb') as file:
			output = bytearray(format_data_to_raw(), 'utf-8')
			file.write(output)

	def format_data_to_raw():
		out = ''
		for item in data:
			item = map(str, item)
			out += '_'.join(item) + ';'
		return out

	funcs = {
		"bytes": write_bytes,
		"text": write_txt
	}

	try:
		return funcs[settings.DATA_TYPING]()
	except KeyError:
		raise KeyError("Non-supported data typing format")
	except Exception as exs:
		raise Exception("Writing data error: " + str(exs))


class Attrs(dict):
	def __init__(self, *args, **kwargs):
		super().__init__()
		if all((args, kwargs)):
			raise AttributeError("Object __init__ taking only args OR kwargs")
		if args and not kwargs:
			self.attrs = {"id": args[0], "name": args[1]}
		else:
			self.attrs = kwargs
