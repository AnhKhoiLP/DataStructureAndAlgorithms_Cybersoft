
#| Tạo List 3 SP
products =[
	{"index" : 1,"name" : "Laptop","price" : 1000,"description" : "Gaming Laptop"},
	{"index" : 2,"name" : "Smartphone","price" : 500,"description" : "Isung Phone"},
	{"index" : 3,"name" : "Massage Gun","price" : 2000,"description" : "Máy Massage Rung Lắc Châu Phi Cực Mạnh"}
	]
#| Duyệt
for product in products:
	print(product)
#| Thêm
products.append(
	{
		"index" : 4,
		"name" : "Smartphone",
		"price" : 700,
		"description" : "SungApple Phone"
	}
)
#|Thêm (Anh Sang Đòi)
def	them_sp():
	name = input("Nhap sp:")
	price = input("Nhap gia")
	id = max(product["id"] for product in products)+1
	des = input("Nhap mieu ta")
	products.append(
	{
		"index" : id,
		"name" : name,
		"price" : price,
		"description" : des
	}
)
#| Xóa
products = [product for product in products if product["id"] != 2]
#| Sửa
for product in products:
	if 	product["id"] 		== 	1:
		product["name"]		=	"Macbook"
		product["price"]	=	2000
#| Tìm
for product in products:
	if "Phone" in products["name"]:
		print(product)
