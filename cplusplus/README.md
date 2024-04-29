# cplusplus
- Challenge name: cplusplus
- Given file: [cplusplus](./cplusplus) và [output.txt](./output.txt)
  
chạy thử chương trình thì thấy chạy hoài chạy hoài mà không dừng thì thế nên nhảy vào IDA check thử

Đọc code thì hiểu đơn giản là chương trình random 2 số bất kì rồi chạy qua 3 hàm và in ra kết quả 
![image](https://github.com/1Nhihi/nhap/assets/127366803/e85d0490-acd8-4a57-a3c7-08ae886d667e)

và biết được format của flag là "amateursCTF{...}" vì thế nên mình brute force 2 tham số đầu vào 

```python3=
def Addition(a, b):
	return (a + b)% 0x3B9ACA07

def Multiplication(a1, a2):    		
    return (a1 * a2) % 0x3B9ACA07

def sub_555555555374(a1,a2):
	a3 = 1
	while a2:
		if a2 &1:
			a3 = Multiplication(a3, a1) % 0x3B9ACA07
		a1 = Multiplication(a1,a1) % 0x3B9ACA07
		a2 >>=1
	return a3

a = ord('a')

for i in range( 0xff):
	for j in range( 0xff):

		v6  = 0

		v3 = Addition(v6, a)
		v4 = Multiplication(v3, i)
		v6 = sub_555555555374(v4 , j)
		if v6 == 816696039:
			print(v6, i, j)

# 816696039 237 41
```

có được 2 số random là 237 và 41 và ouput rồi thì mình tiếp lục brute force các ký tự 1 lần nữa và có được script là [script](./script.py)

> 🚩: `amateursCTF{r/programminghorror/comments/18x7vk9/}`
