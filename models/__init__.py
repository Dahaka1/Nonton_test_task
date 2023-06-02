from data import write_data, read_data
from typing import Optional, Any
from main import base_data_path


class Data:
	data: Optional[list[tuple[str]]]
	attrs: dict
	data_path: str

	def __init__(self, *args, **kwargs):
		self.data = read_data(base_data_path())
		self.data_path = base_data_path()

	def __add__(self, other: Any) -> object:
		if not isinstance(other, self.__class__):
			raise ValueError("Incorrect adding var type")
		key, value = other.attrs.values()
		new_data: tuple = key, value
		self.data.append(new_data)
		return self.data

	def __delete__(self, instance: Any) -> bool:
		try:
			instance.data = self.refresh_data(instance)  # refreshing
			var = next(iter(filter(lambda item: item[0] == instance.id, instance.data)))
			self.data.remove(var)
			Data().save(self.data)
			return True
		except (StopIteration, ValueError):
			return False

	def __getitem__(self, instance_id) -> Optional[Any]:
		try:
			self.data = self.refresh_data(instance_id)  # refreshing
			obj = next(filter(lambda item: item[0] == instance_id, self.data))
		except StopIteration:
			return None
		return obj[1]

	@staticmethod
	def save(data) -> None:
		write_data(data, Data().data_path)

	@staticmethod
	def objects(instance):
		try:
			instance.data = Data().refresh_data(instance)  # refreshing
			return [instance.__class__(*item) for item in instance.data]
		except Exception as exs:
			raise ValueError("Getting data objects error: " + str(exs))

	@staticmethod
	def refresh_data(instance: Any) -> list[tuple]:
		try:
			data = read_data(instance.data_path)
		except AttributeError:
			data = read_data(base_data_path())
		return data
