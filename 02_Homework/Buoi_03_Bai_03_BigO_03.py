while (i < n):
	while (a < n):
		while(b < n):
			b = b + 1
		a = a + 1
	while (c < n):
		c = c + 1
	i = i + 100

#* Phân Tích
	#| Đối Với Vòng Lặp Xác Định Số Lần Lặp Và Cách Chúng Phụ Thuộc Vào Kích Thước Đầu Vào:
		#+ Khởi Tạo:
			## Biến i, a, b, và c được khởi tạo
			## Giả sử a = 0, b = 0, c = 0 và i = 0
		#+ 01 - Vòng Lặp while (i < n)
			## Vòng lặp chạy từ i = 0 cho đến i < n.
			## Mỗi lần lặp, giá trị của i được tăng thêm 100.
				#? Số Lần Lặp Được Tính Là: 2n/100
		#+ 02 - Vòng Lặp while (a < n) Và Vòng Lặp while (b < n)
			## Cả 2 đều bắt đầu từ a = 0 và b = 0
			## Mỗi lần lặp, giá trị của a tăng thêm 1 và b được tăng thêm n.
			## Số lần lặp của mỗi vòng là: n
				#? Số Lần Lặp Được Tính Là: 2n * 2n = 4n^2
		#+ 03 - Vòng Lặp while (c < n)
			## Vòng này bắt đầu c = 0
			## Mỗi lần lặp, giá trị của i được tăng thêm 1.
				#? Số Lần Lặp Được Tính Là: 2n
	#| Biểu thức F(N):
		#+ Tổng Số Lần Lặp Của Mỗi Lần Lặp Vòng Lặp while (i < n) Là: F(N) = (n^2 + n)
		#+ Tổng Số Lần Lặp Của while (i < n) Tính Luôn Cả Phép Gán: F(N) = (4n^2 + 2n) * (2n / 100)
	#| Độ Phức Tạp Thời Gian Chạy:
		#+ Xác Định F(N):
			## F(N) = (4n^2 + 2n) * (2n / 100)
			## 		= ((4n^2 + 2n)*2n) / 100
			## 		= ((4n^2 * 2n) + (2n * 2n)) / 100
			## 		= (8n^3 + n^2)/100
		#+ Bỏ Qua Hằng Số Ta Có:
			## F(N) = O(n^3) + O(n^2)
		#+ Xác Định Phần Có Tốc Độ Tăng Trưởng Lớn Nhất
			## F(N) ≈ O(n^3) khi n -> ∞
		#+ Ký Hiệu Big O: O(n^3)