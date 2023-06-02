from typing import Any
from . import Data
from data import Attrs
from main import base_data_path


class ProductsImpl(Data):
	data: list[tuple[str]]
	data_path: str

	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		attrs = Attrs(*args, **kwargs).attrs
		self.attrs = attrs
		self.data_path = base_data_path()

	@staticmethod
	def addProduct(instance: Any) -> bool:
		empty = ProductsImpl()
		if any(obj.attrs.get('id') == instance.id for obj in empty.objects(instance)):
			return False
		empty += instance
		Data().save(empty)
		return True

	@staticmethod
	def deleteProduct(instance: Any) -> bool:
		return ProductsImpl().__delete__(instance)

	@staticmethod
	def getName(instance_id: str) -> str:
		return ProductsImpl()[instance_id] or str()

	@staticmethod
	def findByName(instance_name: str) -> list[str]:
		empty = ProductsImpl()
		filtered = list(map(lambda item: item[0], filter(lambda item: item[1] == instance_name,
														 empty.data)))
		return filtered
