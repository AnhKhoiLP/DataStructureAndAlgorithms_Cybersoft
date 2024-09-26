//+ Code 02 Bài 01
	{
		"question_id": 1834,
		"input_format": "Array",
		"output_format": "Interger",
		"sample_input": "nums = [4,7,8,15,3,5]",
		"sample_output": "2",
		"_level": "hard",
		"created_at": "2023-11-01T19:12:04.460Z",
		"deleted_at": null,
		"en": {
			"question_title": "Split the Array to Make Coprime Products",
			"problem": "Return the number of divisions that satisfy this condition.",
			"explanation": "You are given a 0-indexed integer array nums of length n.\n\nA split at an index i where 0 <= i <= n - 2 is called valid if the product of the first i + 1 elements and the product of the remaining elements are coprime.\n\nFor example, if nums = [2, 3, 3], then a split at the index i = 0 is valid because 2 and 9 are coprime, while a split at the index i = 1 is not valid because 6 and 3 are not coprime. A split at the index i = 2 is not valid because i == n - 1.\nReturn the smallest index i at which the array can be split validly or -1 if there is no such split.\n\nTwo values val1 and val2 are coprime if gcd(val1, val2) == 1 where gcd(val1, val2) is the greatest common divisor of val1 and val2.\n\n\nExample 1:\n\n<img src = \"https://assets.leetcode.com/uploads/2022/12/14/second.PNG\" style=\"background: white\" width = \"300\"/>\n\nInput: nums = [4,7,8,15,3,5]\nOutput: 2\nExplanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.\nThe only valid split is at index 2.\n\nExample 2:\n\n<https://assets.leetcode.com/uploads/2022/12/14/capture.PNG\" style=\"background: white\" width = \"300\"/>\n\nInput: nums = [4,7,15,8,3,5]\nOutput: -1\nExplanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.\nThere is no valid split.",
			"constraint_input": "Array",
			"constraint_output": "Interger",
			"constraint_time": "10000"
		},
		"vi": {
			"question_title": "Chia mảng để tạo ra tích không chung",
			"problem": "Trả về số lượng cách chia thỏa mãn điều kiện đã cho.",
			"explanation": "Bạn được cho một mảng số nguyên không âm nums có độ dài n. \n\nMột phân chia tại chỉ số i trong đó 0 <= i <= n - 2 được gọi là hợp lệ nếu tích của i + 1 phần tử đầu tiên và tích của các phần tử còn lại là số nguyên tố.\n\nVí dụ, nếu nums = [2, 3, 3], thì một phân chia tại chỉ số i = 0 là hợp lệ vì 2 và 9 là số nguyên tố, trong khi một phân chia tại chỉ số i = 1 không hợp lệ vì 6 và 3 không phải số nguyên tố. Một phân chia tại chỉ số i = 2 cũng không hợp lệ vì i == n - 1.\n\nHãy trả về chỉ số i nhỏ nhất mà mảng có thể được phân chia hợp lệ hoặc -1 nếu không có phân chia nào hợp lệ.\n\nHai giá trị val1 và val2 được gọi là số nguyên tố nếu gcd(val1, val2) == 1, trong đó gcd(val1, val2) là ước chung lớn nhất của val1 và val2.\n\nVí dụ 1:\n\n<img src = \"https://assets.leetcode.com/uploads/2022/12/14/second.PNG\" style=\"background: white\" width = \"300\"/>\n\nInput: nums = [4, 7, 8, 15, 3, 5]\nOutput: 2\nGiải thích: Bảng trên hiển thị giá trị của tích của i + 1 phần tử đầu tiên, các phần tử còn lại và ước chung lớn nhất của chúng tại mỗi chỉ số i. Phân chia hợp lệ duy nhất là tại chỉ số 2.\n\nVí dụ 2:\n\n<https://assets.leetcode.com/uploads/2022/12/14/capture.PNG\" style=\"background: white\" width = \"300\"/>\n\nInput: nums = [4, 7, 15, 8, 3, 5]\nOutput: -1\nGiải thích: Bảng trên hiển thị giá trị của tích của i + 1 phần tử đầu tiên, các phần tử còn lại và ước chung lớn nhất của chúng tại mỗi chỉ số i. Không có phân chia nào hợp lệ.",
			"constraint_input": "Array",
			"constraint_output": "Interger",
			"constraint_time": "10000"
		},
		"test_case": [
			{
				"testcase_id": 0,
				"_input": "nums = [4,7,8,15,3,5]",
				"_output": "2"
			},
			{
				"testcase_id": 1,
				"_input": "nums = [4,7,15,8,3,5]",
				"_output": "-1"
			}
		],
		"init_code": [
			{
				"_language": "py",
				"tle": 10000,
				"_function": "import math\n\ndef findValidSplit(nums):\n  # Your code here",
				"base_code": "import math\n__function__\nprint(findValidSplit(__test_case__))",
				"_answer": "import math\n\ndef findValidSplit(nums):\n    ans = 0\n    for i, a in enumerate(nums[:-1]):\n        for j, b in enumerate(nums[ans:], ans):\n            if math.gcd(a, b) != 1:\n                ans = j\n        if i == ans:\n            return ans\n    return -1",
				// import math

				// def findValidSplit(nums):
				// 	last_valid_index = 0
				// 	# Duyệt qua tất cả các phần tử trừ phần tử cuối
				// 	for current_index, current_number in enumerate(nums[:-1]):  
				// 		for next_index, next_number in enumerate(nums[last_valid_index:], last_valid_index):
				// 			# Kiểm tra nếu GCD của hai số khác 1
				// 			if math.gcd(current_number, next_number) != 1:  
				// 				# Cập nhật chỉ số vị trí cuối hợp lệ nếu điều kiện thỏa mãn
				// 				last_valid_index = next_index  
				// 		# Nếu chỉ số hiện tại trùng với vị trí cuối hợp lệ
				// 		if current_index == last_valid_index:  
				// 			# Trả về chỉ số này làm vị trí chia hợp lệ
				// 			return last_valid_index  
				// 	# Nếu không có vị trí chia hợp lệ, trả về -1
				// 	return -1  
				"hint": {
					"type": "text",
					"content": ""
				},
				"video_solution": ""
			}
		],
		"categories": [
			{
				"name": "Phúc soạn",
				"id": 70
			},
			{
				"name": "Algorithms",
				"id": 1
			}
		]}
