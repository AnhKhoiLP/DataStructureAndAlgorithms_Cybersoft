import customtkinter as ctk
ctk.set_appearance_mode("dark")

#* Yêu Cầu Người Dùng Nhập Số Lượng Nút Từ Terminal
	# try:
	#     number_buttons = int(input("Nhập số lượng nút bạn muốn tạo:"))
	# except ValueError:
	#     print("Vui lòng nhập một số nguyên hợp lệ.")
	#     exit()

number_buttons = 1000

#* Khởi Tạo Cửa Sổ Chính
main_window = ctk.CTk()
main_window.title("Cybersoft")
main_window.geometry("400x600")
main_window.resizable(False, True)

#* Tạo Container Để Cho Phép Cuộn
container = ctk.CTkCanvas(master = main_window, bg = "#A9A9A9")
container.pack(side = "left", fill = "both", expand = True)

#* Tạo Thanh Cuộn
scrollbar = ctk.CTkScrollbar(main_window, orientation = "vertical", command = container.yview)
scrollbar.pack(side = "right", fill = "y")

#* Liên Kết Thanh Cuộn Với container
container.configure(yscrollcommand = scrollbar.set)

button_frame = ctk.CTkFrame(container)
container.create_window((0, 0), window = button_frame, anchor = "n")

#* Số Lượng Nút Hiển Thị Ban Đầu Và Đã Load
initial_button_count = 20
buttons_loaded = 0

#* Tạo Nút Ban Đầu
def load_buttons():
    global buttons_loaded
    for i in range(buttons_loaded, min(buttons_loaded + initial_button_count, number_buttons)):
        button = ctk.CTkButton(
            master = button_frame,
            text = f"Button {i + 1} !",
            corner_radius = 8,
            width = 370,
            height = 10,
            font = ("Courier New", 15),
            border_spacing = 1,
            fg_color = "#C5F8E4",
            hover_color = "#0B9560",
            text_color = "#000000"
        )
        button.pack(padx = 5, pady = 5)
    buttons_loaded +=  initial_button_count
    update_scroll_region()

#* Cập Nhật Vùng Cuộn
def update_scroll_region(event = None):
    button_frame.update_idletasks()
    container.config(scrollregion = container.bbox("all"))

#* Tải Thêm Nút Khi Cuộn Gần Cuối
def on_scroll(event):
    container.yview_scroll(int(-1*(event.delta//120)), "units")
    if container.yview()[1] > 0.9:
        if buttons_loaded < number_buttons:
            load_buttons()

#* Gọi Hàm Tạo Nút Ban Đầu
load_buttons()

#* Gắn Sự Kiện Cuộn Chuột Và Kiểm Tra Vị Trí Cuộn
main_window.bind_all("<MouseWheel>", on_scroll)
container.bind("<Configure>", update_scroll_region)

#* Chạy Giao Diện
main_window.mainloop()
