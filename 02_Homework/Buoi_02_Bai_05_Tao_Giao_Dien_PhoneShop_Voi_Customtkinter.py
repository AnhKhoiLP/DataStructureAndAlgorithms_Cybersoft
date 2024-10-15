import customtkinter as ctk

danh_sach_dien_thoai = [
	{
		"index": 1,
		"name": "iPhone",
		"Announced": "09-01-2007",
		"Discontinued": "11-07-2008",
		"Realese OS": "iPhone OS 1.0",
		"Date Realease": "29-06-2007"
	}
]

#* Khởi Tạo Cửa Sổ Chính
window = ctk.CTk()
window.title("Phone Shop")
window.geometry("1920x1080")  #* Đặt kích thước cửa sổ chính
window.resizable(False, True)



#* Chạy Giao Diện
window.mainloop()
