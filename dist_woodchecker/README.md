
# dist_woodchecker
Đề bài cho ta 2 file là "cpu.py" và "woodchecker.wpk"
kiểm tra  thấy file .wpk là dạng text.
Mở 2 file ra xem thì thấy trong "woodchecker.wpk" chứa các opcodes còn "cpu.py" gọi "woodchecker.wpk" để kiểm tra flag nhập vào có đúng không (VM)
vì đề bài yêu cầu phải nhập vào chuỗi có độ dài 20:
![](https://hackmd.io/_uploads/HkeZCbvPn.png)


nên lấy  một string có độ dài 20 và kiểm tra trong trường hợp nào thì cpu.store trả về 1
* chú ý: flag có có kiểu dữ liệu là 'bytes' 

```python=
f = open("woodchecker.wpk").readlines()
flag = b'hihihuhuhahakakalala'

addr = 0
store = 0
mem = bytearray(1 << 29)
mem[:len(flag)] = flag
op = 0
cnt = 0
k = 1
arr = []
for i in f:
    if 'INC' in i:
        addr += 1

    elif 'INV' in i:
        mem[addr // 8] ^= 1 << (addr % 8)
    elif 'LOAD' in i:
        store = mem[addr // 8] >> (addr % 8) & 1
        if(store == 1):
            print('store = mem[' + str(addr // 8) + '] >> (' + str(addr % 8) + ') & 1, store =', store,end = "")
            print("------------------------------",k)
        k+=1
    elif 'CDEC' in i:
        addr -= store   
```

chạy thử:
![](https://hackmd.io/_uploads/B1cLIZvwh.png)


nó trả về giá trị store với phép tính của store tướng ứng
trong đề: cpu.mem[:len(flag)]  
vậy nên chỉ cần quan tâm tới mem[19] + nó dịch phải tương ứng từ 0 tới 7 (8 lần) 
vì thế nên vị trí đầu tiên để kiểm tra là dòng thứ 482 của LOAD opcodes (mem[19]>>7)
-> Cách làm là khởi tạo biến 'l = 482' và một biết count = 0 để đến khi tất cả store của 8 lần dịch phải đều = 1 -> out = kí tự đó + out
```python= 
f = open("woodchecker.wpk").readlines()
print("Hihi")
l = 482
out = b''
for c in range(20):
    line = l
    for ch in range(32, 128):
        flag = chr(ch).encode() + out
        while len(flag) < 20:
            flag = b'n' + flag
        
        mem = bytearray(1 << 29)
        mem[:len(flag)] = flag
        addr = 0
        store = 0

        op = 0
        count = 0

        for i in f:
            if 'INC' in i:
                addr += 1
            elif 'INV' in i:
                mem[addr // 8] ^= 1 << (addr % 8)
            elif 'LOAD' in i:
                store = mem[addr // 8] >> (addr % 8) & 1
                op += 1
            elif 'CDEC' in i:
                addr -= store

            if op == line:
                if store == 1:
                    count += 1
                    line += 1
                    if count == 8:
                        out = chr(ch).encode() + out
                        print(out.decode())
                        l = line
                        break
                else:
                    line = l
#SEE{pIcKyP1CIF0rmeS}
```
>Vậy flag là: "SEE{pIcKyP1CIF0rmeS}"
