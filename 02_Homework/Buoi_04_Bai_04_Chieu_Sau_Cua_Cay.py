
#+ [NÚT C LÀ NÚT ĐƯỢC KHOANH TRÒN]
#         A
#       /   \
#      B     C
#     / \    / \
#    D   E  F   G

## Xác Định Nút Gốc
	#+ Nút Gốc Của Cây Là Nút A.
## Xác Định Cấu Trúc Của Cây
	#+ Các Nút Con Của A: B Và C Là Con Trực Tiếp Của A.
	#+ Các Nút Con Của B: D Và E Là Con Của B.
	#+ Các Nút Con Của C: F Và G Là Con Của C.
## Các Nút Liên Kết Với Nhau:
	#+ A Có 2 Con B Và C
		#| A → B
		#| A → C
	#+ B Có 2 Con D Và E
		#| B → D
		#| B → E
	#+ C Có 2 Con F Và G
		#| C → F
		#| C → G
## Đánh Giá Vị Trí Của Nút C Trong Cấu Trúc Cây.
	#+ Cấp Độ		: Nút C Nằm Ở Cấp Độ 1 (Tính Từ Gốc A Là Cấp Độ 0)
	#+ Vai Trò		: Nút C Là Nút Con Của Nút A Và Là Nút Cha Của Hai Nút F Và G.
	#+				  Nút C Thuộc Tầng Giữa Trong Cây, Đóng Vai Trò Như Một Nút Trung Gian, Liên Kết Giữa Gốc Và Các Nút Lá .
	#+ Loại Nút		: C Là Nút Trung Gian Nằm Giữa Gốc Và Các Nút Lá.
	#+ Chiều Sâu	: Chiều Sâu Của C Là 1, Nghĩa Là Nó Nằm Cách Gốc A Đúng 1 Cạnh.
## Bắt Đầu Từ Nút Gốc, Theo Dõi Đường Đi Đến Nút Được Khoanh Tròn.
	#+ A TỚI C
## Depth, Height, Size, Level Của Cả Cây
#*	|	Node	|	Depth	|	Height	|	Size	|	Level	|
#*	|	 A  	|	  0  	|	  2   	|	 7  	|	  0  	|
#*	|	 B  	|	  1  	|	  1   	|	 3  	|	  1  	|
#*	|	 C  	|	  1  	|	  1   	|	 3  	|	  1  	|
#*	|	 D  	|	  2  	|	  0   	|	 1  	|	  2  	|
#*	|	 E  	|	  2  	|	  0   	|	 1  	|	  2  	|
#*	|	 F  	|	  2  	|	  0   	|	 1  	|	  2  	|
#*	|	 G  	|	  2  	|	  0   	|	 1  	|	  2  	|
## Depth, Height, Size, Level Từ Nút C
#*	|	Node	|	Depth	|	Height	|	Size	|	Level	|
#*	|	 C  	|	  1  	|	  1   	|	 3  	|	  1  	|
#*	|	 F  	|	  2  	|	  0   	|	 1  	|	  2  	|
#*	|	 G  	|	  2  	|	  0   	|	 1  	|	  2  	|
