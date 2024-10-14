i = 0
while (i < n):
	i = i + 100

#* Phân Tích
	#| Đối Với Vòng Lặp Xác Định Số Lần Lặp Và Cách Chúng Phụ Thuộc Vào Kích Thước Đầu Vào:
		#+ Khởi Tạo:
			## Biến i = 0.
		#+ Vòng Lặp while
			## Vòng lặp chạy cho đến khi giá trị của i >= n.
				#? Thao Tác 01: Kiểm tra điều kiện i < n
				#? Thao Tác 02: Thực hiện phép gán i = i + 100
			## Mỗi lần lặp, giá trị của i được tăng thêm 100.
		#+ Số Lần Lặp Được Tính Là: 2n/100
	#| Độ Phức Tạp Thời Gian Chạy:
		#+ Mỗi lần lặp thực hiện thao tác gán giá trị i = i + 100 đây là một thao tác có độ phức tạp O(1)
		#+ Ký Hiệu Big O: O(n)
	#| Biểu thức F(N):
		#+ F(N)=1 + 2n/100
			## 1: Đại diện cho thao tác khởi tạo i = 0 (O(1)).
			## 2n: Đại diện cho việc vòng lặp thực hiện n lần với mỗi lần bao gồm hai thao tác chính: kiểm tra điều kiện i < n và gán i = i + 1. Mỗi thao tác trong mỗi vòng lặp có độ phức tạp O(1), và hai thao tác gộp lại là 2n.