//+ Code 02 Bài 02
	{
		"question_id": 1982,
		"input_format": "Array, Array, Integer",
		"output_format": "Integer",
		"sample_input": "[3,6,1,3,4], [2,1,3,4,5], 25",
		"sample_output": "3",
		"_level": "hard",
		"created_at": "2023-11-06T18:55:01.585Z",
		"deleted_at": null,
		"en": {
			"question_title": "Maximum Number of Robots Within Budget",
			"problem": "You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget. Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.",
			"explanation": "You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget.\nThe total cost of running `k` chosen robots is equal to \nmax(chargeTimes) + k * sum(runningCosts), \nwhere max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.\nReturn the maximum number of consecutive robots you can run such that the total cost does not exceed budget.\n\nExample:\nInput: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25\nOutput: 3\nExplanation: \nIt is possible to run all individual and consecutive pairs of robots within budget.\nTo obtain answer 3, consider the first 3 robots. The total cost will be max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 which is less than 25.\nIt can be shown that it is not possible to run more than 3 consecutive robots within budget, so we return 3.",
			"constraint_input": "Array, Array, Interger",
			"constraint_output": "Interger",
			"constraint_time": "10000"
		},
		"vi": {
			"question_title": "Số Robot tối đa phù hợp ngân sách",
			"problem": "Bạn có n robots có chỉ số là chargeTimes và runningCosts. Robot thứ i mất chargeTimes[i] đơn vị để sạc và mất runningCosts[i] đơn vị để chạy. Bạn cũng được cung cấp một số nguyên budget. Trả về số lượng tối đa của robot liên tiếp mà bạn có thể chạy mà tổng chi phí không vượt quá ngân sách.",
			"explanation": "Bạn có n robots. Bạn được cung cấp hai mảng số nguyên có chỉ số 0 là chargeTimes và runningCosts, cả hai đều có độ dài là n. Robot thứ i mất chargeTimes[i] đơn vị để sạc và mất runningCosts[i] đơn vị để chạy. Bạn cũng được cung cấp một số nguyên budget.\n\nTổng chi phí chạy k robot đã chọn bằng max(chargeTimes) + k * sum(runningCosts), trong đó max(chargeTimes) là chi phí sạc lớn nhất giữa k robot và sum(runningCosts) là tổng chi phí chạy giữa k robot.\n\nTrả về số lượng tối đa của robot liên tiếp mà bạn có thể chạy mà tổng chi phí không vượt quá ngân sách.\n\nĐầu vào: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25\nĐầu ra: 3\nGiải thích:\nCó thể chạy tất cả các robot riêng lẻ và cặp robot liên tiếp trong ngân sách.\nĐể có đáp án là 3, hãy xem xét 3 robot đầu tiên. Tổng chi phí sẽ là \nmax(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24, thấp hơn 25.\n\nCó thể chứng minh rằng không thể chạy nhiều hơn 3 robot liên tiếp trong ngân sách, vì vậy chúng ta trả về 3.",
			"constraint_input": "Array, Array, Integer",
			"constraint_output": "Integer",
			"constraint_time": "10000"
		},
		"test_case": [
			{
				"testcase_id": 0,
				"_input": "[3,6,1,3,4], [2,1,3,4,5], 25",
				"_output": "3"
			},
			{
				"testcase_id": 1,
				"_input": "[11,12,19], [10,8,7], 19",
				"_output": "0"
			}
		],
		"init_code": [
			{
				"_language": "py",
				"tle": 10000,
				"_function": "from collections import deque\n\ndef maximumRobots():\n  # Your code here",
				"base_code": "__function__\nprint(maximumRobots(__test_case__))",
				"_answer": "from collections import deque\n\ndef maximumRobots(chargeTimes, runningCosts, budget):\n  prefix_sum = [0] * (len(chargeTimes) + 1)\n  max_count = 0\n  stack = deque()\n  for i in range(1, len(chargeTimes) + 1):\n    prefix_sum[i] = prefix_sum[i-1] + runningCosts[i-1]\n    \n    left = 0\n    for right in range(len(chargeTimes)):\n      \n      while stack and chargeTimes[stack[-1]] < chargeTimes[right]:\n        stack.pop()\n      \n      stack.append(right)\n      current_budget = chargeTimes[stack[0]] + (right+1-left) * (prefix_sum[right+1] - prefix_sum[left])\n      \n      while stack and current_budget > budget:\n        if left == stack[0]:\n          stack.popleft()\n        left += 1\n        if stack:\n          current_budget = chargeTimes[stack[0]] + (right+1-left) * (prefix_sum[right+1] - prefix_sum[left])\n      \n      if current_budget <= budget:\n            max_count = max(max_count, right+1-left)\n    return max_count",
				"hint": {
					"type": "text",
					"content": ""
				},
				"video_solution": ""
			}
		],
		"categories": [
			{
				"name": "Algorithms",
				"id": 1
			},
			{
				"name": "Phúc soạn",
				"id": 65
			}
		]}

