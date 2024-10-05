class Node:
    def __init__(self, phone):
        self.key = phone["price"]
        self.info = phone
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def insert_node(self, phone):
        self.root = self.insert(self.root, phone)

    def insert(self, current_node, phone):
        if current_node is None:
            return Node(phone)

        if phone["price"] < current_node.key:
            current_node.left = self.insert(current_node.left, phone)
        elif phone["price"] > current_node.key:
            current_node.right = self.insert(current_node.right, phone)

        return current_node

    def get_tree(self):
        return self.in_order(self.root)

    def in_order(self, current_node):
        if current_node is None:
            return ''
        left_part = self.in_order(current_node.left)
        right_part = self.in_order(current_node.right)
        
        return f"{left_part} {current_node.key} {right_part}".strip()

    def find_price(self, min_price, max_price):
        result = []
        self._find_price(self.root, min_price, max_price, result)
        return result

    def _find_price(self, current_node, min_price, max_price, result):
        if current_node is None:
            return

        # Kiểm tra xem current_node.info có phải là từ điển không
        if isinstance(current_node.info, dict) and "name" in current_node.info:
            if min_price <= current_node.key <= max_price:
                result.append(current_node.info["name"])

        self._find_price(current_node.left, min_price, max_price, result)
        self._find_price(current_node.right, min_price, max_price, result)

    def find_exact_price(self, price):
        result = []
        self._find_exact_price(self.root, price, result)
        return result if result else "Deo co"

    def _find_exact_price(self, current_node, price, result):
        if current_node is None:
            return

        if current_node.key == price:
            result.append(current_node.info["name"])

        self._find_exact_price(current_node.left, price, result)
        self._find_exact_price(current_node.right, price, result)

# Danh sách điện thoại
phone_list = [
    {"name": "phone A", "price": 13},
    {"name": "phone B", "price": 20},
    {"name": "phone C", "price": 4},
    {"name": "phone D", "price": 2},
    {"name": "phone E", "price": 14},
    {"name": "phone F", "price": 22},
    {"name": "phone G", "price": 5}
]

phone_tree = BSTree()
for phone in phone_list:
    phone_tree.insert_node(phone)

min_price = 2
max_price = 7
exact_price = 20
exact_price2 = 10000

result_in_range = phone_tree.find_price(min_price, max_price)
result_exact_price = phone_tree.find_exact_price(exact_price)

print("Cai Cay", phone_tree.get_tree())
print("Dien Thoai Trong Khoang Gia {} Den {}: {}".format(min_price, max_price, result_in_range))
print("Dien Thoai Co Gia Tri La {}: {}".format(exact_price, result_exact_price))

result_exact_price2 = phone_tree.find_exact_price(exact_price2)
print("Dien Thoai Co Gia Tri La {}: {}".format(exact_price2, result_exact_price2))