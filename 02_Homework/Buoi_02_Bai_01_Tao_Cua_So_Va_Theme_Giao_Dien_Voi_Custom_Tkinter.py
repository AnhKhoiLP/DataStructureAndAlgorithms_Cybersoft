
#* Import Custom Tkinter
import customtkinter

#* Modes:
	#+ System (Default)
	#+ Light
	#+ Dark
customtkinter.set_appearance_mode("System")

#* Thems:
	#+ blue (Default)
	#+ dark-blue
	#+ green
customtkinter.set_default_color_theme("blue")

#* Trong Python, CTk Là Viết Tắt Của CustomTkinter
#* CTk Window Là Cửa Sổ Giao Diện Người Dùng (Window) Được Tạo Bởi Thư Viện CustomTkinter
root = customtkinter.CTk()

#* Độ Phân Giải Màn Hình
root.geometry("500x300")

#* Người Dùng Không Được Phép Thay Đổi Kích Thước Cửa Sổ
root.resizable(False, False)

#* Tiêu Đề Cửa Sổ (Thanh Tiêu Đề Của Cửa Sổ Hiện Tên Của Bản)
root.title("Lê Phước Anh Khôi")

#* Chạy CustomTkinter
root.mainloop()