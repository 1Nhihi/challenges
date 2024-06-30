# chall1.exe
ném vào Detect It Easy thì biết được file này là py -> exe nên dùng [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) decompile file này để có đc file pyc và dùng [Uncompyle6](https://github.com/rocky/python-uncompyle6/) and [Decompyle++](https://github.com/zrax/pycdc) để chuyển file pyc thành py thì thấy được code của bài như thế này:
```python=
import base64

def main():
    Flag = input('[+] Input Flag: ')
    b = ''
    for i in Flag:
        k = 7
        for j in range(8):
            b += str(ord(i) >> k & 1)
            k = k - 1


    if b == '0100011101000100010101010100001101010100010001100111101101110000001101110101111101110100011011110101111100110011011110000011001101111101':
        print('Correct')
    else:
        print('Incorrect')

if __name__ == '__main__':
    main()
```
hiểu đơi giản thì code nó chỉ chuyển đổi các ký tự thành một dãy binary rồi and với 1 thôi  -> sờ cờ ríp của bài:
```python=
b = '0100011101000100010101010100001101010100010001100111101101110000001101110101111101110100011011110101111100110011011110000011001101111101'
binary_array = []

for i in range(0,len(b),8):
	binary_array.append(int(b[i:i+8],2))
	
a = "".join(map(chr,binary_array))
print(a)
# GDUCTF{p7_to_3x3}
```
> flag là :  "GDUCTF{p7_to_3x3}"
