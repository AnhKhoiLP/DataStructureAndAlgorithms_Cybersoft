import customtkinter as ctk

# Khởi tạo cửa sổ chính
window = ctk.CTk()
window.title("cybersoft")
window.geometry("400x600")  # Đặt kích thước cửa sổ chính

# Tạo một khung chính cho các nút và thanh cuộn
main_frame = ctk.CTkFrame(window)
main_frame.pack(side="left", fill="both", expand=True)

# Tạo thanh cuộn
scrollbar = ctk.CTkScrollbar(window, orientation="vertical")
scrollbar.pack(side="right", fill="y")

# Tạo một canvas để chứa các nút
canvas = ctk.CTkCanvas(main_frame, bg="grey")
canvas.pack(side="left", fill="both", expand=True)

# Liên kết thanh cuộn với canvas
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=canvas.yview)

# Tạo một frame chứa các nút
button_frame = ctk.CTkFrame(canvas)
canvas.create_window((0, 0), window=button_frame, anchor="nw")

# Tạo 1000 nút
for i in range(1000):
    button = ctk.CTkButton(button_frame, text=f"Button {i+1} !")
    button.pack(pady=5)  # Thêm khoảng cách giữa các nút

# Cập nhật kích thước của frame chứa nút
button_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))  # Thiết lập vùng cuộn

# Chạy giao diện
window.mainloop()
