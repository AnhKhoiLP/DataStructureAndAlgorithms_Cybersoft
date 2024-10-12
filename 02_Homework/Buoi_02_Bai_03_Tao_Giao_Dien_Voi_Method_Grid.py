import customtkinter as ctk

#* Khởi tạo cửa sổ chính
window = ctk.CTk()
window.title("cybersoft")
window.geometry("800x600")

#* Người Dùng Không Được Phép Thay Đổi Kích Thước Cửa Sổ
window.resizable(False, False)

#* Tạo 4 Frame
frame01 = ctk.CTkFrame(window, fg_color="yellow")
frame02 = ctk.CTkFrame(window, fg_color="red")
frame03 = ctk.CTkFrame(window, fg_color="gray")
frame04 = ctk.CTkFrame(window, fg_color="blue")

frame01.grid(row=0, column=0, sticky="nsew")#? Frame 01 - Top.Left 		- Yellow
frame02.grid(row=0, column=1, sticky="nsew")#? Frame 02 - Top.Right 	- Red
frame03.grid(row=1, column=0, sticky="nsew")#? Frame 03 - Bottom.Left 	- Gray
frame04.grid(row=1, column=1, sticky="nsew")#? Frame 04 - Bottom.Right 	- Blue

#* Cài đặt tỉ lệ cho các hàng và cột
window.grid_rowconfigure	(0, weight=1)
window.grid_rowconfigure	(1, weight=1)
window.grid_columnconfigure	(0, weight=1)
window.grid_columnconfigure	(1, weight=1)

#* Chạy giao diện
window.mainloop()