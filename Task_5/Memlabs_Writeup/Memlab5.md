# Memlab 5

Giờ mình vẫn imageinfo để biết profile của nó như nào thui.

![1701158080675](image/Memlab5/1701158080675.png)

Profile của file này là ``Win7SP1x64``

Giờ mình sẽ dùng pslist để coi xem có gì đang chạy nhaaa

![1701158211388](image/Memlab5/1701158211388.png)

Ta thấy là đang chạy ``WinRAR.exe`` và ``NOTEPAD.exe``.

Giờ mình filescan kết hợp grep để tìm các file .rar thôi.

![1701158407774](image/Memlab5/1701158407774.png)

Tìm thì được 1 file ``SW1wb3J0YW50.rar``, ta lấy phyoffset ``0x000000003eed56f0`` rồi dumpfile thôi.

![1701158584088](image/Memlab5/1701158584088.png)

Đổi tên rồi unrar coi có gì nha.

![1701158637469](image/Memlab5/1701158637469.png)

Có pass rồi, mà đây là stage 2 thế thì phải đi tìm flag stage 1 trước đã.

Sau khi mất một khoảng thời gian mò thì mình đã chịu và đi coi wu thì thấy họ dùng plugin ``iehistory``.

Plugin ``iehistory`` sẽ giúp ta khôi phục các đoạn của tệp bộ nhớ đệm index.dat lịch sử Internet Explorer. Nó có thể tìm các liên kết được truy cập cơ bản (thông qua FTP hoặc HTTP). Nó áp dụng cho mọi quy trình tải và sử dụng thư viện wininet.dll, không chỉ riêng Internet Explorer. Thông thường sẽ bao gồm cả File Explorer và các phầm mềm độc hại.

Sau khi dùng plugin này, ta thấy được 1 file .bmp mà có tiêu đề là mã base64 là ``ZmxhZ3shIV93M0xMX2QwbjNfU3Q0ZzMtMV8wZl9MNEJfM19EMG4zXyEhfQ``

![1701159933690](image/Memlab5/1701159933690.png)

Decode thì thu được flag đầu tiên.

![1701159962687](image/Memlab5/1701159962687.png)

**First Flag: flag{!!_w3LL_d0n3_St4g3-1_0f_L4B_5_D0n3!!}**

Giờ có flag đầu rồi, extract file rar kia thui, vì theo mô tả thì có flag 1 thì mới có flag 2 được.

![1701179468593](image/Memlab5/1701179468593.png)

**Second FLag: flag{W1th_th1s_$taGe_2_1s_c0mPL3T3_!!}**

Mình tưởng là chỉ có 2 flag tại vì trong ảnh bảo là final, thế nhưng mô tả thì lại bảo có flag thứ 3.

Nhìn kỹ lại pslist thì cũng có 1 file ``WerFault.exe`` lạ quá, thế nên là mình thử phân tích nó coi sao.

Mình sẽ thử ``cmdline`` để coi xem người dùng đã gõ những lệnh nào trên cmd.

![1701181598744](image/Memlab5/1701181598744.png)

Ái chà chà, chương trình lạ này có sử dụng PID, mình thử pslist lại thì PID này chính là của NOTEPAD.exe. Mình nghi là tệp ``WerFault.exe`` sẽ giả mạo ``NOTEPAD.exe`` để tấn công máy người dùng.

![1701181703716](image/Memlab5/1701181703716.png)

Giờ mình sẽ dùng plugin ``procdump`` để kết xuất tệp thực thi tiến trình của file .exe độc này. Khác với plugin ``memdump``, plugin trích xuất tất cả các trang lưu trữ trong bộ nhớ của một quy trình, thì ``procdump`` sẽ giúp ta kết xuất file .exe này. Vì có thể đây không phải là ``NOTEPAD.exe`` chính gốc mà là một phần mêm khác mạo danh.

![1701183447607](image/Memlab5/1701183447607.png)

Giờ mở IDA lên coi có thể reverse lại exe này không.

Sau khi mở IDA, vào phần WinMainCRTStartup, thì mình thu được flag nha cả nhà iu của em.

![1701183528738](image/Memlab5/1701183528738.png)

**Third Flag: bi0s{M3m_l4B5_OVeR_!}**
