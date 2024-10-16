import customtkinter as ctk

danh_sach_dien_thoai = [
	{
		"index": 1,
		"name": "iPhone",
		"Announced": "09-01-2007",
		"Discontinued": "11-07-2008",
		"Release OS": "iPhone OS 1.0",
		"Release Date": "29-06-2007"
	},
	{
		"index": 2,
		"name": "iPhone 3G",
		"Announced": "09-06-2008",
		"Discontinued": "07-06-2010",
		"Release OS": "iOS 2.0",
		"Release Date": "11-07-2008"
	},
	{
		"index": 3,
		"name": "iPhone 3GS",
		"Announced": "08-06-2008",
		"Discontinued": "12-09-2012",
		"Release OS": "iOS 3.0",
		"Release Date": "19-06-2009"
	},
	{
		"index": 4,
		"name": "iPhone 4",
		"Announced": "07-06-2010",
		"Discontinued": "10-09-2013",
		"Release OS": "iOS 4.0",
		"Release Date": "24-06-2010"
	},
	{
		"index": 5,
		"name": "iPhone 4s",
		"Announced": "04-10-2011",
		"Discontinued": "09-09-2014",
		"Release OS": "iOS 5.0",
		"Release Date": "14-10-2011"
	},
	{
		"index": 6,
		"name": "iPhone 5",
		"Announced": "12-09-2012",
		"Discontinued": "10-09-2013",
		"Release OS": "iOS 6.0",
		"Release Date": "21-09-2012"
	},
	{
		"index": 7,
		"name": "iPhone 5c",
		"Announced": "10-09-2013",
		"Discontinued": "09-09-2015",
		"Release OS": "iOS 7.0",
		"Release Date": "20-09-2013"
	},
	{
		"index": 8,
		"name": "iPhone 5s",
		"Announced": "10-09-2013",
		"Discontinued": "21-03-2016",
		"Release OS": "iOS 7.0",
		"Release Date": "20-09-2013"
	},
	{
		"index": 9,
		"name": "iPhone 6",
		"Announced": "09-09-2014",
		"Discontinued": "07-09-2016",
		"Release OS": "iOS 8.0",
		"Release Date": "19-09-2014"
	},
	{
		"index": 10,
		"name": "iPhone 6 Plus",
		"Announced": "09-09-2014",
		"Discontinued": "07-09-2016",
		"Release OS": "iOS 8.0",
		"Release Date": "19-09-2014"
	},
	{
		"index": 11,
		"name": "iPhone 6s",
		"Announced": "09-09-2015",
		"Discontinued": "12-09-2018",
		"Release OS": "iOS 9.0",
		"Release Date": "25-09-2015"
	},
	{
		"index": 12,
		"name": "iPhone 6s Plus",
		"Announced": "09-09-2015",
		"Discontinued": "12-09-2018",
		"Release OS": "iOS 9.0",
		"Release Date": "25-09-2015"
	},
	{
		"index": 13,
		"name": "iPhone SE",
		"Announced": "21-03-2016",
		"Discontinued": "12-09-2018",
		"Release OS": "iOS 9.3",
		"Release Date": "31-03-2016"
	},
	{
		"index": 14,
		"name": "iPhone 7",
		"Announced": "07-09-2016",
		"Discontinued": "10-09-2019",
		"Release OS": "iOS 10.0",
		"Release Date": "16-09-2016"
	},
	{
		"index": 15,
		"name": "iPhone 7 Plus",
		"Announced": "07-09-2016",
		"Discontinued": "10-09-2019",
		"Release OS": "iOS 10.0",
		"Release Date": "16-09-2016"
	},
	{
		"index": 16,
		"name": "iPhone 8",
		"Announced": "12-09-2017",
		"Discontinued": "15-04-2020",
		"Release OS": "iOS 11.0",
		"Release Date": "22-09-2017"
	},
	{
		"index": 17,
		"name": "iPhone 8 Plus",
		"Announced": "12-09-2017",
		"Discontinued": "15-04-2020",
		"Release OS": "iOS 11.0",
		"Release Date": "22-09-2017"
	},
	{
		"index": 18,
		"name": "iPhone X",
		"Announced": "12-09-2017",
		"Discontinued": "12-09-2018",
		"Release OS": "iOS 11.0",
		"Release Date": "03-11-2017"
	},
	{
		"index": 19,
		"name": "iPhone XR",
		"Announced": "12-09-2018",
		"Discontinued": "14-09-2021",
		"Release OS": "iOS 12.0",
		"Release Date": "26-10-2018"
	},
	{
		"index": 20,
		"name": "iPhone XS",
		"Announced": "12-09-2018",
		"Discontinued": "10-09-2019",
		"Release OS": "iOS 12.0",
		"Release Date": "21-09-2018"
	},
	{
		"index": 21,
		"name": "iPhone XS Max",
		"Announced": "12-09-2018",
		"Discontinued": "10-09-2019",
		"Release OS": "iOS 12.0",
		"Release Date": "21-09-2018"
	},
	{
		"index": 22,
		"name": "iPhone 11",
		"Announced": "10-09-2019",
		"Discontinued": "07-09-2022",
		"Release OS": "iOS 13.0",
		"Release Date": "20-09-2019"
	},
	{
		"index": 23,
		"name": "iPhone 11 Pro",
		"Announced": "10-09-2019",
		"Discontinued": "13-10-2020",
		"Release OS": "iOS 13.0",
		"Release Date": "20-09-2019"
	},
	{
		"index": 24,
		"name": "iPhone 11 Pro Max",
		"Announced": "10-09-2019",
		"Discontinued": "13-10-2020",
		"Release OS": "iOS 13.0",
		"Release Date": "20-09-2019"
	},
	{
		"index": 25,
		"name": "iPhone SE",
		"Announced": "15-04-2020",
		"Discontinued": "08-03-2022",
		"Release OS": "iOS 13.4",
		"Release Date": "24-04-2020"
	},
	{
		"index": 26,
		"name": "iPhone 12",
		"Announced": "13-10-2020",
		"Discontinued": "12-09-2023",
		"Release OS": "iOS 14.1",
		"Release Date": "23-10-2020"
	},
	{
		"index": 27,
		"name": "iPhone 12 Mini",
		"Announced": "13-10-2020",
		"Discontinued": "07-09-2022",
		"Release OS": "iOS 14.2",
		"Release Date": "13-11-2020"
	},
	{
		"index": 28,
		"name": "iPhone 12 Pro",
		"Announced": "13-10-2020",
		"Discontinued": "14-09-2021",
		"Release OS": "iOS 14.1",
		"Release Date": "23-10-2020"
	},
	{
		"index": 29,
		"name": "iPhone 12 Pro Max",
		"Announced": "13-10-2020",
		"Discontinued": "14-09-2021",
		"Release OS": "iOS 14.2",
		"Release Date": "13-11-2020"
	},
	{
		"index": 30,
		"name": "iPhone 13",
		"Announced": "14-09-2021",
		"Discontinued": "09-09-2024",
		"Release OS": "iOS 15.0",
		"Release Date": "24-09-2021"
	},
	{
		"index": 31,
		"name": "iPhone 13 Mini",
		"Announced": "14-09-2021",
		"Discontinued": "21-09-2023",
		"Release OS": "iOS 15.0",
		"Release Date": "24-09-2021"
	},
	{
		"index": 32,
		"name": "iPhone 13 Pro",
		"Announced": "14-09-2021",
		"Discontinued": "07-09-2022",
		"Release OS": "iOS 15.0",
		"Release Date": "24-09-2021"
	},
	{
		"index": 33,
		"name": "iPhone 13 Pro Max",
		"Announced": "14-09-2021",
		"Discontinued": "07-09-2022",
		"Release OS": "iOS 15.0",
		"Release Date": "24-09-2021"
	},
	{
		"index": 34,
		"name": "iPhone SE",
		"Announced": "08-03-2022",
		"Discontinued": "In production",
		"Release OS": "iOS 15.4",
		"Release Date": "18-03-2022"
	},
	{
		"index": 35,
		"name": "iPhone 14",
		"Announced": "07-09-2022",
		"Discontinued": "In production",
		"Release OS": "iOS 16.0",
		"Release Date": "16-09-2022"
	},
	{
		"index": 36,
		"name": "iPhone 14 Plus",
		"Announced": "07-09-2022",
		"Discontinued": "In production",
		"Release OS": "iOS 16.0",
		"Release Date": "07-10-2022"
	},
	{
		"index": 37,
		"name": "iPhone 14 Pro",
		"Announced": "07-09-2022",
		"Discontinued": "12-09-2023",
		"Release OS": "iOS 16.0",
		"Release Date": "16-09-2022"
	},
	{
		"index": 38,
		"name": "iPhone 14 Pro Max",
		"Announced": "07-09-2022",
		"Discontinued": "12-09-2023",
		"Release OS": "iOS 16.0",
		"Release Date": "16-09-2022"
	},
	{
		"index": 39,
		"name": "iPhone 15",
		"Announced": "12-09-2023",
		"Discontinued": "In production",
		"Release OS": "iOS 17.0",
		"Release Date": "22-09-2023"
	},
	{
		"index": 40,
		"name": "iPhone 15 Plus",
		"Announced": "12-09-2023",
		"Discontinued": "In production",
		"Release OS": "iOS 17.0",
		"Release Date": "22-09-2023"
	},
	{
		"index": 41,
		"name": "iPhone 15 Pro",
		"Announced": "12-09-2023",
		"Discontinued": "09-09-2024",
		"Release OS": "iOS 17.0",
		"Release Date": "22-09-2023"
	},
	{
		"index": 42,
		"name": "iPhone 15 Pro Max",
		"Announced": "12-09-2023",
		"Discontinued": "09-09-2024",
		"Release OS": "iOS 17.0",
		"Release Date": "22-09-2023"
	},
	{
		"index": 43,
		"name": "iPhone 16",
		"Announced": "09-09-2024",
		"Discontinued": "In production",
		"Release OS": "iOS 18.0",
		"Release Date": "20-09-2024"
	},
	{
		"index": 44,
		"name": "iPhone 16 Plus",
		"Announced": "09-09-2024",
		"Discontinued": "In production",
		"Release OS": "iOS 18.0",
		"Release Date": "20-09-2024"
	},
	{
		"index": 45,
		"name": "iPhone 16 Pro",
		"Announced": "09-09-2024",
		"Discontinued": "In production",
		"Release OS": "iOS 18.0",
		"Release Date": "20-09-2024"
	},
	{
		"index": 46,
		"name": "iPhone 16 Pro Max",
		"Announced": "09-09-2024",
		"Discontinued": "In production",
		"Release OS": "iOS 18.0",
		"Release Date": "20-09-2024"
	}]

