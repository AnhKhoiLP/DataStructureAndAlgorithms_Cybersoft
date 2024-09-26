
#> Hãy xây dựng một list sinh viên với các thuộc tính sau: mã sinh viên, tên sinh viên, điểm toán, điểm văn, điểm hóa.
# 	Tạo list gồm 5 sinh viên
# 	In thông tin các sinh viên có điểm trung bình lớn hơn 5
# 	In ra các sinh viên có điểm hoá dưới 5

class SinhVien:
	def __init__(self, ma_sv, ten_sv, diem_toan, diem_van, diem_hoa):
		self.ma_sv = ma_sv
		self.ten_sv = ten_sv
		self.diem_toan = diem_toan
		self.diem_van = diem_van
		self.diem_hoa = diem_hoa

	def tinh_diem_trung_binh(self):
		return (self.diem_toan + self.diem_van + self.diem_hoa) / 3    

	def __str__(self):
		return f"Mã SV: {self.ma_sv}, Tên SV: {self.ten_sv}, Điểm TB: {self.tinh_diem_trung_binh():.2f}, Điểm Hóa: {self.diem_hoa}"

sinh_vien_list = [
	SinhVien("SV001", "Nguyễn Văn A", 6, 7, 8),
	SinhVien("SV002", "Trần Thị B", 4, 5, 3),
	SinhVien("SV003", "Lê Văn C", 8, 9, 7),
	SinhVien("SV004", "Phạm Thị D", 5, 4, 6),
	SinhVien("SV005", "Đinh Văn E", 3, 2, 4)]

#$ In sinh viên có điểm trung bình lớn hơn 5
print("Danh sách sinh viên có điểm trung bình lớn hơn 5:")
for sv in sinh_vien_list:
		if sv.tinh_diem_trung_binh() > 5:
			print(sv)
#$ In sinh viên có điểm hóa dưới 5
print("\nDanh sách sinh viên có điểm hóa dưới 5:")
for sv in sinh_vien_list:
	if sv.diem_hoa < 5:
		print(sv)