//+ Trắc Nghiệm Buổi 03 Bài 01: Kiến Thức Về BigO\
	{
		"statusCode": 200,
		"message": null,
		"content": {
			"id": 15,
			"chuyenDeId": 0,
			"loaiChuyenDe": "CLASS",
			"monHocId": 1404,
			"tenNhiemVu": "Kiến thức về BigO",
			"tongCoin": 10,
			"tongExp": 186,
			"tagSkill": "PYTHON",
			"diemHoatDong": 0,
			"hoanThanhLabel": null,
			"hoanThanh": false,
			"truyCap": false,
			"trangThaiBaiTap": null,
			"taskIdNext": 16,
			"maLoaiNhiemVu": "QUIZ",
			"noiDungNhiemVu": [
				{
					"requiredId": 2756,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "Big O notation d&ugrave;ng &dstrok;&#x1ec3; &dstrok;&aacute;nh gi&aacute; g&igrave;&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "Thời gian chạy của một chương trình"
						},
						{
							"ma": "2",
							"noiDung": "Số lượng lỗi trong chương trình"
						},
						{
							"ma": "3",
							"noiDung": "Dung lượng bộ nhớ cần thiết"
						},
						{
							"ma": "4",
							"noiDung": " Cả a) và c)"
						}
					],
					"dapAn": [
						"rTRzOXuC8i+NmESact1F2A=="
					],
					"inputCss": null
				},
				{
					"requiredId": 2757,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "Big O notation cho bi&#x1ebf;t &dstrok;i&#x1ec1;u g&igrave; v&#x1ec1; hi&#x1ec7;u su&#x1ea5;t c&#x1ee7;a m&#x1ed9;t thu&#x1ead;t to&aacute;n&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "Thời gian thực thi tốt nhất"
						},
						{
							"ma": "2",
							"noiDung": "Thời gian thực thi trung bình"
						},
						{
							"ma": "3",
							"noiDung": "Tối đa thời gian thực thi trong trường hợp tệ nhất"
						},
						{
							"ma": "4",
							"noiDung": "Thời gian thực thi trung bình và trong trường hợp tệ nhất"
						}
					],
					"dapAn": [
						"NVbFzFf0j2fLeKBH72JsbA=="
					],
					"inputCss": null
				},
				{
					"requiredId": 2758,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "N&#x1ebf;u m&#x1ed9;t thu&#x1ead;t to&aacute;n c&oacute; &dstrok;&#x1ed9; ph&#x1ee9;c t&#x1ea1;p O&lpar;n&Hat;2&rpar; v&agrave; n&oacute; c&#x1ea7;n 1000ms &dstrok;&#x1ec3; ho&agrave;n th&agrave;nh khi n &equals; 10&comma; th&igrave; m&#x1ea5;t bao l&acirc;u &dstrok;&#x1ec3; ho&agrave;n th&agrave;nh khi n &equals; 100&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "10ms"
						},
						{
							"ma": "2",
							"noiDung": "100ms"
						},
						{
							"ma": "3",
							"noiDung": "1000ms"
						},
						{
							"ma": "4",
							"noiDung": "100000ms"
						}
					],
					"dapAn": [
						"rTRzOXuC8i+NmESact1F2A=="
					],
					"inputCss": null
				},
				{
					"requiredId": 2764,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "def example&lowbar;function&lpar;arr&rpar;&colon;\r&NewLine;    total &equals; 0\r&NewLine;    product &equals; 1\r&NewLine;    for num in arr&colon;\r&NewLine;        total &plus;&equals; num\r&NewLine;    for num in arr&colon;\r&NewLine;        product &ast;&equals; num\r&NewLine;    return total&comma; product\r&NewLine;    \r&NewLine;Cho &dstrok;o&#x1ea1;n ch&#x1b0;&#x1a1;ng tr&igrave;nh Python tr&ecirc;n&comma; &dstrok;&#x1ed9; ph&#x1ee9;c t&#x1ea1;p th&#x1edd;i gian c&#x1ee7;a ch&#x1b0;&#x1a1;ng tr&igrave;nh l&agrave;&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "O(1)"
						},
						{
							"ma": "2",
							"noiDung": "O(n)"
						},
						{
							"ma": "3",
							"noiDung": "O(n^2)"
						},
						{
							"ma": "4",
							"noiDung": "O(2n)"
						}
					],
					"dapAn": [
						"ncDKR/+sPpfLsUJ7Ah0LaA=="
					],
					"inputCss": null
				},
				{
					"requiredId": 2765,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "def example&lowbar;function&lpar;arr&rpar;&colon;\r&NewLine;    result &equals; 0\r&NewLine;    for i in range&lpar;len&lpar;arr&rpar;&rpar;&colon;\r&NewLine;        for j in range&lpar;len&lpar;arr&rpar;&rpar;&colon;\r&NewLine;            result &plus;&equals; arr&lbrack;i&rbrack; &plus; arr&lbrack;j&rbrack;\r&NewLine;    return result\r&NewLine;\r&NewLine;&Dstrok;&#x1ed9; ph&#x1ee9;c t&#x1ea1;p th&#x1edd;i gian c&#x1ee7;a &dstrok;o&#x1ea1;n ch&#x1b0;&#x1a1;ng tr&igrave;nh n&agrave;y l&agrave;&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "O(1)"
						},
						{
							"ma": "2",
							"noiDung": "O(n)"
						},
						{
							"ma": "3",
							"noiDung": "O(n^2)"
						},
						{
							"ma": "4",
							"noiDung": "O(2n^2)"
						}
					],
					"dapAn": [
						"NVbFzFf0j2fLeKBH72JsbA=="
					],
					"inputCss": null
				},
				{
					"requiredId": 2766,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "def example&lowbar;function&lpar;arr&rpar;&colon;\r&NewLine;    total &equals; 0\r&NewLine;    for num in arr&colon;\r&NewLine;        total &plus;&equals; num\r&NewLine;    return total\r&NewLine;\r&NewLine;&Dstrok;&#x1ed9; ph&#x1ee9;c t&#x1ea1;p th&#x1edd;i gian c&#x1ee7;a &dstrok;o&#x1ea1;n ch&#x1b0;&#x1a1;ng tr&igrave;nh n&agrave;y l&agrave;&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "O(1)"
						},
						{
							"ma": "2",
							"noiDung": "O(n)"
						},
						{
							"ma": "3",
							"noiDung": "O(n^2)"
						},
						{
							"ma": "4",
							"noiDung": "O(2n)"
						}
					],
					"dapAn": [
						"ncDKR/+sPpfLsUJ7Ah0LaA=="
					],
					"inputCss": null
				},
				{
					"requiredId": 2767,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "def example&lowbar;function&lpar;arr&rpar;&colon;\r&NewLine;    total &equals; 0\r&NewLine;    for i in range&lpar;len&lpar;arr&rpar;&rpar;&colon;\r&NewLine;        for j in range&lpar;len&lpar;arr&rpar;&rpar;&colon;\r&NewLine;            for k in range&lpar;len&lpar;arr&rpar;&rpar;&colon;\r&NewLine;                total &plus;&equals; arr&lbrack;i&rbrack; &plus; arr&lbrack;j&rbrack; &plus; arr&lbrack;k&rbrack;\r&NewLine;    return total\r&NewLine;\r&NewLine;&Dstrok;&#x1ed9; ph&#x1ee9;c t&#x1ea1;p th&#x1edd;i gian c&#x1ee7;a &dstrok;o&#x1ea1;n ch&#x1b0;&#x1a1;ng tr&igrave;nh n&agrave;y l&agrave;&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "O(1)"
						},
						{
							"ma": "2",
							"noiDung": "O(n)"
						},
						{
							"ma": "3",
							"noiDung": "O(n^2)"
						},
						{
							"ma": "4",
							"noiDung": "O(n^3)"
						}
					],
					"dapAn": [
						"rTRzOXuC8i+NmESact1F2A=="
					],
					"inputCss": null
				},
				{
					"requiredId": 2768,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "def example&lowbar;function&lpar;arr&rpar;&colon;\r&NewLine;    return arr&lbrack;0&rbrack;\r&NewLine;\r&NewLine;&Dstrok;&#x1ed9; ph&#x1ee9;c t&#x1ea1;p th&#x1edd;i gian c&#x1ee7;a &dstrok;o&#x1ea1;n ch&#x1b0;&#x1a1;ng tr&igrave;nh n&agrave;y&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "O(1)"
						},
						{
							"ma": "2",
							"noiDung": "O(n)"
						},
						{
							"ma": "3",
							"noiDung": "O(log n)"
						},
						{
							"ma": "4",
							"noiDung": "O(n^2)"
						}
					],
					"dapAn": [
						"EUoElvbAU57oL0v/sVRqyQ=="
					],
					"inputCss": null
				},
				{
					"requiredId": 2769,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "def example&lowbar;function&lpar;arr&rpar;&colon;\r&NewLine;    count &equals; 0\r&NewLine;    i &equals; 0\r&NewLine;    while i &lt; len&lpar;arr&rpar;&colon;\r&NewLine;        count &plus;&equals; arr&lbrack;i&rbrack;\r&NewLine;        i &plus;&equals; 1\r&NewLine;    return count\r&NewLine;\r&NewLine;&Dstrok;&#x1ed9; ph&#x1ee9;c t&#x1ea1;p th&#x1edd;i gian c&#x1ee7;a &dstrok;o&#x1ea1;n ch&#x1b0;&#x1a1;ng tr&igrave;nh n&agrave;y l&agrave;&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "O(1)"
						},
						{
							"ma": "2",
							"noiDung": "O(n)"
						},
						{
							"ma": "3",
							"noiDung": "O(log n)"
						},
						{
							"ma": "4",
							"noiDung": "O(n^2)"
						}
					],
					"dapAn": [
						"ncDKR/+sPpfLsUJ7Ah0LaA=="
					],
					"inputCss": null
				},
				{
					"requiredId": 2770,
					"tieuDe": "Hãy chọn đáp án đúng",
					"inPut": "def example&lowbar;function&lpar;n&rpar;&colon;\r&NewLine;    count &equals; 0\r&NewLine;    while n &gt; 0&colon;\r&NewLine;        count &plus;&equals; 1\r&NewLine;        n &sol;&sol;&equals; 10\r&NewLine;    return count\r&NewLine;\r&NewLine;&Dstrok;&#x1ed9; ph&#x1ee9;c t&#x1ea1;p th&#x1edd;i gian c&#x1ee7;a &dstrok;o&#x1ea1;n ch&#x1b0;&#x1a1;ng tr&igrave;nh n&agrave;y l&agrave;&quest;",
					"outPut": "",
					"maLoaiBaiTap": "single",
					"cauTraLoi": [
						{
							"ma": "1",
							"noiDung": "O(1)"
						},
						{
							"ma": "2",
							"noiDung": "O(n)"
						},
						{
							"ma": "3",
							"noiDung": "O(log n)"
						},
						{
							"ma": "4",
							"noiDung": "O(n^2)"
						}
					],
					"dapAn": [
						"NVbFzFf0j2fLeKBH72JsbA=="
					],
					"inputCss": null
				}
			],
			"listCheckHint": [
				{
					"maTieuDe": "HINT",
					"trangThai": false
				},
				{
					"maTieuDe": "SOLUTION",
					"trangThai": false
				},
				{
					"maTieuDe": "SOLUTION_VIDEO",
					"trangThai": false
				}
			],
			"getDiemBaiTapNop": null,
			"getDiemBaiTapQuiz": null,
			"xemDemo": false
		},
		"dateTime": "2024-09-23T23:03:17.7731423+07:00"
	}
