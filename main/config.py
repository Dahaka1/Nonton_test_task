DATA_BASE_DIR = "data/"
DATA_FILES_FORMAT = ".dat"
DATA_TYPING = "bytes"  # text/bytes

STARTING_CMDS = [
	"from models.general import ProductsImpl",
	"from models.subclasses import Product"
]

STARTING_MSG = "Packages was successfully imported.\n" \
			   "Now you can create instances you needed by commands:\n" \
			   "- 'foo = Product(id=*ID*, name=*NAME*)'\n" \
			   "- 'bar = ProductsImpl()'"

