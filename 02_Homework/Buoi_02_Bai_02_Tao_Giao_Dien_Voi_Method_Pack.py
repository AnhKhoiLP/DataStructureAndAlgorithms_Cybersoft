import customtkinter as CTk

#* Khởi Tạo Cửa Sổ Chính
window = CTk.CTk()
window.title("Lê Phước Anh Khôi")
window.geometry("800x600")

#* Người Dùng Không Được Phép Thay Đổi Kích Thước Cửa Sổ
window.resizable(False, False)

#* Tạo 2 Frame Cha Chứa Các Frame Con
top_frame 		= CTk.CTkFrame(window)
bottom_frame 	= CTk.CTkFrame(window)

#* Custom Top + Bot Frame
top_frame	.pack(side = "top"		, fill = "both", expand = True)
bottom_frame.pack(side = "bottom"	, fill = "both", expand = True)

#* Tạo 4 Frame
frame01 = CTk.CTkFrame(top_frame	, fg_color = "yellow")
frame02 = CTk.CTkFrame(top_frame	, fg_color = "red")
frame03 = CTk.CTkFrame(bottom_frame	, fg_color = "gray")
frame04 = CTk.CTkFrame(bottom_frame	, fg_color = "blue")

frame01.pack(side = "left", fill = "both", expand = True)		
frame02.pack(side = "left", fill = "both", expand = True)		
frame03.pack(side = "left", fill = "both", expand = True)		
frame04.pack(side = "left", fill = "both", expand = True)		

#* Chạy giao diện
window.mainloop()