import customtkinter as ctk

# Khởi Tạo Cửa Sổ Chính
window = ctk.CTk()
window.title("Cybersoft")
window.geometry("400x600")  # Đặt kích thước cửa sổ chính
ctk.set_appearance_mode("dark")

# Tạo Canvas để cho phép cuộn
canvas = ctk.CTkCanvas(master = window, bg = "white")
canvas.pack(side="left", fill="none", expand=True)

# Tạo Thanh Cuộn
scrollbar = ctk.CTkScrollbar(window, orientation="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Liên Kết Thanh Cuộn Với Canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Tạo Frame con bên trong Canvas
button_frame = ctk.CTkFrame(canvas)
canvas.create_window((0, 0), window=button_frame, anchor="nw")

# Ngăn không cho frame tự động điều chỉnh kích thước
button_frame.pack_propagate(False)

#Số Nút
number_buttons = 5

# Tạo 1000 Nút
for i in range(number_buttons):
	button = ctk.CTkButton(
		master=button_frame,
		text=f"Button {i + 1} !",
		corner_radius=8,
		width=200,
		height=30,
		font=("Courier New", 12),
		border_spacing=10
	)
	button.pack(side="top", padx = 20, pady = 5)  # Thêm khoảng cách giữa các nút

# Cập Nhật Kích Thước Của Frame Chứa Nút
def update_scroll_region(event=None):
	# Cập nhật kích thước của button_frame
	button_frame.update_idletasks()  # Cập nhật kích thước
	canvas.config(scrollregion=canvas.bbox("all"))  # Cập nhật vùng cuộn

	# # Đặt chiều cao cho button_frame theo số lượng nút
	# button_frame_height = 30 * number_buttons + 20 * number_buttons - 1  # Chiều cao của 1000 nút + khoảng cách
	# button_frame.configure(height = button_frame_height)

# Gọi hàm cập nhật khi cửa sổ được tạo
update_scroll_region()

# Gắn sự kiện để cập nhật lại khi khung được thay đổi kích thước
window.bind("<Configure>", update_scroll_region)

# Gắn sự kiện cuộn khi cuộn chuột
window.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta//120)), "units"))

# Chạy Giao Diện
window.mainloop()