# Khởi tạo cửa sổ chính
window = ctk.CTk()
window.title("Phone Shop")
window.geometry("1920x1080")
window.resizable(True, True)

frame_dien_thoai = ctk.CTkCanvas(window, width=1920)
frame_dien_thoai.pack(side="right", fill="both", expand=True)

frame_noi_dung = ctk.CTkFrame(frame_dien_thoai)
frame_dien_thoai.create_window((0, 0), window=frame_noi_dung, anchor="nw")

def tao_the_dien_thoai(frame, dien_thoai):
	phone_frame = ctk.CTkFrame(frame, width=400, height=600, corner_radius = 20) 
	phone_frame.pack_propagate(False)
	phone_frame.pack(side = "left", padx = 40, pady = 20)

	phone_image = ctk.CTkImage(light_image = Image.open('DataStructureAndAlgorithms_Cybersoft\02_Homework\00_Install\02_Homework'))

	phone_label = ctk.CTkLabel(phone_frame, text=dien_thoai["name"], font=("Courier New", 20))
	phone_label.pack(pady=10)

	announced_label = ctk.CTkLabel(phone_frame, text=f"Announced")
	announced_label.pack()

	announced_label = ctk.CTkLabel(phone_frame, text=f"{dien_thoai['Announced']}")
	announced_label.pack()

	os_label = ctk.CTkLabel(phone_frame, text=f"{dien_thoai['Release OS']}")
	os_label.pack()

	button = ctk.CTkButton(
			master = phone_frame,
			text = "Mua Hàng",
			corner_radius = 8,
			width = 200,
			height = 20,
			font = ("Courier New", 15),
			border_spacing = 1,
			fg_color = "#C5F8E4",
			hover_color = "#0B9560",
			text_color = "#000000"
		)
	button.pack(padx = 5, pady = 5)

