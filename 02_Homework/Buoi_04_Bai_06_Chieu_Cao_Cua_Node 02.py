
#+ [NÚT A LÀ NÚT ĐƯỢC KHOANH TRÒN]
#          A
#       /  |  \
#      B   Z    C
#     / \     /  \ \
#    D   E   F   G   Z
#            |
#            H

## Tìm Và Xác Định Vị Trí Của Nút Được Khoanh Tròn
	#+ Chiều Cao Của Một Nút: Được Định Nghĩa Là Số Bước Lớn Nhất Từ Nút Đó Đến Nút Lá (Nút Không Có Con)
## Tìm Các Nút Lá Mà Từ Nút Được Khoanh Tròn Có Thể Đạt Đến.
	#+ Từ Nút Z
		#| Nút Z Không Có Bất Kỳ Con Nào
		#| Do Đó, Chính Nó Là Một Nút Lá
## Tính Toán Số Bước Từ Nút Được Khoanh Tròn Đến Nút Lá Xa Nhất
	#+ (2 Bước) - Đường Đi Từ Nút Z Đến Nút D: Z → B → D
	#+ (2 Bước) - Đường Đi Từ Nút Z Đến Nút E: Z → B → E
	#+ (3 Bước) - Đường Đi Từ Nút Z Đến Nút H: Z → C → F → H
	#+ (2 Bước) - Đường Đi Từ Nút Z Đến Nút G: Z → C → G
## Depth, Height, Size, Level Của Cả Cây
#*	|	Node	|	Depth	|	Height	|	Size	|	Level	|
#*	|	 A  	|	  0  	|	  3   	|	 10  	|	  0  	|
#*	|	 B  	|	  1  	|	  1   	|	  3  	|	  1  	|
#*	|	 C  	|	  1  	|	  2   	|	  4  	|	  1  	|
#*	|	 D  	|	  2  	|	  0   	|	  1  	|	  2  	|
#*	|	 E  	|	  2  	|	  0   	|	  1  	|	  2  	|
#*	|	 F  	|	  2  	|	  1   	|	  2  	|	  2  	|
#*	|	 G  	|	  2  	|	  0   	|	  1  	|	  2  	|
#*	|	 H  	|	  3  	|	  0   	|	  1  	|	  3  	|
#*	|	 Z  	|	  1  	|	  0   	|	  1  	|	  1  	|
## Depth, Height, Size, Level Từ Nút Z
#*	|	Node	|	Depth	|	Height	|	Size	|	Level	|
#*	|	 Z  	|	  1  	|	  0   	|	  1  	|	  1  	|