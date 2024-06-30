# chall1
Mở folder ra thì thấy có 2 file:
![](https://hackmd.io/_uploads/SJmeOsiF3.png)
nhưng  mà chỉ cần quan tâm  BruteJeeps.exe thôi
chạy thử file nhập đại đầu vào thì đầu ra nó cũng ra đại một chuỗi nào đó 
![](https://hackmd.io/_uploads/BkPn_ooYn.png)

ném vào ida
tại vào ida không thấy hàm main nên shift F12 để xem thử:
![](https://hackmd.io/_uploads/rkNFYjsYn.png)

thấy có "Input key:" nè nhảy tới nơi gọi nó thì thấy nếu như mà chiều dài của str đầu vào lớn hơn 4 thì in ra "too long"
![](https://hackmd.io/_uploads/HJk4qisY3.png)
tới đây mượn sờ cờ rip của "gues.exe" đầu tiên:
> flag: "GDUCTF{b6ut3_n3v3r_di33}"