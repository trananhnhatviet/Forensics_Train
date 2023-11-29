# Memlab 6

Giờ mình imageinfo để lấy profile thôi

![1701229194971](image/Memlab6/1701229194971.png)

Profile của chall này là ``Win7SP1x64``, giờ mình pslist coi đang chạy tiến trình gì nha.

![1701229380457](image/Memlab6/1701229380457.png)

Mình thấy người dùng đang chạy tiến trình ``chrome.exe``, ``firefox.exe``, ``WinRAR.exe``, giờ mình đi lấy lịch sử truy cập của Chrome và Firefox coi có gì nha. 

Bài trước thì mình dùng AutoSpy để mở, cũng oki thui nhưng mà mình đã tìm hiểu được thêm 1 vài [plugins](https://github.com/superponible/volatility-plugins) mới ở đây giúp ta nhanh hơn trong việc lấy lịch sử trình duyệt nhanh hơn nha.

![1701229650888](image/Memlab6/1701229650888.png)


Sau một thời gian tìm kiếm thì mình tìm được quả link pastebin.com `` https://pastebin.com/RSGSi1hk`` ở dòng 169.

![1701229719457](image/Memlab6/1701229719457.png)

Sau khi vào link, ta được 1 đoạn link nữa.

![1701229776841](image/Memlab6/1701229776841.png)   

```
https://www.google.com/url?q=https://docs.google.com/document/d/1lptcksPt1l_w7Y29V4o6vkEnHToAPqiCkgNNZfS9rCk/edit?usp%3Dsharing&sa=D&source=hangouts&ust=1566208765722000&usg=AFQjCNHXd6Ck6F22MNQEsxdZo21JayPKug
```

Vào thì được 1 file doc ``Important``, tìm 1 hồi thì thấy 1 đường link ``https://mega.nz/#!SrxQxYTQ`` nữa.

![1701229843586](image/Memlab6/1701229843586.png)


Vào thì lại phải nhập mật khẩu ở mega.

![1701229868510](image/Memlab6/1701229868510.png)

Giờ ta đi tìm mật khẩu đã =(((

Sau khi lục lọi một lúc, thì mình thấy có 1 wu là dùng plugin ``screenshot``, thì mình dùng thử thì ngỡ ngàng ngạc nhiên và bật ngửa là nó có thật.

![1701230721161](image/Memlab6/1701230721161.png)

Sau khi thu được các ảnh, mình mở ra thì thấy ảnh ``session_1.WinSta0.Default.png``, có chụp lại gmail của David lại.

![1701230779106](image/Memlab6/1701230779106.png)

Giờ mình có gmail là ``davidbenjamin939@gmail.com``, mình thử coi nó có gửi password không nha.

Tìm thì nhiều quá, thế nên mình lại grep ``Mega Drive Key``, thì mình tìm được key ``THE KEY IS zyWxCjCYYSEMA-hZe552qWVXiPwa5TecODbjnsscMIU``.

![1701231396605](image/Memlab6/1701231396605.png)

Mở ra thì lại không được, mình dùng HxD để coi xem nó bị làm sao.

![1701231652869](image/Memlab6/1701231652869.png)

Mình tìm lại [writeup cũ](https://github.com/trananhnhatviet/Forensics_Train/blob/main/Task_2/Bai_1/PNG_Chunk.md) của mình thì thấy là ``IHDR chunk`` phải viết hoa hết thay vì viết thường chữ i, đổi lại thành Hoa thui.
![1701231685563](image/Memlab6/1701231685563.png)

![1701231700395](image/Memlab6/1701231700395.png)
Mở được rùi nè. Mình có nửa flag đầu tiên.

**Fisrt Part Flag: inctf{thi5_cH4LL3Ng3_!s_g0nn4_b3_?_**

Giờ mình thử tìm hiểu firefox xem có lịch sử gì không nha.

![1701231895108](image/Memlab6/1701231895108.png)

Không có gì thật, giờ mình xem cái WinRAR.

![1701231978368](image/Memlab6/1701231978368.png)

Đây rồi, flag.rar đây rồi, giờ dumpfiles thôi nào.

![1701232035837](image/Memlab6/1701232035837.png)


Đổi tên rồi unrar thôi nàoo
![1701232084401](image/Memlab6/1701232084401.png)

Còn phải có pass nữa =(((

Mình thử hết các lệnh hay dùng như là ``cmdline``, ``cmdscan``, ``consoles`` thì mình được cái này.

![1701234124891](image/Memlab6/1701234124891.png)

Mình nghĩ ngay đến plugin ``envars``. Việc gì mà không thử nào. Ghép thêm ``grep -i "pass"`` coi sao.

Tadaaa, mình dã có được password hihiihihi

![1701234284893](image/Memlab6/1701234284893.png)

Đó là ``easypeasyvirus``.

Giờ thì unrar thôi nào.

![1701234325138](image/Memlab6/1701234325138.png)

**Flag: inctf{thi5_cH4LL3Ng3_!s_g0nn4_b3_?_aN_Am4zINg_!_i_gU3Ss???_}**