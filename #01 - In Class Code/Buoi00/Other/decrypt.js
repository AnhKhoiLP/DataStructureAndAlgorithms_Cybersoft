//npm install crypto-js
//import CryptoJS from 'crypto-js';
const CryptoJS = require('crypto-js');
const key = 'b2314589FASe41121fbbce2eQF412916';
const decrypt = (cipherText) => {
  const keyBytes = CryptoJS.enc.Utf8.parse(key);
  const iv = CryptoJS.enc.Hex.parse('00000000000000000000000000000000'); // IV với toàn số 0

  const encrypted = CryptoJS.enc.Base64.parse(cipherText);

  const decrypted = CryptoJS.AES.decrypt(
    { ciphertext: encrypted },
    keyBytes,
    {
      iv: iv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    }
  );

  // Chuyển đổi từ dạng nhị phân sang chuỗi UTF-8 và trả về kết quả
  return decrypted.toString(CryptoJS.enc.Utf8);
};

// Ví dụ sử dụng
const cipherText = "ncDKR/+sPpfLsUJ7Ah0LaA==";
const decryptedText = decrypt(cipherText);
console.log(decryptedText);

// console.log("Câu: 01 | S | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
// console.log("Câu: 02 | S | " + decrypt("EUoElvbAU57oL0v/sVRqyQ=="));
// console.log("Câu: 03 | S | " + decrypt("EUoElvbAU57oL0v/sVRqyQ=="));
// console.log("Câu: 04 | S | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
// console.log("Câu: 05 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 06 | S | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
// console.log("Câu: 07 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 08 | S | " + decrypt("EUoElvbAU57oL0v/sVRqyQ=="));
// console.log("Câu: 09 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 10 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 11 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 12 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 13 | S | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
// console.log("Câu: 14 | S | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
// console.log("Câu: 15 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 16 | S | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
// console.log("Câu: 17 | S | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
// console.log("Câu: 18 | S | " + decrypt("EUoElvbAU57oL0v/sVRqyQ=="));
// console.log("Câu: 19 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 20 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 21 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 22 | S | " + decrypt("EUoElvbAU57oL0v/sVRqyQ=="));
// console.log("Câu: 23 | S | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
// console.log("Câu: 24 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 25 | S | " + decrypt("EUoElvbAU57oL0v/sVRqyQ=="));
// console.log("Câu: 26 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 27 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 28 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu: 29 | S | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu 01 | single | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
// console.log("Câu 02 | single | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu 03 | single | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
// console.log("Câu 04 | single | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
// console.log("Câu 05 | single | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));
// console.log("Câu 06 | single | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
// console.log("Câu 07 | single | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
// console.log("Câu 08 | single | " + decrypt("EUoElvbAU57oL0v/sVRqyQ=="));
// console.log("Câu 09 | single | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
// console.log("Câu 10 | single | " + decrypt("NVbFzFf0j2fLeKBH72JsbA=="));

console.log("Câu 01 | single | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
console.log("Câu 02 | single | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
console.log("Câu 03 | single | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
console.log("Câu 04 | single | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
console.log("Câu 05 | single | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
console.log("Câu 06 | single | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
console.log("Câu 07 | single | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
console.log("Câu 08 | single | " + decrypt("rTRzOXuC8i+NmESact1F2A=="));
console.log("Câu 09 | single | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));
console.log("Câu 10 | single | " + decrypt("ncDKR/+sPpfLsUJ7Ah0LaA=="));

