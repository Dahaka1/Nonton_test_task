from .general import ProductsImpl
from typing import Optional
from tests import test_input
from data import read_data, init_database


class Product(ProductsImpl):
	id: Optional[str]
	name: Optional[str]

	def __init__(self, *args, **kwargs):
		self.data_path = init_database(self.__class__)
		self.data = read_data(self.data_path)
		super().__init__(*args, **kwargs)
		test_input(args, kwargs)
		if not any(args):
			self.id = kwargs.get("id", None)
			self.name = kwargs.get("name", None)
		else:
			self.id, self.name = args


