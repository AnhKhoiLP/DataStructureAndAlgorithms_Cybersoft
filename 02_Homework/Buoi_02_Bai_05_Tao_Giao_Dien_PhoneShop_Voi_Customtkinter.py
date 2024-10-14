import customtkinter as ctk

danh_sach_dien_thoai = [
	{
		index: 1,
		
	}
]

#* Khởi Tạo Cửa Sổ Chính
window = ctk.CTk()
window.title("Phone Shop")
window.geometry("1920x1080")  #* Đặt kích thước cửa sổ chính
window.resizable(False, True)



#* Chạy Giao Diện
window.mainloop()
