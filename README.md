# LIGHTS CONTROL USING HAND GESTURE RECOGNITION

## Group member:
- Lê Hồng Nguyên
- Trần Phước Hiền
- Lê Phan Minh Thông

## Content of Report:
|Column 1| Column 2|
| ------------- |:-------------:|
|Introduction about this project|3|
|About hardware|3|
|Components|3|
|Properties of components|3|
|Schematic design|5|
|About software|5|
|Requirement analysis|5|
|Flowchart|6|
|Source code|6|
|Implementation and inspection|7|
|Conclusion|7|

## Introduction about this project
- Chúng ta rất quen làm việc với máy tính thông qua “công cụ” bàn phím và chuột. Với tiến bộ công nghệ đáng kinh ngạc đã tạo nên những cách tương tác mới giữa người và máy, nổi bật như màn hình chạm (như iPhone, iPad) và cử động (như Nintendo Wii), rồi đến công nghệ điều khiển bằng giọng nói (như Siri). Nhiều thiết bị “thông minh” hiện nay còn cho phép người dùng “nhập” văn bản trực tiếp bằng cách đọc (nhờ phần mềm nhận dạng giọng nói). Để việc tương tác người-máy ngày càng tự nhiên và thoải mái, người ta đã phát triển các công nghệ cho phép sử dụng cử chỉ để điều khiển máy tính và các thiết bị số khác.
- Với dự án này, chúng tôi hy vọng có thể đem lại sự tiện lợi và thoải mái đến cho mọi người thông qua việc sử dụng cử chỉ của bàn tay để điều khiển 1 thiết bị rất quen thuộc trong cuộc sống hằng ngày là đèn điện. 
- Bởi vì cử chỉ cũng được coi là ngôn ngữ của cơ thể. Việc điều khiển đèn thông qua cử chỉ sẽ diễn ra nhanh chóng và tự nhiên hơn thay vì sử dụng công tắc truyền thống hay ra lệnh bằng giọng nói.

## About hardware
a. Components
|Column 1| Column 2|
| ------------- |:-------------:|
|cổng COMPIM|2|
|đèn LED-GREEN|1|
|đèn LED-RED|1|
|mạch SIMULINO UNO|1|
|Camera|1|
|PC|1|
|RES 220 Ohm|2|
|chân GROUND|1|

b. Properties of components

Cổng COMPIM
- Nó làm việc như một điểm gắn kết, nơi mà cáp từ thiết bị ngoại vi có thể được cắm vào , thông qua đó, cho phép dữ liệu truyền đi và đến thiết bị

LED-RED
- Còn gọi là “Điốt phát sáng” được làm từ vật liệu bán dẫn GaAsP, bước sóng 630-660 nm, hoạt động ở mức điện áp 1.8V

LED-GREEN
- Còn gọi là “Điốt phát sáng” được làm từ vật liệu bán dẫn AIGaP, bước sóng 550-570 nm, hoạt động ở mức điện áp 3.5V

Mạch SIMULINO UNO
- Đây là một bảng mạch vi điều khiển nguồn mở dựa trên vi điều khiển Microchip ATmega328 được phát triển bởi Arduino.cc. Bảng mạch được trang bị các bộ chân đầu vào/ đầu ra Digital và Analog có thể giao tiếp với các bảng mạch mở rộng khác nhau

Camera
- Đây là thiết bị ghi hình có khả năng ghi lại các dữ liệu về môi trường như màu sắc, chuyển động, hình dạng vật thể, …

PC
- Là máy tính cá nhân có khả năng xử lý dữ liệu và tương tác mạnh mẽ

Chân GROUND
- Đây là điểm tham chiếu cho tất cả các tín hiệu hoặc đường dẫn chung trong mạch điện nơi có thể đo được tất cả các điện áp. Đây cũng được gọi là cống (drain) chung vì phép đo điện áp dọc theo nó bằng không

c. Schematic design

<img src="https://github.com/hienlu2010vn/pythonLedController/blob/main/Images/Schematic%20design.png">
## About software
- Requirement analysis
	<ul>
	<li>Non-functional Requirements</li>
	<li>Functional Requirements: Điều khiển tắt mở đèn</li>
	</ul>

- Flowchart
<img src="https://github.com/hienlu2010vn/pythonLedController/blob/main/Images/Flowchart.png">


- [Source code](https://github.com/hienlu2010vn/pythonLedController)

## Implementation and inspection
<img src="https://github.com/hienlu2010vn/pythonLedController/blob/main/Images/Implementation%20and%20inspection.png">

## Conclusion
- Hệ thống hoạt động ổn định khi chạy thử nghiệm
- Một số lỗi có thể xảy ra khi có nhiều người cùng xuất hiện trong khu vực khiến hệ thống không hoạt động được
- Trong tương lai, hệ thống cần được nâng cấp để có thể hoạt động được trong nhiều hoàn cảnh khác nhau và cải thiện hiệu năng