scrollbar = ctk.CTkScrollbar(frame_dien_thoai, orientation="vertical", command=frame_dien_thoai.yview)
scrollbar.pack(side="right", fill="both")
frame_dien_thoai.configure(yscrollcommand=scrollbar.set)

so_dien_thoai_moi_dong = 4
so_dien_thoai_moi_dot = 8
current_index = 0
def tai_them_dien_thoai():
	global current_index
	for i in range(so_dien_thoai_moi_dot):
		if current_index >= len(danh_sach_dien_thoai):
			break
		if current_index % so_dien_thoai_moi_dong == 0:
			dong_frame = ctk.CTkFrame(frame_noi_dung)
			dong_frame.pack(fill="x")
		tao_the_dien_thoai(dong_frame, danh_sach_dien_thoai[current_index])
		current_index += 1
	frame_noi_dung.update_idletasks()
	frame_dien_thoai.config(scrollregion=frame_dien_thoai.bbox("all"))
def update_scroll_region(event = None):
	frame_dien_thoai.config(scrollregion = frame_dien_thoai.bbox("all"))
def on_scroll(event):
	frame_dien_thoai.yview_scroll(int(-1*(event.delta//120)), "units")
	if frame_dien_thoai.yview()[1] > 0.9:
		if current_index % so_dien_thoai_moi_dong == 0:
			tai_them_dien_thoai()

window.bind_all("<MouseWheel>", on_scroll)
frame_dien_thoai.bind("<Configure>", update_scroll_region)
tai_them_dien_thoai()

window.mainloop()