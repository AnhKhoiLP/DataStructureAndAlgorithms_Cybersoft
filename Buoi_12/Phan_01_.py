class NguoiNode:
    def __init__(self, giaTri):
        self.giaTri = giaTri
        self.conTrai = None
        self.conPhai = None
#+ CHÈN THÊM MỘT NODE
def chenNodetoCay(cay, giaTri):
    if cay is None:
        return NguoiNode(giaTri)
    else:
        if giaTri < cay.giaTri:
            cay.conTrai = chenNodetoCay(cay.conTrai, giaTri)
        else:
            cay.conPhai = chenNodetoCay(cay.conPhai, giaTri)
    return cay
#+ IN THEO FORMAT
def inCay(cay, capDo=0, tienTo="Gốc: "):
    if cay is not None:
        print(" " * (capDo * 4) + tienTo + str(cay.giaTri))
        inCay(cay.conTrai, capDo + 1, "L--- ")
        inCay(cay.conPhai, capDo + 1, "R--- ")
# debai = [10, 7, 2, 1, 84, 100, 9, 20, 66, 44, 55, 3]
debai = [13, 20, 4, 2, 14, 22, 5]
cay = None
for giaTri in debai:
    cay = chenNodetoCay(cay, giaTri)
inCay(cay)

#? Phần 02
lstPhone =[
	{
		"name": "phone A",
		"price": 3
	},
	{
		"name": "phone B",
		"price": 2
	},
	{
		"name": "phone C",
		"price": 1
	},
	{
		"name": "phone D",
		"price": 1
	},
	{
		"name": "phone E",
		"price": 4
	},
	{
		"name": "phone F",
		"price": 10
	},
	{
		"name": "phone g",
		"price": 22
	}
]
