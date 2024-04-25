def base10_to_base17(number):
    if number == 0:
        return "0"

    digits = "0123456789ABCDEF"
    base17 = ""
    while number:
        base17 = digits[number % 17] + base17
        number //= 17
    return base17

# return: a - (temp2 - temp1)
def sub(a ):  
	return a - 0x1ab508ca3bebb49643721d1ebbcc0ea46ed44dca6179

x = 0x5915f8ba06db0a50aa2f3eee4baef82e70be1a9ac80cb59e5b9cb15a15a7f7246604a5e456ad5324167411480f893f97e3
x = sub(x)
x = base10_to_base17(x)

# Chia chuỗi hex thành các cặp
x = [x[i:i+2] for i in range(0, len(x), 2)]

# Chuyển đổi từ hex sang ký tự ASCII
x = [chr(int(pair, 16) +12) for pair in x]
print("".join(x))

arr = [9, 11, 7, 13, 5, 15, 3, 17, 1, 19, 0, 21, 2, 23, 4, 25, 6, 27, 8, 29, 10, 31, 12, 33, 14, 35, 16, 37, 18, 39, 20, 41, 22, 43, 24, 45, 26, 47, 28, 46, 30, 44, 32, 42, 34, 40, 36, 38]

for i in range(48):
  for j in range(48):
      if arr[j] == i:
          print(x[j],end = "")
          break


