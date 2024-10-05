
#>	Trung tâm đào tạo lập trình Techx cần lưu trữ thông tin quản lý với các thông tin như sau:
#		1/ Học viên:
#			- Đối tượng: HocVien(maHV, tenHV, ngaySinh, khoaHoc)
#			- Phương thức:
#				+ dangKyKhoaHoc(khoaHoc): Đăng ký một khóa học mới.
#				+ hienThiKhoaHoc(): Hiển thị danh sách khóa học đã đăng ký.Khóa học:
#		2/ Khóa học:
#			- Đối tượng: KhoaHoc(maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi)
#			- Phương thức:
#				+ thongTinKhoaHoc(): Hiển thị thông tin chi tiết về khóa học.
#		3/ Yêu cầu thực hiện:
#				+ Tạo các lớp đối tượng cho Học viên, Khóa học.
#				+ Định nghĩa các phương thức theo yêu cầu.
#				+ Tạo một số đối tượng (ít nhất 2 học viên, 2 khóa học) và thực hiện một số thao tác trên chúng (đăng ký khóa học, hiển thị khóa học ).


# Định nghĩa lớp KhoaHoc
class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi
    
    def thongTinKhoaHoc(self):
        return f"+ Mã khóa học: {self.maKhoaHoc}, Tên khóa học: {self.tenKhoaHoc}, Hình thức: {self.hinhThuc}, Học phí: {self.hocPhi} VND"

# Định nghĩa lớp HocVien
class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = []
    
    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)
    
    def hienThiKhoaHoc(self):
        if self.khoaHoc:
            print(f"Học viên {self.tenHV} đã đăng ký các khóa học sau:")
            for khoa in self.khoaHoc:
                print(khoa.thongTinKhoaHoc())
        else:
            print(f"+ Học viên {self.tenHV} chưa đăng ký khóa học nào.")

# Quản lý Học viên và Khóa học
class QuanLy:
    def __init__(self):
        self.danhSachHocVien = []
        self.danhSachKhoaHoc = []
    
    def themHocVien(self, maHV, tenHV, ngaySinh):
        hocVien = HocVien(maHV, tenHV, ngaySinh)
        self.danhSachHocVien.append(hocVien)
        print(f"+ Đã thêm học viên: {tenHV}")
    
    def themKhoaHoc(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        khoaHoc = KhoaHoc(maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi)
        self.danhSachKhoaHoc.append(khoaHoc)
        print(f"+ Đã thêm khóa học: {tenKhoaHoc}")
    
    def dangKyKhoaHoc(self, maHV, maKhoaHoc):
        hocVien = next((hv for hv in self.danhSachHocVien if hv.maHV == maHV), None)
        khoaHoc = next((kh for kh in self.danhSachKhoaHoc if kh.maKhoaHoc == maKhoaHoc), None)
        
        if hocVien and khoaHoc:
            hocVien.dangKyKhoaHoc(khoaHoc)
            print(f"+ Học viên {hocVien.tenHV} đã đăng ký khóa học {khoaHoc.tenKhoaHoc}.")
        else:
            print("+ Không tìm thấy học viên hoặc khóa học.")
    
    def hienThiKhoaHocCuaHocVien(self, maHV):
        hocVien = next((hv for hv in self.danhSachHocVien if hv.maHV == maHV), None)
        if hocVien:
            hocVien.hienThiKhoaHoc()
        else:
            print("+ Không tìm thấy học viên.")
    
    def thongTinKhoaHoc(self, maKhoaHoc):
        khoaHoc = next((kh for kh in self.danhSachKhoaHoc if kh.maKhoaHoc == maKhoaHoc), None)
        if khoaHoc:
            print(khoaHoc.thongTinKhoaHoc())
        else:
            print("+ Không tìm thấy khóa học.")

# Ví dụ sử dụng
quanLy = QuanLy()

# Thêm học viên
quanLy.themHocVien("HV01", "Nguyen Van A", "1990-01-01")
quanLy.themHocVien("HV02", "Le Thi B", "1992-02-02")

# Thêm khóa học
quanLy.themKhoaHoc("KH01", "Lập trình Python", "Online", 2000000)
quanLy.themKhoaHoc("KH02", "Phân tích dữ liệu", "Offline", 3000000)

# Đăng ký khóa học
quanLy.dangKyKhoaHoc("HV01", "KH01")
quanLy.dangKyKhoaHoc("HV01", "KH02")
quanLy.dangKyKhoaHoc("HV02", "KH02")

# Hiển thị khóa học đã đăng ký của học viên
quanLy.hienThiKhoaHocCuaHocVien("HV01")
quanLy.hienThiKhoaHocCuaHocVien("HV02")

# Thông tin khóa học
quanLy.thongTinKhoaHoc("KH01")