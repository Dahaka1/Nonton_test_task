# nonton_test_task 

# ABOUT
It's the project realizing a simple example of non-relational database structure (high-level).
There's no supporting using as server or script waiting for incoming tasks or commands.
It just supports package importable usage from Python console.

# BUILT IN
No external packages using.

# USAGE
- Set up configuration file in 'main' package. You can use text- or bytes-based data structure;
- Import exampling packages 'Product' and 'ProductsImpl', based on parent-class 'Data';
- Then make an instance of class 'Product' with tho parameters such as "id" and "name";
- Use 'ProductsImpl'-instance for using their class methods for handling 4 general DB queries:
    - addProduct(arg: _Product instance_) - adding new DB-row if there's no object with same "id" field;
    - deleteProduct(arg: _Product instance_) - deleting row from DB if it exists;
    - getName(arg: _"id" field (integer)_) - finding field "name" by field "id" if it exists;
    - findByName(arg: _"name" field (string)_) - finding all fields "id" where field "name" is equally query-name if there exists.