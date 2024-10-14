i = 0
while (i < n):
    i = i + 1

#* Phân Tích
	#| Đối Với Vòng Lặp Xác Định Số Lần Lặp Và Cách Chúng Phụ Thuộc Vào Kích Thước Đầu Vào:
		#+ Khởi Tạo:
			## Biến a được khởi tạo bằng 0 (độ phức tạp là O(1)).
			## Mỗi lần lặp, i tăng thêm 1.
			## Do đó, số lần lặp của vòng lặp sẽ là n lần, vì i phải đi từ 0 đến n - 1.
		#+ Vòng Lặp while
			## Vòng lặp chạy cho đến khi giá trị của a đạt giá trị n.
			## Mỗi lần lặp, giá trị của a được tăng thêm 1.
		#+ Số Lần Lặp Và Phụ Thuộc
			## 01 - a = 0 và dừng khi a = n.
			## 02 - a tăng lên 1 mỗi lần lặp
			## 03 - Vậy tổng số lần lặp của vòng lặp là n lần.
	#| Độ Phức Tạp Thời Gian Chạy:
		#+ Mỗi lần lặp thực hiện thao tác gán giá trị a = a + 1 đây là một thao tác có độ phức tạp O(1)
		#+ Ký Hiệu Big O: O(n)
	#| Biểu thức F(N):
		#+ F(N)=1+2n
			## 1: Đại diện cho thao tác khởi tạo a = 0 (O(1)).
			## 2n: Đại diện cho việc vòng lặp thực hiện n lần với mỗi lần bao gồm hai thao tác chính: kiểm tra điều kiện a < n và gán a = a + 1. Mỗi thao tác trong mỗi vòng lặp có độ phức tạp O(1), và hai thao tác gộp lại là 2n.