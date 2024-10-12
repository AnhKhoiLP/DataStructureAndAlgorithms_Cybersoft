class Node:
	def __init__(self, phone):
		self.key = phone["price"]
		self.info = phone
		self.left = None
		self.right = None

class BSTree:
#> TẠO CÂY NHỊ PHÂN
	def __init__(self):
		self.root = None
#> THÊM NÚT MỚI VÀO NÀ
	def insert_node(self, phone):
		self.root = self._insert(self.root, phone)
#> PHÂN LOẠI TRÁI / PHẢI
	def _insert(self, current_node, phone):
	## TRỐNG THÌ THÊM ĐT MỚI VÀO
		if not current_node:
			return Node(phone)
	## GIÁ < THÊM VÀO TRÁI
		if phone["price"] < current_node.key:
			current_node.left = self._insert(current_node.left, phone)
	## GIÁ > THÊM VÀO PHẢI
		elif phone["price"] > current_node.key:
			current_node.right = self._insert(current_node.right, phone)
	## RETURN CURRENT_NODE
		return current_node
#> IN RA CÂY DẠNG STRING
	def get_tree(self):
		return self._in_order(self.root).strip()
#> DUYỆT CÂY THEO THỨ TỰ IN-ORDER: NHÁNH TRÁI, NÚT HIỆN TẠI, NHÁNH PHẢI
	def _in_order(self, current_node):
		if not current_node:
			return ''
		return f"{self._in_order(current_node.left)} {current_node.key} {self._in_order(current_node.right)}"
#> TÌM KIẾM CÁC GIÁ TRỊ TRONG KHOẢNG CÁCH 1
	def find_price_range(self, min_price, max_price):
		result = []
		self._find_price_range(self.root, min_price, max_price, result)
		return result
#> TÌM KIẾM CÁC GIÁ TRỊ TRONG KHOẢNG CÁCH 2
	def _find_price_range(self, current_node, min_price, max_price, result):
		if not current_node:
			return
	## NẾU GIÁ TRỊ NODE NẰM TRONG KHOẢNG
		if min_price <= current_node.key <= max_price:
			result.append(current_node.info["name"])
	## NẾU GIÁ TRỊ NODE LỚN HƠN MIN_PRICE, SANG TRÁI
		if current_node.key > min_price:
			self._find_price_range(current_node.left, min_price, max_price, result)
	## NẾU GIÁ TRỊ NODE NHỎ HƠN MAX_PRICE, SANG PHẢI
		if current_node.key < max_price:
			self._find_price_range(current_node.right, min_price, max_price, result)
#> ĐT CÓ GIÁ CHÍNH XÁC CÁCH 1
	def find_exact_price(self, price):
		result = self._find_exact_price(self.root, price)
		return result if result else "Khong phai la tao khong co ma tao khong ban"
#> ĐT CÓ GIÁ CHÍNH XÁC CÁCH 2
	def _find_exact_price(self, current_node, price):
		if not current_node:
			return None
	## NẾU GIÁ TRỊ NODE NẰM TRONG KHOẢNG
		if current_node.key == price:
			return current_node.info["name"]
	## NẾU GIÁ TRỊ NODE LỚN HƠN MIN_PRICE, SANG TRÁI
		elif price < current_node.key:
			return self._find_exact_price(current_node.left, price)
	## NẾU GIÁ TRỊ NODE NHỎ HƠN MAX_PRICE, SANG PHẢI
		else:
			return self._find_exact_price(current_node.right, price)
#> Danh sách điện thoại
phone_list = [
	{"name": "phone A", "price": 13},
	{"name": "phone B", "price": 20},
	{"name": "phone C", "price": 4 },
	{"name": "phone D", "price": 2 },
	{"name": "phone E", "price": 14},
	{"name": "phone F", "price": 22},
	{"name": "phone G", "price": 5 }
]
#> TẠO CÂY ĐT
phone_tree = BSTree()
for phone in phone_list:
	phone_tree.insert_node(phone)
#> MIN, MAX, EXACT HAVE, EXACT HAVEN'T
min_price = 2
max_price = 7
exact_price = 20
exact_price2 = 10000
#> QUẨY
print("Cay B.S.T:", phone_tree.get_tree())
print("Dien thoai trong khoang gia {} den {}: {}".format(min_price, max_price, phone_tree.find_price_range(min_price, max_price)))
print("Dien thoai co gia tri la {}: {}".format(exact_price, phone_tree.find_exact_price(exact_price)))
print("Dien thoai co gia tri la {}: {}".format(exact_price2, phone_tree.find_exact_price(exact_price2)))
