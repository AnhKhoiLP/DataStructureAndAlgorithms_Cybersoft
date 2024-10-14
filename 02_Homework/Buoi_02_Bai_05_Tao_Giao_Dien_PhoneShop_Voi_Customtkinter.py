import customtkinter as ctk

#* Khởi Tạo Cửa Sổ Chính
window = ctk.CTk()
window.title("cybersoft")
window.geometry("400x600")  #* Đặt kích thước cửa sổ chính

#* Tạo Một Khung Chính Cho Các Nút Và Thanh Cuộn
main_frame = ctk.CTkFrame(window)
main_frame.pack(side="left", fill="both", expand=True)

#* Tạo Thanh Cuộn
scrollbar = ctk.CTkScrollbar(window, orientation="vertical")
scrollbar.pack(side="right", fill="y")

#* Tạo Một Canvas Để Chứa Các Nút
canvas = ctk.CTkCanvas(main_frame, bg="grey")
canvas.pack(side="left", fill="both", expand=True)

#* Liên Kết Thanh Cuộn Với canvas
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=canvas.yview)

#* Tạo Một Frame Chứa Các Nút
button_frame = ctk.CTkFrame(canvas)
canvas.create_window((0, 0), window=button_frame, anchor="nw")

#* Tạo 1000 Nút
for i in range(1000):
    button = ctk.CTkButton(button_frame, text=f"Button {i+1} !")
    button.pack(pady=5)  #* Thêm khoảng cách giữa các nút

#* Cập Nhật Kích Thước Của Frame Chứa Nút
button_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

#* Chạy Giao Diện
window.mainloop()
