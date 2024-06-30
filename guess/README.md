# gues.exe

Chạy thử file:

![](https://hackmd.io/_uploads/Sy0rtGAvh.png)

Mở IDA:

![](https://hackmd.io/_uploads/HyM2FfAw3.png)
nếu mà độ dài chuỗi > 4 thì in ra "too long"

hỏi chatGPT thì nó bày dùng subprocess, với input đầu vào thì brute force chuỗi có 4,3,2,1 ký tự 
![](https://hackmd.io/_uploads/SJ9CjG0D2.png)

thêm điểu kiện bỏ qua lỗi "UnicodeDecodeError" có được script:
```py=
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"  

import subprocess
def out(a):
    # Tạo một quy trình subprocess
    process = subprocess.Popen(['gues.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    input_str = a

    process.stdin.write(input_str)
    process.stdin.close()

    # Đọc kết quả output từ stdout
    try:
        output_str = process.stdout.read()
        if "{" in output_str and "}" in output_str:
            print("Output:", output_str)

    except UnicodeDecodeError:
        pass

    # Đọc kết quả lỗi từ stderr (nếu có)
    error_str = process.stderr.read()

    # Đợi quy trình kết thúc
    process.wait()

    # In kết quả
    # print("Error:", error_str)

for i in characters:
    for j in characters:
        for k in characters:
            for h in characters:
                key = i+j+k+h 
                out(key)
                
            key = i+j+k
            out(key)
        key = i+j
        out(key)
    key = i 
    out(key)

#KCSC{brut6_n6rv6r_die}
```
![](https://hackmd.io/_uploads/SyKKAMRvn.png)
>flag là: "KCSC{brut6_n6rv6r_die}"
